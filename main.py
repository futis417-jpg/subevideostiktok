import os
import random
import json
import tempfile
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

# TUS COOKIES
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
    print("🚀 Intentando subida con versión 1.2.0...")
    
    # Usamos un archivo temporal con formato estricto
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as tf:
        json.dump(MIS_COOKIES_DATOS, tf)
        cookie_path = tf.name

    try:
        upload_video(
            OUTPUT_VIDEO,
            description='Bot automático #IA #IshakBot',
            cookies=cookie_path,
            browser='chromium',
            headless=True
        )
        print("✅ ¡LOGRADO!")
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        if os.path.exists(cookie_path):
            os.remove(cookie_path)

if __name__ == "__main__":
    generar_video_texto()
    subir_a_tiktok()
