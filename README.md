 # DevOps Pipeline - Production-Ready Infrastructure

  A complete end-to-end DevOps pipeline demonstrating modern cloud-native practices with CI/CD, GitOps, encrypted secrets    
   management, and automated deployments.

  ## 🏗️ Architecture

  ┌─────────────────────────────────────────────────────────────────┐
  │                        Developer Workflow                        │
  └─────────────────────────────────────────────────────────────────┘
                                ↓
                      Git Push (GitHub)
                                ↓
  ┌─────────────────────────────────────────────────────────────────┐
  │                    GitHub Actions (CI/CD)                        │
  │  • Build Docker image                                           │
  │  • Tag with commit SHA                                          │
  │  • Push to Docker Hub                                           │
  │  • Update Helm chart values                                     │
  └─────────────────────────────────────────────────────────────────┘
                                ↓
  ┌─────────────────────────────────────────────────────────────────┐
  │                   ArgoCD (GitOps Engine)                        │
  │  • Monitors Git repository                                      │
  │  • Detects configuration changes                                │
  │  • Syncs to Kubernetes cluster                                  │
  └─────────────────────────────────────────────────────────────────┘
                                ↓
  ┌─────────────────────────────────────────────────────────────────┐
  │                    Kubernetes Cluster                           │
  │                                                                  │
  │  ┌──────────────────┐  ┌──────────────────┐                   │
  │  │ Sealed Secrets   │  │ NGINX Ingress    │                   │
  │  │ Controller       │  │ Controller       │                   │
  │  │ • Decrypts       │  │ • Routes traffic │                   │
  │  │   secrets        │  │ • Load balancing │                   │
  │  └──────────────────┘  └──────────────────┘                   │
  │                                                                  │
  │  ┌──────────────────────────────────────────────────────────┐  │
  │  │             Application Pods (v6.0)                      │  │
  │  │  • Consumes decrypted secrets                           │  │
  │  │  • Health checks                                         │  │
  │  │  • Auto-scaling ready                                    │  │
  │  └──────────────────────────────────────────────────────────┘  │
  └─────────────────────────────────────────────────────────────────┘
                                ↓
                      http://dev.local:8082
                           (End Users)

  ## 🛠️ Tech Stack

  | Component | Technology | Purpose |
  |-----------|-----------|---------|
  | **CI/CD** | GitHub Actions | Automated build & deployment |
  | **GitOps** | ArgoCD | Declarative continuous delivery |
  | **Container Registry** | Docker Hub | Image storage |
  | **Orchestration** | Kubernetes (k3d) | Container management |
  | **Package Manager** | Helm | Application configuration |
  | **Secrets** | Sealed Secrets | Encrypted secrets in Git |
  | **Ingress** | NGINX Ingress | Traffic routing & load balancing |
  | **Monitoring** | Prometheus & Grafana | Metrics & visualization |

  ## ✨ Features

  ✅ **Full GitOps Workflow** - Single source of truth in Git
  ✅ **Automated CI/CD** - Zero manual deployment steps
  ✅ **Encrypted Secrets** - Safe storage in version control
  ✅ **Infrastructure as Code** - Reproducible environments
  ✅ **Production-Ready** - Health checks, monitoring, rollbacks
  ✅ **Clean URLs** - Ingress routing with domain names

  ## 🚀 How It Works

  ### Deployment Flow

  1. **Developer pushes code** to GitHub
  2. **GitHub Actions** automatically:
     - Builds Docker image
     - Tags with Git commit SHA (immutable versioning)
     - Pushes to Docker Hub
     - Updates Helm chart values.yaml
     - Commits chart update to Git
  3. **ArgoCD** detects Git change and:
     - Syncs desired state to cluster
     - Deploys updated application
     - Decrypts sealed secrets
  4. **Sealed Secrets Controller**:
     - Decrypts encrypted secrets
     - Creates Kubernetes secrets
     - Injects into pods
  5. **Ingress Controller**:
     - Routes external traffic
     - Load balances requests
     - Provides clean URL access

  ### Security

  - **Secrets encrypted** with Sealed Secrets (RSA public key cryptography)
  - **No plaintext secrets** in Git repository
  - **Automated decryption** in cluster only
  - **Full audit trail** via Git history
  - **RBAC** for least privilege access

  ## 📊 Monitoring & Observability

  - **Prometheus** - Metrics collection
  - **Grafana** - Visualization dashboards
  - **ArgoCD UI** - Deployment status
  - **Kubernetes logs** - Application debugging
  - **Health endpoints** - Liveness & readiness probes

  ## 🎯 Key Achievements

  - ✅ **Zero-downtime deployments** with rolling updates
  - ✅ **Automatic rollback** on deployment failures
  - ✅ **Encrypted secrets** in version control (GitOps-compliant)
  - ✅ **Immutable versioning** with Git commit SHAs
  - ✅ **Complete automation** from code to production
  - ✅ **Production-ready** infrastructure patterns

  ## 📝 Quick Start

  ```bash
  # Make code change
  nano app.py

  # Commit and push
  git add app.py
  git commit -m "Update feature"
  git push

  # Watch automation:
  # 1. GitHub Actions: https://github.com/sebrcg/customer-docker-app/actions
  # 2. ArgoCD: http://localhost:8080
  # 3. Live app: http://dev.local:8082

  🏆 Interview Highlights

  "I built a production-ready DevOps pipeline implementing GitOps principles with ArgoCD for continuous delivery, GitHub     
  Actions for CI/CD, Sealed Secrets for encrypted configuration management, and NGINX Ingress for traffic routing. The       
  entire workflow is automated - a single Git push triggers the pipeline that builds, tests, and deploys to Kubernetes       
  with zero manual intervention."

  📚 Skills Demonstrated

  - CI/CD pipeline design and implementation
  - GitOps methodology with ArgoCD
  - Kubernetes orchestration and management
  - Docker containerization
  - Helm chart development
  - Secrets management (Sealed Secrets)
  - Infrastructure as Code
  - Ingress configuration and traffic routing
  - Monitoring and observability
  - Git workflow and version control
  - Debugging and troubleshooting

