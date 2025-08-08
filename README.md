# FastAPI Project

A modern FastAPI project with automatic code formatting and linting using Ruff.

## Setup

1. Make sure you have Python 3.13+ installed
2. Install dependencies:
   ```bash
   uv sync
   ```

3. Activate the virtual environment:
   ```bash
   source .venv/bin/activate  # On macOS/Linux
   # or
   .venv\Scripts\activate     # On Windows
   ```

## Development

### Code Formatting and Linting

This project uses [Ruff](https://github.com/astral-sh/ruff) for both linting and formatting, which provides:
- **Import sorting** (replaces isort)
- **Code formatting** (replaces Black)
- **Linting** (replaces Flake8, pylint, etc.)
- **Extremely fast** performance

#### Quick Commands

```bash
# Format and lint all code (recommended)
./scripts/format.sh

# Or run commands individually:

# Check for linting issues and fix them
ruff check --fix .

# Format code
ruff format .

# Check only (no fixes)
ruff check .

# Check specific file
ruff check src/features/todo/service.py

# Show what would be fixed without applying
ruff check --diff .
```

#### Import Sorting

Ruff automatically organizes your imports into sections:
1. **Future imports** (`from __future__ import ...`)
2. **Standard library** (`import os`, `from pathlib import Path`)
3. **Third-party** (`from fastapi import FastAPI`)
4. **First-party** (`from src.features import ...`)
5. **Local folder** (`from . import ...`)

#### Editor Integration (Format on Save)

For the best development experience, configure your editor to run Ruff on save:

##### **VS Code** (Recommended)

1. Install the [Ruff extension](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff)
2. The project includes `.vscode/settings.json` with optimal settings
3. VS Code will automatically:
   - Format code on save
   - Fix linting issues on save
   - Organize imports on save

##### **PyCharm/IntelliJ**

1. Install the Ruff plugin from the marketplace
2. Go to **Settings** → **Tools** → **External Tools**
3. Add a new tool:
   - **Name**: Ruff Format
   - **Program**: `ruff`
   - **Arguments**: `format $FilePath$`
   - **Working Directory**: `$ProjectFileDir$`
4. Set up a macro to run on save or use keyboard shortcut

##### **Neovim**

Using `nvim-lspconfig`:
```lua
require('lspconfig').ruff.setup({
  init_options = {
    settings = {
      configuration = "./pyproject.toml"
    }
  }
})
```

Using `conform.nvim` for formatting:
```lua
require("conform").setup({
    formatters_by_ft = {
        python = {
          "ruff_fix",      -- Fix linting issues
          "ruff_format",   -- Format code
          "ruff_organize_imports", -- Organize imports
        },
    },
})
```

##### **Vim**

Add to your `.vimrc`:
```vim
" Format on save
autocmd BufWritePre *.py execute ':!ruff format ' . shellescape(@%)
autocmd BufWritePre *.py execute ':!ruff check --fix ' . shellescape(@%)
```

##### **Zed**

Add to your Zed settings:
```json
{
  "languages": {
    "Python": {
      "language_servers": ["ruff"],
      "format_on_save": "on",
      "formatter": [
        {
          "code_actions": {
            "source.organizeImports.ruff": true,
            "source.fixAll.ruff": true
          }
        },
        {
          "language_server": {
            "name": "ruff"
          }
        }
      ]
    }
  }
}
```

##### **Emacs**

Using `ruff-format` package:
```elisp
(require 'ruff-format)
(add-hook 'python-mode-hook 'ruff-format-on-save-mode)
```

##### **Sublime Text**

1. Install the LSP package and LSP-ruff
2. Add to your LSP settings:
```json
{
  "clients": {
    "ruff": {
      "enabled": true,
      "command": ["ruff", "server"],
      "selector": "source.python"
    }
  }
}
```

### Running the Application

```bash
# Development server
uvicorn src.app:app --reload

# Or using the server.py file
python server.py
```

## Project Structure

```
src/
├── app.py              # FastAPI application
├── database.py         # Database configuration
└── features/
    └── todo/
        ├── models.py   # SQLAlchemy models
        ├── schema.py   # Pydantic schemas
        └── service.py  # Business logic
```

## Configuration

### Ruff Configuration

Ruff is configured in `pyproject.toml` with:
- Line length: 88 characters (same as Black)
- Import sorting enabled
- Common Python linting rules
- FastAPI-specific rule adjustments

### Key Features

- ✅ Import sorting and organization
- ✅ Code formatting (Black-compatible)
- ✅ Linting with auto-fix
- ✅ Fast performance (written in Rust)
- ✅ All-in-one tool (replaces multiple tools)
- ✅ Format on save in all major editors
