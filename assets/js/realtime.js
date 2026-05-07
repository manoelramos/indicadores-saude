(function () {
	function ensureRealtimeBadge() {
		var titleContainer = document.querySelector(".header .title");
		if (!titleContainer) {
			return null;
		}

		var badge = document.getElementById("realtime-status-badge");
		if (badge) {
			return badge;
		}

		badge = document.createElement("p");
		badge.id = "realtime-status-badge";
		badge.style.margin = "4px 0 0";
		badge.style.fontSize = "12px";
		badge.style.opacity = "0.9";
		badge.style.color = "#ffffff";
		badge.textContent = "Tempo real: desconectado";
		titleContainer.appendChild(badge);
		return badge;
	}

	function updateBadge(badge, payload, connected) {
		if (!badge) {
			return;
		}

		var timestamp = payload && payload.timestamp
			? new Date(payload.timestamp).toLocaleTimeString("pt-BR")
			: "--:--:--";
		var message = payload && payload.message ? payload.message : "Sem mensagem";
		var clients = payload && typeof payload.connectedClients === "number"
			? payload.connectedClients
			: 0;
		var statusText = connected ? "conectado" : "desconectado";
		var color = connected ? "#9af7b0" : "#ffc6c6";

		badge.style.color = color;
		badge.textContent = "Tempo real: " + statusText + " | " + message + " | " + timestamp + " | clientes: " + clients;
	}

	function initRealtime() {
		var badge = ensureRealtimeBadge();
		if (!badge || typeof EventSource === "undefined") {
			return;
		}

		try {
			var stream = new EventSource("/events");

			stream.addEventListener("update", function (event) {
				try {
					var payload = JSON.parse(event.data);
					updateBadge(badge, payload, true);
				} catch (error) {
					updateBadge(badge, null, false);
				}
			});

			stream.onerror = function () {
				updateBadge(badge, null, false);
			};
		} catch (error) {
			updateBadge(badge, null, false);
		}
	}

	if (document.readyState === "loading") {
		document.addEventListener("DOMContentLoaded", initRealtime);
	} else {
		initRealtime();
	}
})();
