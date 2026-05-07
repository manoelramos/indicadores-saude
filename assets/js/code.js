// CODE

function normalizarIndentacao(codeElement) {
    // Pega o texto puro (sem tags), usado para calcular indentação lógica
    let texto = codeElement.textContent.split("\n");

    while (texto[0].trim() === "") texto.shift();
    while (texto[texto.length - 1].trim() === "") texto.pop();

    const minIndent = Math.min(
        ...texto
            .filter(l => l.trim() !== "")
            .map(l => l.match(/^(\s*)/)[0].length)
    );

    // Agora aplica a remoção na versão com HTML (preservando as cores)
    let linhasHTML = codeElement.innerHTML.split("\n");
    linhasHTML = linhasHTML.map(l => l.replace(new RegExp("^\\s{" + minIndent + "}"), ""));
    codeElement.innerHTML = linhasHTML.join("\n");
}

function copiarCodigo(codeElement) {
    const texto = codeElement.textContent;
    navigator.clipboard.writeText(texto);
}

document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".code-container").forEach(container => {
        const code = container.querySelector("code");
        normalizarIndentacao(code);

         // Opção 1: Usa o botão já existente NO HTML
        const btn = container.querySelector(".copy-btn");
        if (btn) {
            btn.onclick = () => copiarCodigo(code);
        }

        //Opção 2: Cria um novo botão e adiciona ele no HTML
        // const btn = document.createElement("button");
        // btn.textContent = "Copiar";
        // btn.className = "copy-btn";
        // btn.onclick = () => copiarCodigo(code);
        // container.appendChild(btn);
    });
});



document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll("pre code").forEach(code => {
        const linhas = code.innerHTML.split("\n");

        const minIndent = Math.min(
            ...linhas
                .filter(l => l.trim().length > 0)
                .map(l => l.match(/^(\s*)/)[0].length)
        );

        const novoHTML = linhas.map(l => l.slice(minIndent)).join("\n");

        code.innerHTML = novoHTML;
    });
});
