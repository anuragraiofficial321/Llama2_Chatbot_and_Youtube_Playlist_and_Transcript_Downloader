from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    send_file,
    abort,
    jsonify,
)
from Video_Transcript import transcript
import os, sys
from os.path import dirname, join, abspath

sys.path.insert(0, abspath(join(dirname(__file__), "..")))

app = Flask(__name__)
app.config["TIMEOUT"] = None


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


def serve_file(file_path, download_name):
    try:
        return send_file(file_path, as_attachment=True, download_name=download_name)
    except FileNotFoundError:
        abort(404)


@app.errorhandler(404)
def file_not_found(error):
    return "File Not Found", 404


@app.route("/download", methods=["POST"])
def download():
    url = str(request.form.get("youtube_url"))
    print(url)

    video_transcript = transcript.youtube_transcript(url)

    video_transcript.remove_transcript_file()

    title = video_transcript.get_transcript()

    Training_data = f"Transcript_Text_File/{title}.txt"

    return serve_file(Training_data, f"{title}.txt")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

# url = "https://www.youtube.com/watch?v=gveDhZW-rUk&pp=ygUMaHViZXJtYW4gbGFi"
# url = "https://youtu.be/cwakOgHIT0E"
