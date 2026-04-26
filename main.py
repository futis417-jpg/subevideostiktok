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
    "Suscríbete para más contenido de automatización.",
    "Dominando Python desde un Chromebook."
]

FONT_SIZE = 70
VIDEO_DURATION = 7
OUTPUT_VIDEO = "video_final.mp4"
TEMP_IMAGE = "temp_background.png"

# COOKIES ULTRA-LIMPIAS (Solo lo necesario para loguear)
MIS_COOKIES_DATOS = [
    {"name": "sessionid", "value": "18b77c5378a939e0a7675188609afdf7", "domain": ".tiktok.com", "path": "/", "secure": True, "httpOnly": True},
    {"name": "sessionid_ss", "value": "18b77c5378a939e0a7675188609afdf7", "domain": ".tiktok.com", "path": "/", "secure": True, "httpOnly": True},
    {"name": "sid_tt", "value": "18b77c5378a939e0a7675188609afdf7", "domain": ".tiktok.com", "path": "/", "secure": True, "httpOnly": True},
    {"name": "tt_chain_token", "value": "vsYbp866+tKkTgdUN2jDTw==", "domain": ".tiktok.com", "path": "/", "secure": True, "httpOnly": True}
]

def generar_video_texto():
    print("🎨 Generando imagen de texto...")
    fondo_color = (random.randint(0, 80), random.randint(0, 80), random.randint(0, 80))
    img = Image.new('RGB', (1080, 1920), color=fondo_color)
    d = ImageDraw.Draw(img)
    texto = random.choice(TEXTOS_NOTICIAS)
    
    try:
        font = ImageFont.truetype("arial.ttf", FONT_SIZE)
    except:
        font = ImageFont.load_default()
        
    d.text((100, 900), texto, fill=(255, 255, 255), font=font)
    img.save(TEMP_IMAGE)
    
    print("🎬 Creando video con MoviePy 2.0...")
    clip = ImageClip(TEMP_IMAGE).with_duration(VIDEO_DURATION)
    clip.write_videofile(OUTPUT_VIDEO, fps=24)

def subir_a_tiktok():
    print("🚀 Intentando subida ULTRA-LIMPIA...")
    
    # Creamos el archivo con un nombre fijo
    with open('cookies_final.json', 'w') as f:
        json.dump(MIS_COOKIES_DATOS, f)
    
    try:
        upload_video(
            OUTPUT_VIDEO,
            description='Bot automático #IA #IshakBot',
            cookies='cookies_final.json',
            browser='chromium',
            headless=True
        )
        print("✅ ¡VÍDEO PUBLICADO!")
    except Exception as e:
        print(f"❌ Error crítico en la subida: {e}")
    finally:
        if os.path.exists('cookies_final.json'):
            os.remove('cookies_final.json')

if __name__ == "__main__":
    generar_video_texto()
    subir_a_tiktok()
