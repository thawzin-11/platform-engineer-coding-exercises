Task: You receive a complaint: A task in our DAG is randomly skipped even though the previous task succeeded.
    Explain:
    - What could cause this?
    - Which DAG/task properties would you inspect?
    - How would you fix this to ensure all dependent tasks run reliably?
Focus: DAG dependencies, skipped states, trigger_rule, retry behavior.

----------

Requirements:

    Install dependencies:

    - pip install pyyaml


Summary:

    - Validates multiple documents per YAML file
    - Catches parse errors gracefully
    - Logs per-document issues with file and index context
    - JSON output is machine-parsable for CI pipelines