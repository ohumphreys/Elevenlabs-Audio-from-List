from google import genai
import wave
import base64
from dotenv import load_dotenv


# The script requires having an environment variable named GEMINI_API_KEY with your API key in a .env file
load_dotenv()



def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(sample_width)
        wf.setframerate(rate)
        wf.writeframes(pcm)

client = genai.Client()

def record_word(word, filepath):

    interaction = client.interactions.create(
        model="gemini-3.1-flash-tts-preview",
        input=f"Say the following word clearly in an RP british accent: {word}.",
        response_format={"type": "audio"},
        generation_config={
            "speech_config": [
                {"voice": "Zephyr"}
            ]
        }
    )
    
    wave_file(filepath, base64.b64decode(interaction.output_audio.data)) # type: ignore
    
words = ["Pobe", "Aluminium Schedule"]

# with open('input/second_set/One Syllable Pseudo.csv', newline='') as f:
#     words = [row[0] for row in csv.reader(f)]

for word in words:
    record_word(word, f'output/British/{word}.wav')