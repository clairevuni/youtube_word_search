from youtube_transcript_api import YouTubeTranscriptApi

import json

def get_transcript(video_id):
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        # transcript_list è una lista di dict con 'text', 'start', 'duration'
        return transcript_list
    except Exception as e:
        print(f"Errore nel recuperare il transcript: {e}")
        return None


def save_transcript_to_json(transcript, filepath):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(transcript, f, ensure_ascii=False, indent=2)
