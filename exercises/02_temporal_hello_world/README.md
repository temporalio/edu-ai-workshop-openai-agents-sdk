# Exercise 2: Temporal Hello World

**Goal:** Create a basic Temporal workflow with activities to understand durability and retries.

**Timebox:** 15 minutes

## What You'll Learn

- How to define Temporal workflows and activities
- How to run a workflow and observe execution in the Temporal UI
- How activities provide automatic retries and durability

## Prerequisites

Make sure Temporal server is running:

```bash
make temporal-up
```

## Steps

1. **Define an activity** - Create a simple activity function that performs a task
2. **Define a workflow** - Create a workflow that calls the activity
3. **Start a worker** - Run the Temporal worker to execute workflows
4. **Execute the workflow** - Trigger the workflow and observe results
5. **Check Temporal UI** - View execution history at http://localhost:8233

## Expected Output

```
🚀 Starting Temporal Hello World workflow...

Activity: Processing data...
Activity: Data processed successfully!

✅ Workflow completed: Hello from Temporal!

View in Temporal UI: http://localhost:8233
```

## Running the Exercise

```bash
make temporal-up    # Start Temporal server
make exercise-2     # Run the exercise
```

Or directly:

```bash
python exercises/02_temporal_hello_world/main.py
```

## Stretch Goal

- Add retry logic to the activity with explicit retry policy
- Simulate a failure and watch automatic retries in Temporal UI
- Add a second activity and call them sequentially

## Need Help?

Check the solution in `solutions/02_temporal_hello_world/`
