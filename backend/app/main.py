from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from textblob import TextBlob

app = FastAPI()

# Definimos qué tipo de datos esperamos recibir
class Noticia(BaseModel):
    url: str
    titulo: str
    contenido: str = None

@app.get("/")
def read_root():
    return {"sistema": "Centinela", "estado": "Online"}

@app.post("/analizar")
def analizar_noticia(noticia: Noticia):
    """
    Recibe una noticia, analiza el sentimiento y decide si es sospechosa.
    """
    analysis = TextBlob(noticia.titulo)
    polarity = analysis.sentiment.polarity  # Va de -1 (Muy negativo) a 1 (Muy positivo)
    
    # Lógica simple de "Fake News" para el TP:
    # Si es muy polarizada (muy odio o mucha felicidad exagerada), es sospechosa.
    es_sospechosa = False
    if polarity < -0.5 or polarity > 0.5:
        es_sospechosa = True

    return {
        "titulo_analizado": noticia.titulo,
        "sentimiento": polarity,
        "alerta_desinformacion": es_sospechosa,
        "mensaje": "Análisis completado por Centinela AI"
    }

# --- ZONA DE PELIGRO ---
# Esto es una vulnerabilidad intencional para probar el pipeline
#def connect_to_aws():
    # Gitleaks detectará este patrón de clave AKIA...
#    aws_access_key_id = "AKIAIMW666S7BELOWKEY" 
#    return "Conectado"