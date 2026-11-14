# ArithmP - Simple Arithmetic Expression Parser

A small arithmetic language interpreter written in Python, with a command-line interface and an interactive mode. Parsing is done with [Lark](https://github.com/lark-parser/lark) and the CLI with [Click](https://click.palletsprojects.com/).

## Features

- Arithmetic expressions (`1 + 1`, `3 * 4`, ...)
- Evaluate an expression from the command line with `-c`
- Interactive interpreter
- Variable assignment (`a = 4`)
- Built-in function calls (`abs(-4)`, `round(2.7)`)
- Arrays (`arr = {1, 2, 3}`, `arr[0]`)

## Prerequisites

- Python **3.13 or higher** (uv downloads it automatically if your system Python is older)
- [uv](https://docs.astral.sh/uv/) (Python project manager), see the [installation guide](https://docs.astral.sh/uv/getting-started/installation/)
- Git
- Optional: [Docker](https://docs.docker.com/get-started/get-docker/) to run the app in a container

## Installation

```bash
git clone https://github.com/NobleGentleman/ArithmP-Project.git
cd ArithmP-Project
uv sync --locked
```

`uv sync` creates a virtual environment in `.venv` and installs the locked dependencies, including the development tools. Select this environment in your IDE for auto-completion and linting.

## Usage

All commands are run through `uv run`, which uses the project's virtual environment.

### Evaluate an expression

Parses the given expression and prints the result.

```bash
uv run arithmp -c "1 + 1"
```

Output:

```
2.0
```

### Interactive interpreter

Running `arithmp` without any argument starts an interactive interpreter: type an expression, press Enter, and the result is printed. Variables are kept from one line to the next. Errors are reported as `Error: ...` and the session continues. Type `exit` to quit.

```bash
uv run arithmp
```

```
>>> 1 + 1
2.0
>>> a = 4
4.0
>>> a * 2
8.0
>>> exit
```

### Show help

```bash
uv run arithmp --help
```

## Language reference

Expressions can be evaluated with `-c` or typed in the interactive interpreter. All numbers are floats.

### Arithmetic expressions

Addition (`+`), subtraction (`-`), multiplication (`*`), division (`/`), modulo (`%`), power (`^`), and unary `+` / `-`. Parentheses group operations.

```bash
uv run arithmp -c "(1 + 2) * 3"
uv run arithmp -c "2 ^ 3"
```

Output of the second command:

```
8.0
```

### Predefined constants

`pi` and `e` are predefined.

### Variable assignment

```
a = 4
a * 2
```

Using an undefined variable raises an error.

### Built-in function calls

Only built-in functions are available (no function definition, no `import`):

| Function | Description |
|----------|-------------|
| `abs(x)` | Absolute value |
| `round(x)` | Rounds to the nearest integer (halves go to the nearest even number) |
| `min(a, b, ...)` / `max(a, b, ...)` | Smallest / largest argument |
| `sqrt(x)` | Square root |
| `floor(x)` / `ceil(x)` | Rounds down / up |

```bash
uv run arithmp -c "abs(-4)"
uv run arithmp -c "round(2.7)"
```

### Arrays

Arrays use braces and are indexed from 0.

```
arr = {1, 2, 3}
arr[0]
```

## Development

### Tests

```bash
uv run pytest
```

### Linting, formatting and type checking

Code quality tools are installed in the `dev` dependency group and exposed as short tasks through [poethepoet](https://poethepoet.natn.io/). The tasks are defined in the `[tool.poe.tasks]` section of `pyproject.toml`.

| Command | Runs | Description |
|---------|------|-------------|
| `uv run poe lint` | `ruff check` | Lints the code: detects errors and bad practices (unused imports, likely bugs, unsorted imports). Does not modify any file. |
| `uv run poe format` | `ruff format` | Formats the code: **rewrites** the files to enforce a consistent style (spacing, quotes, line breaks). |
| `uv run poe format-check` | `ruff format --check` | Checks the formatting **without modifying** any file. Fails if some files would be reformatted. Used by the CI. |
| `uv run poe typecheck` | `ty check` | Type checks the code: detects inconsistent types (for example, passing a `str` where an `int` is expected). |

[ruff](https://docs.astral.sh/ruff/) handles linting and formatting (enabled rule sets: `E`, `F`, `I`, `B`), and [ty](https://docs.astral.sh/ty/) handles type checking.

Typical workflow before opening a Pull Request:

```bash
uv run poe format        # fix the formatting
uv run poe lint          # check for errors
uv run poe typecheck     # check the types
```

The CI runs the non-modifying checks (`lint`, `format-check`, `typecheck`) and fails if any of them reports a problem.

You can also run the tools directly, for example `uv run ruff check`: the tasks are only shortcuts.

### Development tools setup

The development tools were added to the `dev` dependency group with:

```bash
uv add --dev pytest
uv add --dev ruff ty poethepoet
```

If you clone the repository, you do not need to run these commands again: `uv sync --locked` already installs them.

### Adding a dependency

```bash
uv add <package>          # runtime dependency
uv add --dev <package>    # development dependency
```

## Continuous integration

GitHub Actions workflows are in `.github/workflows`:

| Workflow | Trigger | Purpose |
|----------|---------|---------|
| `tests.yml` | Every push and pull request | Installs the dependencies and runs the test suite (`uv run pytest`) on Python 3.13 |
| `lint.yml` | Every push and pull request | Runs `poe lint`, `poe format-check` and `poe typecheck`. Fails if any check reports a problem |
| `release.yml` | Push of a tag starting with `v` | Builds the package with `uv build` and publishes a GitHub release with the wheel and source archive attached, plus auto-generated release notes |

### Creating a release

Push a tag starting with `v` to trigger the release workflow:

```bash
git tag v0.2.0
git push origin v0.2.0
```

The release then appears in the **Releases** section of the GitHub repository, with the files from `dist/` attached.

## Docker

The application can be run in a Docker container, without installing Python or uv.

### Prerequisites

- [Docker](https://docs.docker.com/get-started/get-docker/) installed and running.
- On Linux, prefix `docker` commands with `sudo`, or add your user to the `docker` group.

### Build the image

From the project root:

```bash
docker build -t arithmp .
```

The image is based on `python:3.13-alpine`. Dependencies are installed with `uv` from `uv.lock`.

### Evaluate an expression

```bash
docker run --rm arithmp -c "1 + 1"
```

Output:

```
2.0
```

### Interactive mode

```bash
docker run --rm -it arithmp
```

The `-it` flag is required to get an interactive terminal.

### Show help

```bash
docker run --rm arithmp --help
```

### Useful options

| Option | Purpose |
|--------|---------|
| `-t arithmp` | Name given to the image |
| `--rm` | Removes the container once it exits |
| `-it` | Interactive mode with a terminal |

### Cleanup

```bash
docker rmi arithmp
```

## Project structure

```
.
├── .github/workflows/     # CI: tests, lint, release
├── src/arithmp/
│   ├── arithmp.lark       # Grammar of the language
│   ├── parser.py          # Parser and evaluator
│   └── __main__.py        # Command-line interface (Click)
├── tests/
│   ├── test_operators.py  # Arithmetic operators
│   ├── test_variables.py  # Variable assignment
│   ├── test_functions.py  # Built-in function calls
│   └── test_arrays.py     # Arrays
├── Dockerfile
├── pyproject.toml
└── uv.lock
```

## Contributing workflow

`main` is protected: every change goes through a Pull Request from a `dev/...` branch and is merged with a squash commit.
