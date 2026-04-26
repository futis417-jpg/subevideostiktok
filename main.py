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

# TUS COOKIES (YA INTEGRADAS)
MIS_COOKIES_DATOS = [
    {"domain": ".tiktok.com", "expirationDate": 1784734987, "name": "delay_guest_mode_vid", "path": "/", "secure": True, "value": "8"},
    {"domain": ".tiktok.com", "expirationDate": 1808770630, "name": "tt-target-idc-sign", "path": "/", "secure": True, "value": "WSYNVbkIog5Yw3lFm2yP3vSUpxdc_TgZbjdmTJbm5Z9Th_tsf7qR79VyiW9vuuqW6vPfJv9pfiLjI2yE_ML5FM74cyKKLTRh8ThSlXAEF1YLKwpy3666DWg-ZIwpaG5a_N88Drgw1jO7px4m5TslN5F9upWq9ZoiSQstEC7OHydWQz_Yt01kkmtZkiVznwOlJ6D2eGgPtxrO19NRvuo1nSihs1BYivivuZ3zShqwzd3hm5ZFXnYpeH37ebWJ-N5T9L3GD0szE4k29iHjpGAVaD_tJkbnxxu7ZgDawqLoPO2EF-LQS_7OiN5vqbPkiy4f7FqHlyp4Xx-InNPLy-WSu8lu6VBZq89ZfBjluCMQzm5Wrl73n6nFHGpLCiEPTRWqBuShkNHhoLscj7XkXB943aZ3NlWWVoP7mPdkW8Va_naJ3ViSCyQYg26uG8TJi7qLAXnjstZfGyty_RjT8gC322rThkW_rkudJPEY0VFUAgV67lhKVeP4Hle4kvyxIKSV"},
    {"domain": ".tiktok.com", "expirationDate": 1805122652, "name": "living_user_id", "path": "/", "secure": True, "value": "257475526030"},
    {"domain": ".tiktok.com", "expirationDate": 1778098631, "name": "msToken", "path": "/", "secure": True, "value": "tcHeHDMESied0MG1zq3JnFIqX9tmhNWsXfqyBprkJYKFzQEV9Li4o0lqdHQNdVQdOxZR-r0fjre8tyiM41yymr4WWlAd7sKEZ0yaj_6qk8d-hVhPIlzRrDIePT8WP1aSmMF-Xh7uWvLxWy8="},
    {"domain": ".tiktok.com", "expirationDate": 1791138446, "name": "sessionid", "path": "/", "secure": True, "value": "18b77c5378a939e0a7675188609afdf7"},
    {"domain": ".tiktok.com", "expirationDate": 1791138446, "name": "sessionid_ss", "path": "/", "secure": True, "value": "18b77c5378a939e0a7675188609afdf7"},
    {"domain": ".tiktok.com", "expirationDate": 1791138446, "name": "sid_tt", "path": "/", "secure": True, "value": "18b77c5378a939e0a7675188609afdf7"},
    {"domain": ".tiktok.com", "expirationDate": 1808770625, "name": "ttwid", "path": "/", "secure": True, "value": "1%7CXL2zKyuekGUgedRGpCs_KfyRn6oSaWZUy1b6rwD5hJM%7C1777234625%7Cdb4a12f211a047f914c541a7eec5d0bf1d13b00c49f3d36af010b07a595e8125"}
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
    
    print("🎬 Creando video...")
    clip = ImageClip(TEMP_IMAGE).with_duration(VIDEO_DURATION)
    clip.write_videofile(OUTPUT_VIDEO, fps=24)

def subir_a_tiktok():
    print("🚀 Intentando subir a tu cuenta...")
    
    # Creamos el archivo de cookies al vuelo
    with open('cookies.json', 'w') as f:
        json.dump(MIS_COOKIES_DATOS, f)
    
    try:
        upload_video(
            OUTPUT_VIDEO,
            description='Bot automático #IA #IshakBot',
            cookies='cookies.json',
            browser='chromium',
            headless=True
        )
        print("✅ ¡VÍDEO PUBLICADO!")
    except Exception as e:
        print(f"❌ Fallo en la subida: {e}")
    finally:
        if os.path.exists('cookies.json'):
            os.remove('cookies.json')

if __name__ == "__main__":
    generar_video_texto()
    subir_a_tiktok()
