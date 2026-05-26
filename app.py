import io
import os
import subprocess
import uuid
from pathlib import Path

from flask import Flask, jsonify, render_template, request, send_file

app = Flask(__name__)

BASE_DIR = Path(__file__).parent
UPLOAD_DIR = BASE_DIR / "uploads"
UPLOAD_DIR.mkdir(exist_ok=True)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/convert", methods=["POST"])
def convert():
    if "file" not in request.files:
        return jsonify({"error": "No se envió ningún archivo"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No se seleccionó ningún archivo"}), 400

    if not file.filename.lower().endswith(".m4a"):
        return jsonify({"error": "Solo se aceptan archivos .m4a"}), 400

    original_name = Path(file.filename).stem
    unique_id = str(uuid.uuid4())

    input_path = UPLOAD_DIR / f"{unique_id}.m4a"
    output_path = UPLOAD_DIR / f"{unique_id}.mp3"
    output_filename = f"{original_name}.mp3"

    try:
        file.save(input_path)

        cmd = [
            "ffmpeg",
            "-i", str(input_path),
            "-codec:a", "libmp3lame",
            "-b:a", "320k",
            "-y",
            str(output_path),
        ]

        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode != 0:
            return jsonify({
                "error": f"Error en la conversión: {result.stderr}"
            }), 500

        with open(output_path, "rb") as f:
            mp3_data = f.read()

    finally:
        if input_path.exists():
            input_path.unlink()
        if output_path.exists():
            output_path.unlink()

    return send_file(
        io.BytesIO(mp3_data),
        mimetype="audio/mpeg",
        as_attachment=True,
        download_name=output_filename,
    )


if __name__ == "__main__":
    try:
        subprocess.run(["ffmpeg", "-version"], capture_output=True, check=True)
    except (FileNotFoundError, subprocess.CalledProcessError):
        print("=" * 60)
        print("  ERROR: ffmpeg no está instalado o no está en el PATH.")
        print("=" * 60)
        print("  Descarga ffmpeg desde:")
        print("  https://www.gyan.dev/ffmpeg/builds/")
        print()
        print("  Instrucciones rápidas:")
        print("  1. Descarga ffmpeg-release-essentials.zip")
        print("  2. Extrae el contenido en C:\\ffmpeg")
        print("  3. Agrega C:\\ffmpeg\\bin a tus variables de entorno PATH")
        print("  4. Reinicia la terminal y ejecuta este script de nuevo")
        print("=" * 60)
        exit(1)

    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
