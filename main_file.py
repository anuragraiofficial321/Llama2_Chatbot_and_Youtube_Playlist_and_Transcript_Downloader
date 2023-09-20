from Video_Transcript import transcript
import os, sys
from os.path import dirname, join, abspath


sys.path.insert(0, abspath(join(dirname(__file__), "..")))

url = "https://www.youtube.com/watch?v=gveDhZW-rUk&pp=ygUMaHViZXJtYW4gbGFi"


video_transcript = transcript.youtube_transcript(url)

video_transcript.remove_transcript_file()

video_transcript.get_transcript()
