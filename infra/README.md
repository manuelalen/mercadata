# Infraestructura GitOps con Argo CD

Esta carpeta contiene los manifiestos para desplegar la app `mercadata` en tres entornos:

- `dev`: entorno de desarrollo, con autosync activado.
- `test`: entorno de pruebas, requiere revisión previa.
- `prod`: entorno de producción, sincronización controlada.

Cada entorno incluye un `deployment.yaml` que será gestionado por Argo CD.

Los manifiestos de tipo `Application` en `infra/applications/` son los recursos que Argo CD usa para rastrear cada carpeta como una app independiente.
