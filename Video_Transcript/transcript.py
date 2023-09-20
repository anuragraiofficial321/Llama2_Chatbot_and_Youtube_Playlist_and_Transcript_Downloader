import urllib.parse as urlparse
from youtube_transcript_api import YouTubeTranscriptApi
import re
import os


class youtube_transcript:
    def __init__(self, url):
        self.url = url

    def remove_transcript_file(self):
        try:
            os.remove("Transcript_Text_File/transcript.txt")
        except FileNotFoundError as e:
            pass

    def get_transcript(self):
        try:
            parsed_url = urlparse.urlparse(self.url)
            video_id = urlparse.parse_qs(parsed_url.query)["v"][0]
        except:
            video_id = re.search(r"(?<=youtu.be/)[^&#]+", self.url).group(0)

        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)

            with open("Transcript_Text_File/transcript.txt", "a") as tr:
                for segment in transcript:
                    tr.write(segment["text"])

        except:
            print(
                f"""Could not retrieve a transcript for the video {self.url}
                This is most likely caused by: Subtitles are disabled for this video"""
            )
