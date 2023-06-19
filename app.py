from flask import Flask, request, render_template
from .helpers import chunk_audio_file, send_chunks_to_server

app = Flask(__name__)

@app.route('/', methods=['GET'])
def starter():
    return render_template("index.html")


@app.route('/push_chunks', methods=['POST'])
def upload_chunks():

    file_path = "assignment_audio.wav"
    chunk_size_ms = 20  # Chunk size in milliseconds
    server_url = "http://127.0.0.1:5000/receive_audio"

    chunks = chunk_audio_file(file_path, chunk_size_ms)
    send_chunks_to_server(chunks, server_url)