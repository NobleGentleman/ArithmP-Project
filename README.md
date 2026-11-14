# ArithmP - Simple Arithmetic Expression Parser

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
