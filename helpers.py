import os
import requests
from pydub import AudioSegment
import time

file_path = "assignment_audio.wav"
chunk_size_ms = 20 #20 milliseconds
def chunk_audio_file(file_path, chunk_size):
    audio = AudioSegment.from_file(file_path)
    duration = len(audio)
    chunks = []
    for start in range(0, duration, chunk_size):
        end = start + chunk_size
        if end > duration:
            end = duration
        chunk = audio[start:end]
        chunks.append(chunk)
    return chunks

def send_chunks_to_server(chunks, server_url):
    for i, chunk in enumerate(chunks):
        chunk.export(f"chunk_{i}.wav", format="wav")  # Export chunk as temporary WAV file
        with open(f"chunk_{i}.wav", "rb") as file:
            response = requests.post(server_url, files={"audio": file})
        os.remove(f"chunk_{i}.wav")  # Remove temporary WAV file
        
        # Process the server response
        print(response.text[speech_status]) #Check sever console/terminal for print
        time.sleep(1) #sleep for 1 second


