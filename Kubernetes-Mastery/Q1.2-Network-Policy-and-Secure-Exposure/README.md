Q 1.2 Network Policy & Secure Exposure

 Task: Create Kubernetes manifests for:
    o A deployment (frontend-app) exposed via an Ingress.
    o A NetworkPolicy that allows access only from pods in the backend namespace with label access: true.

 Focus: Service exposure (Ingress), Ingress class annotations, fine-grained NetworkPolicy rules.

-----------

Solution:

1. Deployment: frontend-app running in the default namespace

2. Service: Exposes the frontend-app internally

3. Ingress: Exposes the service externally with class annotation

4. NetworkPolicy: Allows traffic to the frontend only from:

    - Pods in the backend namespace
    - Labeled with access: "true"