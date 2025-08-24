# FastAPI Todo API (JWT Auth + SQLite)

A production-ready starter demonstrating:
- FastAPI with Pydantic v2
- JWT auth (password flow) with `python-jose`
- Password hashing with `passlib[bcrypt]`
- SQLAlchemy 2.0 + SQLite
- Dependency injection and routers
- Tests with `pytest` + `TestClient`
- CORS & settings via `.env`

## Quickstart

### 1) Create a virtual environment & install
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 2) Configure environment
Copy `.env.example` to `.env` and tweak values if you like.

### 3) Run the API
```bash
uvicorn app.main:app --reload
```
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

### 4) Try it
1. Register:
```bash
curl -X POST http://127.0.0.1:8000/auth/register -H "Content-Type: application/json" -d '{"username":"alice","password":"secret"}'
```
2. Get token:
```bash
curl -X POST http://127.0.0.1:8000/auth/token -H "Content-Type: application/x-www-form-urlencoded" -d "username=alice&password=secret"
```
Copy the `access_token`.

3. Create a todo:
```bash
curl -X POST http://127.0.0.1:8000/todos -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d '{"title":"Buy milk","completed":false}'
```

4. List your todos:
```bash
curl -H "Authorization: Bearer <TOKEN>" http://127.0.0.1:8000/todos
```

### 5) Run tests
```bash
pytest -q
```

---

## Project layout
```
fastapi-todo-jwt/
├─ app/
│  ├─ __init__.py
│  ├─ main.py
│  ├─ database.py
│  ├─ models.py
│  ├─ schemas.py
│  ├─ auth.py
│  ├─ deps.py
│  └─ routers/
│     ├─ auth.py
│     └─ todos.py
├─ tests/
│  └─ test_main.py
├─ .env.example
├─ requirements.txt
└─ README.md
```

### Notes
- Uses SQLite by default; switch to Postgres by changing `DATABASE_URL` in `.env`.
- Passwords are hashed (bcrypt). Never store plaintext passwords.
- JWT is short-lived by default (30 minutes). Tune in `.env`.
