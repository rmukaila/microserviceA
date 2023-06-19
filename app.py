from flask import Flask, request
from helpers import chunk_audio_file, send_chunks_to_server


@app.route('/push_chunks', methods=['POST'])
def upload_chunks():

    file_path = "path/to/audio_file.mp3"
    chunk_size_ms = 5000  # Chunk size in milliseconds
    server_url = "http://your_server_url.com/upload"

    chunks = chunk_audio_file(file_path, chunk_size_ms)
    send_chunks_to_server(chunks, server_url)