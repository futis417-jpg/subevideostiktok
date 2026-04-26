import os
import random
import json
from PIL import Image, ImageDraw, ImageFont
from moviepy.video.VideoClip import ImageClip
from tiktok_uploader.upload import upload_video

# --- CONFIGURACIÓN ---
TEXTOS_NOTICIAS = [
    "¡Nueva actualización de la IA-PRO!",
    "Cómo programar bots en 2026.",
    "El futuro de los bots en TikTok.",
    "Ishak Bot: Publicando con GitHub Actions.",
    "Dominando Python desde un Chromebook."
]

FONT_SIZE = 70
VIDEO_DURATION = 7
OUTPUT_VIDEO = "video_final.mp4"
TEMP_IMAGE = "temp_background.png"

# TUS COOKIES (Asegúrate de que el sessionid sea el actual)
MIS_COOKIES_DATOS = [
    {"name": "sessionid", "value": "18b77c5378a939e0a7675188609afdf7", "domain": ".tiktok.com", "path": "/", "secure": True, "httpOnly": True},
    {"name": "sessionid_ss", "value": "18b77c5378a939e0a7675188609afdf7", "domain": ".tiktok.com", "path": "/", "secure": True, "httpOnly": True},
    {"name": "sid_tt", "value": "18b77c5378a939e0a7675188609afdf7", "domain": ".tiktok.com", "path": "/", "secure": True, "httpOnly": True}
]

def generar_video_texto():
    print("🎨 Generando imagen...")
    fondo_color = (random.randint(0, 50), random.randint(0, 50), random.randint(0, 50))
    img = Image.new('RGB', (1080, 1920), color=fondo_color)
    d = ImageDraw.Draw(img)
    texto = random.choice(TEXTOS_NOTICIAS)
    try:
        font = ImageFont.truetype("arial.ttf", FONT_SIZE)
    except:
        font = ImageFont.load_default()
    d.text((100, 900), texto, fill=(255, 255, 255), font=font)
    img.save(TEMP_IMAGE)
    print("🎬 Creando video...")
    clip = ImageClip(TEMP_IMAGE).with_duration(VIDEO_DURATION)
    clip.write_videofile(OUTPUT_VIDEO, fps=24, logger=None)

def subir_a_tiktok():
    print("🚀 Intentando subida final...")
    # Escribimos el JSON de forma que la librería NO PUEDA decir que no es válido
    with open('auth.json', 'w', encoding='utf-8') as f:
        json.dump(MIS_COOKIES_DATOS, f)
    
    try:
        # Forzamos los parámetros mínimos
        upload_video(
            OUTPUT_VIDEO,
            description='Contenido automático #IA #IshakBot',
            cookies='auth.json',
            browser='chromium',
            headless=True
        )
        print("✅ ¡LOGRADO! Mira tu TikTok.")
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        if os.path.exists('auth.json'):
            os.remove('auth.json')

if __name__ == "__main__":
    generar_video_texto()
    subir_a_tiktok()
