# Kubernetes Stateless Web Service — Model v1.0.0

A minimal, production-leaning set of manifests for a stateless web workload.

## Files in this model version
- deployment.yaml
- service.yaml
- (optional) ingress.yaml or horizontalpodautoscaler.yaml in later versions

## How to use
```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

Review the individual files. They are intentionally small and commented so you understand every field.

**Compatibility:** Written for Kubernetes 1.28+ (adjust apiVersion if targeting older clusters).

Update the image name and add your real config (env, resources, probes, etc.).