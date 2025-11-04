# DevOps Pipeline - Quick Reference

  ## 🚀 Common Workflows

  ### Deploy New Version
  ```bash
  # 1. Make code changes
  nano app.py

  # 2. Commit and push
  git add .
  git commit -m "Add new feature"
  git push

  # 3. Watch it deploy automatically!
  # - GitHub Actions: https://github.com/sebrcg/customer-docker-app/actions
  # - ArgoCD: http://localhost:8080
  # - Live: http://dev.local:8082

  Create Encrypted Secret

  # One-line secret creation
  kubectl create secret generic SECRET_NAME \
    --from-literal=KEY=VALUE \
    --namespace=NAMESPACE \
    --dry-run=client -o yaml | kubeseal --format=yaml > sealed-secret.yaml

  # Commit to Git (safe!)
  git add sealed-secret.yaml
  git commit -m "Add encrypted secret"
  git push

  Rollback Deployment

  # Via ArgoCD UI
  argocd app rollback APP_NAME REVISION

  # Via Git
  git revert HEAD
  git push

  🔧 Essential Commands

  Cluster Management

  # Check cluster status
  kubectl get nodes
  kubectl get pods -A

  # Check specific namespace
  kubectl get pods -n dev
  kubectl get svc -n dev
  kubectl get ingress -n dev

  ArgoCD

  # Port-forward to UI
  kubectl port-forward svc/argocd-server -n argocd 8080:443 &

  # Get admin password
  kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d && echo

  # CLI commands
  argocd app list
  argocd app get APP_NAME
  argocd app sync APP_NAME
  argocd app history APP_NAME

  Debugging

  # Check pod logs
  kubectl logs -n NAMESPACE POD_NAME
  kubectl logs -n NAMESPACE deployment/DEPLOYMENT_NAME --tail=50

  # Describe resources
  kubectl describe pod POD_NAME -n NAMESPACE
  kubectl describe ingress INGRESS_NAME -n NAMESPACE

  # Get events
  kubectl get events -n NAMESPACE --sort-by='.lastTimestamp'

  # Check pod status
  kubectl get pods -n NAMESPACE -w

  Secrets

  # List secrets
  kubectl get secrets -n NAMESPACE

  # Decode secret
  kubectl get secret SECRET_NAME -n NAMESPACE -o jsonpath="{.data.KEY}" | base64 -d

  # List sealed secrets
  kubectl get sealedsecrets -n NAMESPACE

  Ingress

  # Port-forward Ingress controller
  kubectl port-forward -n ingress-nginx svc/ingress-nginx-controller 8082:80 &

  # List ingress resources
  kubectl get ingress -A

  # Check ingress logs
  kubectl logs -n ingress-nginx deployment/ingress-nginx-controller

  �� Monitoring

  Prometheus & Grafana

  # Port-forward Prometheus
  kubectl port-forward -n monitoring svc/prometheus-server 9090:80 &

  # Port-forward Grafana
  kubectl port-forward -n monitoring svc/grafana 3000:80 &

  # Access:
  # - Prometheus: http://localhost:9090
  # - Grafana: http://localhost:3000

  Health Checks

  # Check app health endpoint
  curl http://dev.local:8082/health

  # Check pod readiness
  kubectl get pods -n dev -o wide

  🔄 Git Workflows

  Handle Pipeline Conflicts

  # When CI/CD updated the repo
  git pull --rebase
  git push

  View History

  # Recent commits
  git log --oneline -10

  # Changes in specific file
  git log --oneline -- app.py

  # See what changed
  git diff HEAD~1

  🏗️ Architecture Quick View

  Code Push → GitHub Actions → Docker Hub
                  ↓
             Git Update
                  ↓
              ArgoCD
                  ↓
            Kubernetes
            /    |    \
     Secrets  Ingress  App
           \    |    /
                ↓
            End Users

  🎯 URLs Reference

  | Service        | URL                                                     | Credentials           |
  |----------------|---------------------------------------------------------|-----------------------|
  | App (dev)      | http://dev.local:8082                                   | None                  |
  | ArgoCD         | http://localhost:8080                                   | admin / (from secret) |
  | Prometheus     | http://localhost:9090                                   | None                  |
  | Grafana        | http://localhost:3000                                   | admin / prom-operator |
  | GitHub Actions | https://github.com/sebrcg/customer-docker-app/actions   | GitHub login          |
  | Docker Hub     | https://hub.docker.com/r/whalesnail/customer-docker-app | Docker login          |

  💡 Pro Tips

  - Background processes: Add & to run port-forwards in background
  - Watch mode: Use -w flag to watch resources update in real-time
  - Grep filters: Pipe to grep to filter output
  - Tail logs: Always use --tail=N to limit log output
  - Pull before push: Avoid conflicts with git pull --rebase

  🐛 Common Issues

  Issue: Port already in useFix: pkill -f "port-forward" or use different port

  Issue: Git push rejectedFix: git pull --rebase && git push

  Issue: Pod CrashLoopBackOffFix: kubectl logs POD_NAME to see error

  Issue: Ingress 503 errorFix: Check service endpoints with kubectl describe svc

  Issue: Secret not foundFix: Verify sealed secret with kubectl get sealedsecrets
