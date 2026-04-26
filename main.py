import os
import random
from PIL import Image, ImageDraw, ImageFont
from moviepy.video.VideoClip import ImageClip
from tiktok_uploader.upload import upload_video

# --- CONFIGURACIÓN ---
TEXTOS_NOTICIAS = [
    "¡Nueva actualización de la IA-PRO!",
    "Cómo programar bots en 2026 sin morir en el intento.",
    "El futuro de los bots en TikTok es ahora.",
    "Ishak Bot: Publicando cada 20 minutos con GitHub Actions.",
    "Suscríbete para más contenido de automatización."
]

FONT_SIZE = 70
VIDEO_DURATION = 7  # Segundos
OUTPUT_VIDEO = "video_final.mp4"
TEMP_IMAGE = "temp_background.png"

def generar_video_texto():
    print("🎨 Generando imagen de texto...")
    
    # Color de fondo aleatorio
    fondo_color = (random.randint(0, 100), random.randint(0, 100), random.randint(0, 100))
    img = Image.new('RGB', (1080, 1920), color=fondo_color)
    d = ImageDraw.Draw(img)
    
    texto = random.choice(TEXTOS_NOTICIAS)
    
    try:
        font = ImageFont.truetype("arial.ttf", FONT_SIZE)
    except:
        font = ImageFont.load_default()

    # Dibujar texto y adorno
    d.text((100, 900), texto, fill=(255, 255, 255), font=font)
    d.rectangle([90, 880, 110, 1000], fill=(254, 44, 85))
    
    img.save(TEMP_IMAGE)

    print("🎬 Convirtiendo imagen a video...")
    # ESTA ES LA LÍNEA DEL ERROR - ASEGÚRATE QUE ESTÉ ALINEADA CON EL PRINT DE ARRIBA
    clip = ImageClip(TEMP_IMAGE).with_duration(VIDEO_DURATION)
    clip.write_videofile(OUTPUT_VIDEO, fps=24)

def subir_a_tiktok():
    print("🚀 Iniciando subida a TikTok...")
    
    # Verificamos si existe el archivo de cookies generado por el Workflow
    if not os.path.exists('cookies.txt'):
        print("❌ Error: No se encontró el archivo cookies.txt")
        return

    try:
        upload_video(
            OUTPUT_VIDEO,
            description=f'Contenido automático por IA-PRO #bot #automation #2026',
            cookies='cookies.txt',
            browser='chromium',
            headless=True
        )
        print("✅ ¡Publicado con éxito!")
    except Exception as e:
        print(f"❌ Error al subir: {e}")

if __name__ == "__main__":
    generar_video_texto()
    subir_a_tiktok()
