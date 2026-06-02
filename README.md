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
I made a `run.sh` script because I'm lazy and can't be bothered to type long docker commands.

```bash
./run.sh up      # starts everything
./run.sh logs    # shows the backend screaming
./run.sh down    # kills it
```
Otherwise, standard `uv sync` and `python app/main.py` works too.

## Lessons Learned
- **Circular Imports**: ran into a wall with user/comment relationships. fixed it using `TYPE_CHECKING` and forward refs in pydantic.
- **Project Structure**: was a real pain to figure out.
