#!/bin/bash

echo "Checking for pods in CrashLoopBackOff state..."

# Get all pods with status CrashLoopBackOff
kubectl get pods --all-namespaces -o json |
jq -r '
  .items[]
  | . as $pod
  | $pod.status.containerStatuses[]
    | select(.state.waiting.reason == "CrashLoopBackOff")
    | "\($pod.metadata.name)|\($pod.metadata.namespace)|\(.image)"
' | while IFS="|" read -r pod_name namespace image; do
    echo "----------------------------------------------------"
    echo "Pod:        $pod_name"
    echo "Namespace:  $namespace"
    echo "Image:      $image"
    echo "Logs (last 10 lines):"
    echo "----------------------------------------------------"
    kubectl logs -n "$namespace" "$pod_name" --tail=10 2>&1 || echo "Failed to fetch logs"
    echo
done
