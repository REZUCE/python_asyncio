## python_asyncio 
My comments in the code and thoughts on paragraphs book "Python Concurrency with asyncio"

## Требования
- Python 3.11 or more
- Installed [uv](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer)
- aiohttp

## install and start

### 1. Install uv
```bash
git clone https://github.com/your-repository/name-repository.git
cd name-repository
```

### 2. Install dependencies with use uv

#### If there is not project.toml:
```bash
uv init --app
```

#### installing dependencies:
```bash
uv venv venv
#uv add fastapi example
```
#### If there is project.toml:
```bash
uv sync
```

### 3. Activating the virtual environment

#### macOS/Linux:
```bash
source venv/bin/activate
```
