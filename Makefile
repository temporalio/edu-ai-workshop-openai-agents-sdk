.PHONY: setup env lint test temporal-up temporal-down clean pre-commit-install pre-commit-run

setup:
	@echo "Installing dependencies..."
	pip install -e ".[dev]"
	@echo "Setup complete!"

pre-commit-install:
	@echo "Installing pre-commit hooks..."
	pre-commit install
	@echo "Pre-commit hooks installed!"

pre-commit-run:
	@echo "Running pre-commit hooks on all files..."
	pre-commit run --all-files

env:
	@python scripts/check_env.py

lint:
	@echo "Running ruff..."
	ruff check .
	@echo "Running mypy..."
	mypy exercises/ solutions/ scripts/

test:
	@echo "Running tests..."
	pytest -v

temporal-up:
	@bash scripts/run_temporal.sh

temporal-down:
	@echo "Stopping Temporal server..."
	@pkill -f "temporal server start-dev" || echo "Temporal not running"

# Note: Exercises 1-3 are Jupyter notebooks (.ipynb files)
# Exercise 4 uses separate Python files (production pattern)
# Open them in VS Code or Jupyter Lab:
#   exercises/01_agent_hello_world/exercise.ipynb
#   exercises/02_temporal_hello_world/exercise.ipynb
#   exercises/03_durable_agent/exercise.ipynb
#   exercises/04_agent_routing/  (Python files: workflow.py, worker.py, starter.py)

clean:
	@echo "Cleaning up..."
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	@echo "Clean complete!"
