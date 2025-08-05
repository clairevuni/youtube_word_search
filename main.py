from youtube_indexer.downloader import download_audio, extract_video_id
from youtube_indexer.transcript import get_transcript

def process_video(url, output_dir):
    video_id = extract_video_id(url)
    if not video_id:
        print("Video ID non valido")
        return
    
    audio_path = download_audio(url, output_dir)
    if not audio_path:
        print("Download audio fallito")
        return
    
    transcript = get_transcript(video_id)
    if not transcript:
        print("Transcript non disponibile")
        return
    
    # Puoi salvare transcript su file
    with open(f"{output_dir}/{video_id}_transcript.json", "w", encoding="utf-8") as f:
        import json
        json.dump(transcript, f, ensure_ascii=False, indent=2)
    
    print(f"Audio salvato in: {audio_path}")
    print(f"Transcript salvato in: {output_dir}/{video_id}_transcript.json")
