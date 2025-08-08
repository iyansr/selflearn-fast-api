#!/bin/bash

# Format and lint Python code using Ruff

echo "🔍 Running Ruff linter..."
ruff check --fix .

echo "🎨 Running Ruff formatter..."
ruff format .

echo "✅ Code formatting and linting complete!" 