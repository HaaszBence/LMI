# AGENTS.md

## Commands & Toolchain
- **Environment:** Managed by `uv`. Use `uv run` or `uv sync`.
- **Backend:** FastAPI (Python 3.14+). Run via `./run.sh up` (Docker) or `uv run python app/main.py` (local).
- **Frontend:** Vanilla JS + Tailwind. Served from `/static`.
- **Scripts:** 
  - `./run.sh up`: Build and start Docker services.
  - `./run.sh logs`: View Docker logs.
  - `./run.sh down`: Stop Docker services.

## Architecture
- **Structure:** Modular "hub" design. Apps are in `static/apps/`.
- **Backend Flow:** `app/main.py` -> `app/routes/` -> `app/crud/` -> `app/models/`.
- **Database:** PostgreSQL (v17). Database runs as a container service named `db`.
- **Table Creation:** `Base.metadata.create_all` is called directly in `app/main.py` on startup. No migrations tool (Alembic) detected.

## Patterns & Constraints
- **Circular Imports:** Use `TYPE_CHECKING` and forward references for SQLAlchemy/Pydantic relationships.
- **Schemas vs Models:** Strict split between `app/schemas/` (Pydantic) and `app/models/` (SQLAlchemy). 
- **Frontend:** DO NOT use TypeScript or heavy frameworks. Maintain Vanilla JS + Tailwind convention.
- **Static Assets:** The backend mounts `static/` at `/static` and provides explicit routes for app entry points (e.g., `/apps/synapse/`).

## Verification
- No automated test suite detected. 
- Verify changes by running the backend and checking the Swagger docs at `/docs` or the frontend at `/`.
