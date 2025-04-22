
# 🥪 Snack API

API RESTful desenvolvida com Flask para gerenciamento de refeições (snacks), utilizando banco de dados MySQL e SQLAlchemy com variáveis de ambiente separadas.

## 🚀 Funcionalidades

- Criar nova refeição
- Buscar refeição por ID
- Listar todas as refeições
- Atualizar dados de uma refeição
- Deletar uma refeição

---

## 🧱 Tecnologias utilizadas

- Python 3.10+
- Flask
- Flask SQLAlchemy
- MySQL
- python-dotenv
- pymysql

---

## ⚙️ Instalação e uso

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Crie e ative o ambiente virtual (opcional)

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

Crie um arquivo chamado `credentials.env.app` com o seguinte conteúdo:

```
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=3306
DB_NAME=nome_do_banco
SECRET_KEY=sua_chave_secreta
```

### 5. Execute a aplicação

```bash
python app.py
```

A aplicação será executada em `http://127.0.0.1:5000`.

---

## 📦 Endpoints da API

### 🔸 Criar uma refeição

`POST /snack`

```json
{
  "name": "Café da manhã",
  "description": "Ovos e café",
  "time": "08:00:00",
  "date": "2025-04-21",
  "included": true
}
```

---

### 🔹 Buscar refeição por ID

`GET /snack/<id>`

---

### 🔹 Listar todas as refeições

`GET /snack/search/all`

---

### 🔸 Atualizar uma refeição

`PUT /snack/<id>`

```json
{
  "name": "Almoço",
  "description": "Arroz, feijão e salada",
  "time": "12:30:00",
  "date": "2025-04-21",
  "included": true
}
```

---

### 🔻 Deletar uma refeição

`DELETE /snack/delete/<id>`

---

## 🔐 Segurança

Este projeto utiliza variáveis de ambiente para proteger dados sensíveis como credenciais de banco de dados e chave secreta.

Certifique-se de **NÃO versionar** arquivos como `credentials.env.app` ou `.env.docker`:

Exemplo de `.gitignore`:

```
.env.*
credentials.env.*
```

---

## 📌 Observações

- As datas devem estar no formato `YYYY-MM-DD`.
- Horários devem estar no formato `HH:MM:SS`.

---

## 🧑‍💻 Autor

Feito por [Guilherme Jorge Hauck](https://github.com/Guihauck)
