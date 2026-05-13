# 🚀 TaskControl – Sistema Fullstack de Gestão de Tarefas

## 📌 Sobre o Projeto

O **TaskControl** é um sistema fullstack de gerenciamento de tarefas desenvolvido com foco em organização, produtividade e evolução técnica.

A aplicação permite criar, listar, concluir e remover tarefas através de uma interface web moderna integrada a uma API REST construída em Python.

O projeto começou utilizando persistência em JSON para fins de aprendizado e posteriormente evoluiu para uma arquitetura mais profissional utilizando:

- API REST com Flask
- Banco de dados MySQL
- Front-end integrado com JavaScript
- Comunicação via HTTP
- Organização em camadas

---

## 🎯 Objetivo

Desenvolver uma aplicação prática para gerenciamento de tarefas aplicando conceitos reais de desenvolvimento backend e frontend, incluindo:

- Arquitetura organizada
- Consumo de APIs
- Persistência em banco de dados
- Integração Fullstack
- Estrutura escalável

---

# 🖥️ Preview da Interface

> Interface moderna desenvolvida para proporcionar uma experiência limpa e intuitiva.

- Cadastro de tarefas
- Filtros por status
- Conclusão de tarefas
- Remoção de tarefas
- Atualização dinâmica da interface

---

# ⚙️ Funcionalidades

## ✅ Backend

- API REST com Flask
- Integração com MySQL
- CRUD de tarefas
- Rotas HTTP
- Persistência de dados
- Organização em camadas

## ✅ Frontend

- Interface moderna responsiva
- Integração com API via Fetch API
- Renderização dinâmica de tarefas
- Filtros por status
- Atualização em tempo real

---

# 🌐 Rotas da API

| Método | Rota | Função |
|---|---|---|
| GET | `/tarefas` | Listar tarefas |
| POST | `/tarefas` | Criar tarefa |
| PUT | `/tarefas/<id>` | Concluir tarefa |
| DELETE | `/tarefas/<id>` | Remover tarefa |

---

# 🧱 Estrutura do Projeto

```bash
TaskControl/
│
├── app.py                 # API Flask
├── main.py                # Execução local
├── .gitignore
│
├── database/
│   └── connection.py      # Conexão MySQL
│
├── models/
│   └── tarefa.py          # Modelo da tarefa
│
├── services/
│   └── sistema.py         # Regras de negócio
│
├── interface/
│   ├── index.html
│   ├── style.css
│   └── script.js
```

---

# 🛠️ Tecnologias Utilizadas

## Backend
- Python
- Flask
- MySQL
- MySQL Connector

## Frontend
- HTML5
- CSS3
- JavaScript

## Ferramentas
- Git
- GitHub
- Postman
- VS Code
- PyCharm

---

# 🔄 Como Executar o Projeto

## 1️⃣ Clone o repositório

```bash
git clone https://github.com/c2rnan/TaskControl.git
```

---

## 2️⃣ Acesse a pasta do projeto

```bash
cd TaskControl
```

---

## 3️⃣ Instale as dependências

```bash
pip install flask
pip install mysql-connector-python
pip install python-dotenv
```

---

## 4️⃣ Configure o arquivo `.env`

Crie um arquivo `.env` na raiz:

```env
DB_HOST=127.0.0.1
DB_PORT=3306
DB_USER=root
DB_PASSWORD=
DB_NAME=taskcontrol
```

---

## 5️⃣ Execute a API

```bash
python app.py
```

---

## 6️⃣ Abra o Frontend

Abra:

```bash
interface/index.html
```

---

# 🧪 Testes da API

A API pode ser testada utilizando:

- Postman
- Insomnia
- Navegador (rotas GET)

---

# 🚀 Roadmap (Próximas melhorias)

- [ ] Editar tarefas
- [ ] Sistema de categorias/tags
- [ ] Busca por título
- [ ] Data de vencimento
- [ ] Tarefas vencidas destacadas
- [ ] Autenticação de usuários
- [ ] Deploy da API
- [ ] Deploy do frontend
- [ ] Dockerização
- [ ] Responsividade avançada

---

# 📈 Evolução do Projeto

O TaskControl foi desenvolvido como parte do meu processo de evolução prática em desenvolvimento de software, aplicando conceitos reais de:

- Backend
- APIs REST
- Banco de dados
- Frontend
- Integração Fullstack
- Versionamento com Git

O projeto continua em constante evolução com novas funcionalidades e melhorias estruturais.

---

# 👨‍💻 Autor

Desenvolvido por **Caio Renan**

- GitHub: https://github.com/c2rnan

---

# 📌 Observação

Este projeto está em desenvolvimento contínuo e pode sofrer alterações frequentes na arquitetura, interface e funcionalidades.
