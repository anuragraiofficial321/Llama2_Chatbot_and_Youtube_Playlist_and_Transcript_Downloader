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


def serve_file(file_path, download_name):
    try:
        return send_file(file_path, as_attachment=True, download_name=download_name)
    except FileNotFoundError:
        abort(404)


@app.errorhandler(404)
def file_not_found(error):
    return "File Not Found", 404


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/download", methods=["POST"])
def download():
    if request.method == "POST":
        url = str(request.form["url"]).strip()

        video_transcript = transcript.youtube_transcript(url)

        video_transcript.remove_transcript_file()

        success = video_transcript.get_transcript()

        print(success)

        # Add your code to process the URL and check if generation is successful here.
        # Set this flag based on your success criteria.

        if success:
            return jsonify(success=True)  # Return a JSON response to indicate success
        else:
            return jsonify(success=False)
    return render_template("index.html")  # Return a JSON response to indicate failure


@app.route("/hindi_download")
def hindi_download():
    with open("title.txt", "r", encoding="utf-8") as ti:
        title = ti.read()

    path_file = f"Hindi_Text_File/{title}.txt"

    return serve_file(path_file, f"{title}.txt")


@app.route("/english_download")
def english_download():
    with open("title.txt", "r", encoding="utf-8") as ti:
        title = ti.read()

    path_file = f"English_Text_File/{title}.txt"
    # Handle English download logic here
    return serve_file(path_file, f"{title}.txt")


@app.route("/translate_chat")
def translate_chat():
    # Handle English download logic here
    pass


if __name__ == "__main__":
    app.run(debug=True)
