.PHONY: setup env lint test temporal-up temporal-down exercise-1 exercise-2 exercise-3 exercise-4 clean

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

exercise-1:
	@python exercises/01_agent_hello_world/main.py

exercise-2:
	@python exercises/02_temporal_hello_world/main.py

exercise-3:
	@python exercises/03_durable_agent/main.py

exercise-4:
	@python exercises/04_multi_agent_handoff/main.py

clean:
	@echo "Cleaning up..."
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	@echo "Clean complete!"
