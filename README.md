# FastAPI Tutorial

This is a tutorial follow-along from Corey Schafer.

## Requirements

- [uv](https://docs.astral.sh/uv/getting-started/installation/), which manages Python, the virtual environment and dependencies.

You don't need to install Python separately. uv reads the version from `.python-version` (3.14) and downloads it if it isn't already on your machine.

## Installation

```bash
git clone <repo-url>
cd myapp
uv sync
```

`uv sync` creates a `.venv` folder and installs the exact dependency versions recorded in `uv.lock`, including dev tools. You don't need to activate the virtual environment, because `uv run` uses it automatically.

## Running the app

Start the development server, which reloads automatically when you change code:

```bash
uv run poe dev
```

Then open <http://127.0.0.1:8000>.

| Command | What it does |
| --- | --- |
| `uv run poe dev` | Development server with auto-reload (`fastapi dev`) |
| `uv run poe start` | Production-style server without reload (`fastapi run`) |
| `uv run poe` | Lists all available tasks |

Tasks are defined under `[tool.poe.tasks]` in `pyproject.toml` and run with [Poe the Poet](https://poethepoet.natn.io/).

Run commands from the project root. Templates are loaded from `templates/` relative to the folder you start the server in.

## Routes

| Route | Description |
| --- | --- |
| `/`, `/posts` | HTML home page |
| `/api/posts` | Posts as JSON |
| `/docs` | Interactive API docs (Swagger UI) |

## Project structure

```text
myapp/
├── main.py            # FastAPI app and routes
├── templates/         # Jinja2 HTML templates
├── pyproject.toml     # Dependencies and Poe tasks
├── uv.lock            # Locked dependency versions (commit this)
└── .python-version    # Python version used by uv
```

The project uses a flat layout: a runnable app rather than an installable package, so it has no `src/` folder or build system. For more on this choice:

- [uv: Creating projects](https://docs.astral.sh/uv/concepts/projects/init/): the difference between `uv init --app` (flat) and `--package`/`--lib` (src layout)
- [Python Packaging Guide: src layout vs flat layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/)
- [FastAPI CLI](https://fastapi.tiangolo.com/fastapi-cli/): how `fastapi dev` finds the app
- [FastAPI: Bigger Applications](https://fastapi.tiangolo.com/tutorial/bigger-applications/): splitting the app into a package with routers as it grows
# FastAPI-Tutorial
