import requests
from bs4 import BeautifulSoup
import time
import schedule
import os

# La URL del Backend (en Docker, el host es el nombre del servicio: 'backend')
API_URL = "http://backend:8000/analizar"

# Web objetivo (Usamos una simple para demo)
TARGET_URL = "https://news.ycombinator.com/" 

def job():
    print(f"--- Iniciando ronda de vigilancia en {TARGET_URL} ---")
    try:
        # 1. Hacemos el Scraping
        response = requests.get(TARGET_URL)
        if response.status_code != 200:
            print("Error al acceder a la web")
            return

        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extraemos los títulos (en HackerNews son clase 'titleline')
        # NOTA: Esto cambia según la web que elijas.
        titulos = soup.select('.titleline > a')

        # Tomamos solo los primeros 3 para no saturar
        for item in titulos[:3]:
            titulo_texto = item.get_text()
            link = item.get('href')
            
            print(f"Detectado: {titulo_texto}")

            # 2. Enviamos al Backend para análisis
            payload = {
                "url": link,
                "titulo": titulo_texto,
                "contenido": "Contenido pendiente de scraping profundo"
            }

            try:
                res = requests.post(API_URL, json=payload)
                print(f"Resultado Centinela: {res.json()}")
            except Exception as e:
                print(f"Error conectando con API: {e}")
            
            time.sleep(1) # Pausa respetuosa

    except Exception as e:
        print(f"Error crítico en scraper: {e}")

def run_scheduler():
    # Ejecutar cada 1 minuto
    schedule.every(1).minutes.do(job)
    
    # Ejecutar una vez al arrancar para probar
    job()

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    # Pequeña pausa para dar tiempo a que el backend arranque
    time.sleep(5)
    run_scheduler()