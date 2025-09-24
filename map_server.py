# map_server.py
from flask import Flask, request, jsonify
import os, time

app = Flask(__name__)
os.makedirs("uploaded_maps", exist_ok=True)

@app.route('/upload_map', methods=['POST'])
def upload_map():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400
    file = request.files['file']
    fname = f"uploaded_maps/{int(time.time())}.jpg"
    file.save(fname)
    print("✅ Saved:", fname)
    return jsonify({"status": "ok", "file": fname}), 200

if __name__ == '__main__':
    app.run(port=5001)
