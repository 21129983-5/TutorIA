from elevenlabs import play
from elevenlabs.client import ElevenLabs
from dotenv import find_dotenv, load_dotenv

import os

load_dotenv(find_dotenv())

ELEVEN_LABS_API_KEY = os.getenv("ELEVEN_LABS_API_KEY")

def read_text(message):
  client = ElevenLabs(
    api_key=ELEVEN_LABS_API_KEY, # Defaults to ELEVEN_API_KEY
  )

  audio = client.generate(
    text=message,
    voice="Rachel",
    model="eleven_multilingual_v2"
  )
  play(audio)
  return None