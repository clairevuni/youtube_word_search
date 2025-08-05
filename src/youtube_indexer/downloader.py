from urllib.parse import urlparse, parse_qs
from pathlib import Path
from yt_dlp import YoutubeDL

def extract_video_id(url):
    query = urlparse(url)
    if query.hostname == "youtu.be":
        return query.path[1:]
    if query.hostname in ('www.youtube.com', 'youtube.com', 'm.youtube.com'):
        if query.path == '/watch':
            p = parse_qs(query.query)
            return p['v'][0]
        if query.path[:7] == '/embed/':
            return query.path.split('/')[2]
        if query.path[:3] == '/v/':
            return query.path.split('/')[2]
    return None


def download_audio(url, output_dir):
    video_id = extract_video_id(url)
    print(f"DEBUG - video_id: {video_id}")
    if video_id is None:
        print("Errore nel trovare il video, riprova")
        return None
    
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    audio_filename = f"audio_{video_id}.mp3"
    audio_path = Path(output_dir) / audio_filename
    
    if audio_path.exists():
        print(f"File audio già presente: {audio_path}")
        return str(audio_path)
    
    print(f"Scarico audio da YouTube per video_id: {video_id}...")
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': str(audio_path.with_suffix('.%(ext)s')),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True,
        'no_warnings': True,
        'ffmpeg_location': r'C:\Users\chiar\OneDrive\Desktop\ffmpeg-7.1.1-essentials_build\ffmpeg-7.1.1-essentials_build\bin',
    }
    
    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download completato.")
    except Exception as e:
        print(f"Errore durante il download: {e}")
        return None
    
    return str(audio_path)
