# Manual de usuario y Consumo de la APP

Esta sección describe cómo desplegar el Proyecto Centinela y cómo interactuar con sus servicios.

## 1.1 Despliegue del Sistema
Para poner en marcha la plataforma en su entorno local, asegúrese de tener **Docker Desktop** instalado y ejecutándose.

1.  **Clonar el repositorio:**
    Ejecuta powershell
    (Recuerda que debes tener instalado GIT)
    ```bash
    git clone https://github.com/javierprias/proyecto-centinela.git
    cd proyecto-centinela
    ```

2.  **Iniciar los servicios:**
    Abra una terminal en la carpeta del proyecto y ejecute:
    ```bash
    docker-compose up --build
    ```
    *Espere a que termine la construcción. Sabrá que está listo cuando vea logs del `scraper` detectando noticias.*

---

## 1.2 Consumo de la API (Modo Interactivo)
La aplicación utiliza **FastAPI**, lo que genera automáticamente una documentación interactiva (Swagger UI). Esta es la forma más sencilla de consumir la aplicación.

### Paso 1: Acceder a la Interfaz
Abra su navegador web e ingrese a la siguiente dirección:
👉 **[http://localhost:8000](http://localhost:8000)**

Verá una pantalla azul con la lista de funciones disponibles (Endpoints).

### Paso 2: Verificar Estado (Health Check)
1.  Haga clic en la barra verde **`GET /` Read Root**.
2.  Haga clic en el botón **Try it out** (arriba a la derecha).
3.  Haga clic en el botón azul **Execute**.
4.  En "Server response", debería ver:
    ```json
    {
      "sistema": "Centinela",
      "estado": "Online"
    }
    ```

### Paso 3: Analizar una Noticia Manualmente
Puede simular ser el Scraper y enviar una noticia para análisis de sentimiento.

1.  Busque la barra verde **`POST /analizar` Analizar Noticia**.
2.  Haga clic en **Try it out**.
3.  En el recuadro "Request body", copie y pegue este ejemplo (una noticia falsa simulada):
    ```json
    {
      "url": "https://noticia-ejemplo.com",
      "titulo": "El mundo se acaba mañana confirma experto anónimo",
      "contenido": "Texto de prueba"
    }
    ```
4.  Haga clic en **Execute**.
5.  Mire la respuesta en "Server response". El sistema analizará el texto (negativo/alarmista) y devolverá el resultado JSON con el campo `sentimiento` y `alerta_desinformacion`.

---

## 1.3 Monitoreo del Scraper Automático
El sistema incluye un agente (Worker) que trabaja en segundo plano. No requiere intervención del usuario.

1.  Vaya a su terminal donde ejecutó `docker-compose`.
2.  Observe los logs en tiempo real. Verá que cada 60 segundos el scraper:
    *   Busca noticias nuevas en internet.
    *   Las envía automáticamente al Backend.
    *   Imprime el resultado del análisis:
    ```text
    scraper-1 | Detectado: [Título de la noticia]
    scraper-1 | Resultado Centinela: {'titulo_analizado': '...', 'sentimiento': ...}
    ```
