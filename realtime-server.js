const http = require("node:http");
const fs = require("node:fs");
const path = require("node:path");
const { URL } = require("node:url");

const HOST = process.env.HOST || "0.0.0.0";
const PORT = Number(process.env.PORT || 3000);
const ROOT_DIR = __dirname;

const MIME_TYPES = {
	".html": "text/html; charset=utf-8",
	".css": "text/css; charset=utf-8",
	".js": "application/javascript; charset=utf-8",
	".json": "application/json; charset=utf-8",
	".svg": "image/svg+xml",
	".png": "image/png",
	".jpg": "image/jpeg",
	".jpeg": "image/jpeg",
	".gif": "image/gif",
	".webp": "image/webp",
	".ico": "image/x-icon",
	".pdf": "application/pdf",
	".woff": "font/woff",
	".woff2": "font/woff2",
};

const clients = new Set();
let lastRealtimeEvent = buildEventPayload("Servidor em tempo real iniciado.");

function buildEventPayload(message) {
	return {
		message,
		timestamp: new Date().toISOString(),
		connectedClients: clients.size,
	};
}

function writeSseEvent(response, eventName, payload) {
	response.write(`event: ${eventName}\n`);
	response.write(`data: ${JSON.stringify(payload)}\n\n`);
}

function broadcastEvent(payload) {
	lastRealtimeEvent = payload;
	for (const client of clients) {
		writeSseEvent(client, "update", payload);
	}
}

function sendJson(response, statusCode, body) {
	response.writeHead(statusCode, {
		"Content-Type": "application/json; charset=utf-8",
	});
	response.end(JSON.stringify(body));
}

function resolveFilePath(urlPathname) {
	const sanitizedPath = path.normalize(decodeURIComponent(urlPathname)).replace(/^(\.\.[/\\])+/, "");
	const requestedPath = sanitizedPath === "/" ? "/index.html" : sanitizedPath;
	const absolutePath = path.join(ROOT_DIR, requestedPath);
	if (!absolutePath.startsWith(ROOT_DIR)) {
		return null;
	}
	return absolutePath;
}

function handleStaticFile(requestUrl, response) {
	const filePath = resolveFilePath(requestUrl.pathname);
	if (!filePath) {
		sendJson(response, 403, { error: "Acesso negado." });
		return;
	}

	fs.stat(filePath, (statError, stats) => {
		if (statError || !stats.isFile()) {
			sendJson(response, 404, { error: "Arquivo não encontrado." });
			return;
		}

		const extension = path.extname(filePath).toLowerCase();
		const contentType = MIME_TYPES[extension] || "application/octet-stream";
		response.writeHead(200, { "Content-Type": contentType });
		fs.createReadStream(filePath).pipe(response);
	});
}

function requestBodyToJson(request) {
	return new Promise((resolve, reject) => {
		let body = "";
		request.on("data", (chunk) => {
			body += chunk.toString();
			if (body.length > 1_000_000) {
				reject(new Error("Corpo da requisição excedeu o limite."));
			}
		});
		request.on("end", () => {
			if (!body) {
				resolve({});
				return;
			}
			try {
				resolve(JSON.parse(body));
			} catch (error) {
				reject(new Error("JSON inválido."));
			}
		});
		request.on("error", reject);
	});
}

const server = http.createServer(async (request, response) => {
	const requestUrl = new URL(request.url, `http://${request.headers.host || "localhost"}`);

	if (requestUrl.pathname === "/events" && request.method === "GET") {
		response.writeHead(200, {
			"Content-Type": "text/event-stream",
			"Cache-Control": "no-cache, no-transform",
			Connection: "keep-alive",
			"Access-Control-Allow-Origin": "*",
		});

		clients.add(response);
		writeSseEvent(response, "update", buildEventPayload("Cliente conectado ao stream."));
		writeSseEvent(response, "update", lastRealtimeEvent);

		request.on("close", () => {
			clients.delete(response);
		});
		return;
	}

	if (requestUrl.pathname === "/api/realtime/status" && request.method === "GET") {
		sendJson(response, 200, buildEventPayload(lastRealtimeEvent.message));
		return;
	}

	if (requestUrl.pathname === "/api/realtime/update" && request.method === "POST") {
		try {
			const payload = await requestBodyToJson(request);
			const message = typeof payload.message === "string" && payload.message.trim()
				? payload.message.trim()
				: "Atualização recebida no servidor.";
			const eventPayload = buildEventPayload(message);
			broadcastEvent(eventPayload);
			sendJson(response, 200, eventPayload);
		} catch (error) {
			sendJson(response, 400, { error: error.message });
		}
		return;
	}

	if (request.method === "OPTIONS") {
		response.writeHead(204, {
			"Access-Control-Allow-Origin": "*",
			"Access-Control-Allow-Methods": "GET,POST,OPTIONS",
			"Access-Control-Allow-Headers": "Content-Type",
		});
		response.end();
		return;
	}

	handleStaticFile(requestUrl, response);
});

setInterval(() => {
	const heartbeat = buildEventPayload("Sincronização automática.");
	broadcastEvent(heartbeat);
}, 10000);

server.listen(PORT, HOST, () => {
	console.log(`Servidor em execução: http://${HOST}:${PORT}`);
	console.log("SSE disponível em /events");
});
