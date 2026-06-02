# LetsMakeIt

A modular full-stack portal i'm building to figure out how to use FastAPI and SQLAlchemy. The goal is to have a solid "hub" with different apps without the code turning into spaghetti. yummi

## What's in here?
- **Synapse**: a comment wall thingy. 
- **Tasker**: task manager so i don't forget to do groceries.

## The Stack
- **Backend**: FastAPI + SQLAlchemy. spent a lot of time on the `crud/` and `schemas/` split to keep things tidy. backend pain.
- **Frontend**: Vanilla JS and Tailwind. No idea how ts works. This whole thing is an ai slop. Also fuck frontend "devs"
- **Infrastructure**: Docker and Nginx. This was a kick in the nut to set up but it's worth it.

## How to run it
with docker:
```bash
docker-compose up --build
```
otherwise, `uv sync` and `python app/main.py` works too.

## Lessons Learned
- **Circular Imports**: ran into a wall with user/comment relationships. fixed it using `TYPE_CHECKING` and forward refs in pydantic.
- **Project Structure**: was a real pain to figure out.
