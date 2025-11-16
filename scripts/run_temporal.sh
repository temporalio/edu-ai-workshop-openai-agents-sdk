#!/bin/bash

# Check if Temporal is already running
if pgrep -f "temporal server start-dev" > /dev/null; then
    echo "Temporal server is already running"
    echo "  UI: http://localhost:8233"
    exit 0
fi

echo "Starting Temporal dev server..."
echo "  Server: localhost:7233"
echo "  UI: http://localhost:8233"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Start Temporal in the background
temporal server start-dev --db-filename ~/.temporal/default.db &
TEMPORAL_PID=$!

# Wait a bit for server to start
sleep 3

# Check if it started successfully
if ps -p $TEMPORAL_PID > /dev/null; then
    echo "SUCCESS: Temporal server started (PID: $TEMPORAL_PID)"
    echo "   Keep this terminal open or run in background"
    wait $TEMPORAL_PID
else
    echo "ERROR: Failed to start Temporal server"
    exit 1
fi
