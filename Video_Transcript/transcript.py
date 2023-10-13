import urllib.parse as urlparse
from youtube_transcript_api import YouTubeTranscriptApi
import re
import os
from pytube import Playlist, YouTube


class youtube_transcript:
    def __init__(self, url):
        self.url = url

    def remove_transcript_file(self):
        try:
            folder_path = "Transcript_Text_File"
            for filename in os.listdir(folder_path):
                if filename.endswith(".txt"):
                    os.remove(os.path.join(folder_path, filename))
        except FileNotFoundError as e:
            pass

    def get_transcript(self):
        try:
            parsed_url = urlparse.urlparse(self.url)
            video_id = urlparse.parse_qs(parsed_url.query)["v"][0]
            video = YouTube(self.url)
            title = video.title.strip()
        except:
            video_id = re.search(r"(?<=youtu.be/)[^&#]+", self.url).group(0)

        try:
            video = YouTube(self.url)
            title = video.title.strip()
            title = title.replace(" ", "_")
            title = title.replace("|", "_")

        except:
            title = "transcript_file"

        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            # print(transcript)

            with open(f"Transcript_Text_File/{title}.txt", "a") as tr:
                for segment in transcript:
                    tr.write(segment["text"] + " ")

        except:
            print(
                f"""Could not retrieve a transcript for the video {self.url}
                This is most likely caused by: Subtitles are disabled for this video"""
            )

        return title
