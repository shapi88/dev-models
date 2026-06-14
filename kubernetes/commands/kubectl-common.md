# Kubernetes kubectl Common Commands (model references)

```bash
# Get overview
kubectl get pods,svc,deploy -A

# Describe a resource (most useful command for debugging)
kubectl describe pod <pod-name>

# View logs of a container
kubectl logs -f deploy/my-web -c app

# Exec into a pod
kubectl exec -it deploy/my-web -- /bin/sh

# Port-forward for local testing
kubectl port-forward svc/my-web 8080:80
```

See individual model READMEs for full manifest patterns.