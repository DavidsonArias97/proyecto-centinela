# 3. Pipeline CI/CD/CS (DevSecOps)

Se ha implementado un pipeline de Integración y Despliegue Continuo en **GitHub Actions** que integra controles de seguridad automatizados en cada fase, siguiendo el principio de **Shift-Left Security** (Seguridad desde el inicio).

### Herramientas de Seguridad Implementadas

| Herramienta | Fase | Función | Nivel de Bloqueo |
| :--- | :--- | :--- | :--- |
| **Gitleaks** | 🔍 Plan/Code | Escaneo de secretos en el historial de Git para prevenir fugas de credenciales (API Keys, Passwords). | 🔴 **Crítico**<br>*(Falla el pipeline si detecta algo)* |
| **Bandit** | 🐍 Code/Build | Análisis Estático (SAST) para detectar vulnerabilidades lógicas en código Python (ej. timeouts, inyecciones). | 🟠 **Medio/Alto**<br>*(Falla si encuentra malas prácticas)* |
| **Trivy** | 🐳 Build/Test | Análisis de vulnerabilidades (CVEs) en las imágenes Docker y dependencias del sistema operativo base. | 🔴 **Crítico**<br>*(Reporta vulnerabilidades del OS)* |

### Flujo del Pipeline
```mermaid
graph LR
    A[Push Code] --> B{Build & Test}
    
    subgraph "Fase de Seguridad (Shift-Left)"
        B -->|Secret Scanning| C[Gitleaks]
        B -->|SAST Python| D[Bandit]
    end
    
    C --> E[Docker Build]
    D --> E
    
    subgraph "Seguridad de Artefactos"
        E -->|Container Scan| F[Trivy]
    end
    
    F --> G[Deploy Ready]
