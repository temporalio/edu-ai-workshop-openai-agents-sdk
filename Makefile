.PHONY: setup env lint test temporal-up temporal-down clean

setup:
	@echo "Installing dependencies..."
	pip install -e ".[dev]"
	@echo "Setup complete!"

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

# Note: All exercises are Jupyter notebooks (.ipynb files)
# Open them in VS Code or Jupyter Lab:
#   exercises/01_agent_hello_world/exercise.ipynb
#   exercises/02_temporal_hello_world/exercise.ipynb
#   exercises/03_durable_agent/exercise.ipynb
#   exercises/04_multi_agent_handoff/exercise.ipynb

clean:
	@echo "Cleaning up..."
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	@echo "Clean complete!"
