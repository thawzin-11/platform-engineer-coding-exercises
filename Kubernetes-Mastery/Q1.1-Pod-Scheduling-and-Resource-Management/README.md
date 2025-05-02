1. Node affinity for env=prod and presence of GPU.

2. Resource requests = limits (2Gi memory, 1 CPU) as QoS = Guaranteed (requests = limits)

3. Uses priorityClassName and avoids overcommitting memory to reduce eviction risk.

4. Mounts a Kubernetes Secret named app-secrets.