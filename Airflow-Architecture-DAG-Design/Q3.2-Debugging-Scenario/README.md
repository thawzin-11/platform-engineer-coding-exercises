Task: You receive a complaint: A task in our DAG is randomly skipped even though the previous task succeeded.
 Explain:
    What could cause this?
    Which DAG/task properties would you inspect?
    How would you fix this to ensure all dependent tasks run reliably?
Focus: DAG dependencies, skipped states, trigger_rule, retry behavior.


Solution:

1. What Could Cause a Task to be Skipped?

    ## The most common causes include, but here's for sample one.

    Cause:
    - trigger_rule not satisfied

    Explanation:
    - By default, a task runs only if all upstream tasks succeed. If even one is skipped/failed and trigger_rule isn't adjusted, the downstream task is 
      skipped.


2. Which DAG/Task Properties to Inspect

    trigger_rule: If it’s left as default (all_success), any skipped or failed upstream task will prevent execution.
    depends_on_past: If True, a task won’t run unless its previous run succeeded.
    wait_for_downstream: Can block task progression until downstream tasks of prior runs finish.
    execution_timeout or system-level retries: If timeouts occur silently, tasks may be retried and skip downstream logic.


3. How to Fix it

    A. Set the Correct trigger_rule
        - If a task has multiple upstreams or may follow a branch, explicitly set trigger_rule:

    B. Review DAG Logic
        - Avoid depends_on_past=True unless strictly required.

-----

Summary:

- To ensure reliable downstream task execution:

    - Inspect trigger rules and explicitly set them when needed.
    - Avoid relying on defaults if your DAG uses branches or complex dependencies.
    - Use the UI’s Task Instance Details to trace exact causes of skipped tasks.
