from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

@app.route("/")
def home():
    return "YouTube Transcript API läuft!"

@app.route("/transcript")
def get_transcript():
    video_id = request.args.get("id")
    if not video_id:
        return jsonify({"error": "Bitte gib eine Video-ID an (Parameter: id)"}), 400
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return jsonify(transcript)
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run()
