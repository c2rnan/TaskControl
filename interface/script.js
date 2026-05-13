const API = "http://localhost:5000/tarefas";

let _allTasks = [];
let _currentFilter = "todas";

// ── Carrega do backend ─────────────────────────────────
function carregarTarefas() {
    fetch(API)
        .then(res => res.json())
        .then(dados => {
            _allTasks = dados;
            atualizarContador();
            aplicarFiltro();
        })
        .catch(() => mostrarErro("Não foi possível conectar ao servidor."));
}

// ── Renderiza com filtro aplicado ──────────────────────
function aplicarFiltro() {
    const filtrados = _currentFilter === "todas"
        ? _allTasks
        : _allTasks.filter(t => t.status === _currentFilter);

    const lista = document.getElementById("lista");
    const emptyState = document.getElementById("empty-state");
    lista.innerHTML = "";

    if (filtrados.length === 0) {
        emptyState.style.display = "flex";
        return;
    }
    emptyState.style.display = "none";

    filtrados.forEach((t, i) => {
        const card = document.createElement("li");
        card.className = `card ${t.status}`;
        card.style.animationDelay = `${i * 60}ms`;

        const prioLabel = {
            alta:  '<span class="prio alta">● Alta</span>',
            media: '<span class="prio media">● Média</span>',
            baixa: '<span class="prio baixa">● Baixa</span>',
        }[t.prioridade] || "";

        const statusLabel = t.status === "concluida"
            ? '<span class="status-badge concluida">✔ Concluída</span>'
            : '<span class="status-badge pendente">◌ Pendente</span>';

        card.innerHTML = `
            <div class="card-top">
                <strong class="card-titulo ${t.status === "concluida" ? "riscado" : ""}">${t.titulo}</strong>
                ${statusLabel}
            </div>
            ${t.descricao ? `<p class="card-desc">${t.descricao}</p>` : ""}
            <div class="card-meta">
                ${prioLabel}
                ${t.usuario ? `<span class="card-user">👤 ${t.usuario}</span>` : ""}
            </div>
            <div class="actions">
                ${t.status !== "concluida"
                    ? `<button class="btn-concluir" onclick="concluir(${t.id})">✔ Concluir</button>`
                    : ""}
                <button class="btn-deletar" onclick="deletar(${t.id})">🗑 Remover</button>
            </div>
        `;

        lista.appendChild(card);
    });
}

// ── Filtro ─────────────────────────────────────────────
function filtrar(tipo, btn) {
    _currentFilter = tipo;
    document.querySelectorAll(".filter-btn").forEach(b => b.classList.remove("active"));
    btn.classList.add("active");
    aplicarFiltro();
}

// ── Contador ───────────────────────────────────────────
function atualizarContador() {
    const total     = _allTasks.length;
    const pendentes = _allTasks.filter(t => t.status === "pendente").length;
    const conc      = _allTasks.filter(t => t.status === "concluida").length;
    const el = document.getElementById("task-count");
    if (el) el.textContent = `${total} tarefa${total !== 1 ? "s" : ""} · ${pendentes} pendente${pendentes !== 1 ? "s" : ""} · ${conc} concluída${conc !== 1 ? "s" : ""}`;
}

// ── CRUD ───────────────────────────────────────────────
function criarTarefa() {
    const titulo     = document.getElementById("titulo").value.trim();
    const descricao  = document.getElementById("descricao").value.trim();
    const prioridade = document.getElementById("prioridade").value;
    const usuario    = document.getElementById("usuario").value.trim();

    if (!titulo) {
        shakeCampo("titulo");
        return;
    }

    const btn = document.querySelector(".btn-criar");
    btn.disabled = true;
    btn.querySelector("span:last-child").textContent = "Criando...";

    fetch(API, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ titulo, descricao, prioridade, usuario })
    })
    .then(() => {
        limparCampos();
        _currentFilter = "todas";
        document.querySelectorAll(".filter-btn").forEach((b, i) => {
            b.classList.toggle("active", i === 0);
        });
        carregarTarefas();
    })
    .catch(() => mostrarErro("Erro ao criar tarefa."))
    .finally(() => {
        btn.disabled = false;
        btn.querySelector("span:last-child").textContent = "Criar Tarefa";
    });
}

function concluir(id) {
    fetch(`${API}/${id}`, { method: "PUT" })
        .then(() => carregarTarefas())
        .catch(() => mostrarErro("Erro ao concluir tarefa."));
}

function deletar(id) {
    if (!confirm("Remover esta tarefa?")) return;
    fetch(`${API}/${id}`, { method: "DELETE" })
        .then(() => carregarTarefas())
        .catch(() => mostrarErro("Erro ao remover tarefa."));
}

// ── Helpers ────────────────────────────────────────────
function limparCampos() {
    ["titulo", "descricao", "prioridade", "usuario"].forEach(id => {
        document.getElementById(id).value = "";
    });
}

function shakeCampo(id) {
    const el = document.getElementById(id);
    el.classList.add("shake");
    el.focus();
    setTimeout(() => el.classList.remove("shake"), 500);
}

function mostrarErro(msg) {
    const toast = document.createElement("div");
    toast.className = "toast";
    toast.textContent = msg;
    document.body.appendChild(toast);
    setTimeout(() => toast.remove(), 3500);
}

// ── Init ───────────────────────────────────────────────
carregarTarefas();