Task: Write a Bash script that:
	- Lists all pods across namespaces in CrashLoopBackOff state.
	- Prints: pod name, namespace, image, and last 10 lines of logs.
Focus: Shell scripting, kubectl, filtering output, loop and formatting.

---------

Requirements

    - kubectl
    - jq

    Install jq if missing:
        - sudo apt install jq