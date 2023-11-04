import requests


API_URL = "https://api-inference.huggingface.co/models/openpecha/speecht5-tts-01"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content

audio_bytes = query({
	"inputs": "The answer to the universe is 42",
})
# You can access the audio with IPython.display for example
from IPython.display import Audio
Audio(audio_bytes)