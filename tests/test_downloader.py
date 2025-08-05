from youtube_indexer.downloader import download_audio

def test_download_audio():
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    output_dir = "data/audio_test"
    
    audio_path = download_audio(url, output_dir)
    
    assert audio_path is not None
    assert audio_path.endswith(".mp3")
