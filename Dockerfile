FROM python:3.14-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1
# Copy from the cache instead of linking since it's a container
ENV UV_LINK_MODE=copy

# Install dependencies
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-install-project

# Copy the application
COPY . .

# Ensure data directory exists
RUN mkdir -p /app/data

# Expose the port
EXPOSE 8000

# Run the application using python module syntax
CMD ["uv", "run", "python", "-m", "app.main"]
