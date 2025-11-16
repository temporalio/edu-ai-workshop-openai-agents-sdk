#!/bin/bash
set -e

echo "Bootstrapping Temporal AI Agents Workshop..."

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -e ".[dev]" --quiet

# Install Temporal CLI
echo "Installing Temporal CLI..."
if ! command -v temporal &> /dev/null; then
    curl -sSf https://temporal.download/cli.sh | sh
    # Add to PATH for current session
    export PATH="$HOME/.temporalio/bin:$PATH"
    echo 'export PATH="$HOME/.temporalio/bin:$PATH"' >> ~/.bashrc
else
    echo "Temporal CLI already installed"
fi

# Copy .env.sample to .env if it doesn't exist
if [ ! -f .env ]; then
    echo "Creating .env file from template..."
    cp .env.sample .env
    echo "WARNING: Please add your OPENAI_API_KEY to .env file"
fi

# Verify environment
echo "Checking environment..."
python scripts/check_env.py || echo "WARNING: Environment check failed - see above for details"

echo ""
echo "Bootstrap complete!"
echo ""
echo "Next steps:"
echo "  1. Add your OPENAI_API_KEY to .env file"
echo "  2. Run 'make temporal-up' to start Temporal server"
echo "  3. Run 'make exercise-1' to start the workshop"
