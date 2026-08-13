from dotenv import load_dotenv
import os
from elevenlabs.client import ElevenLabs
from elevenlabs import PronunciationDictionaryVersionLocator

load_dotenv()

client = ElevenLabs(
    api_key=os.getenv('ELEVENLABS_API_KEY') # This is stored in a .env file that is loaded above
)


# The voices that I'm using by demographic property
# names are of format [B|W] [S|N] [F|M], 
# where B/W refers to Black or White, S|N refers to Southern or Non-Southern, and F|M refers to Female or Male
voice_keys = {
    'BNF' : 'NQMJRVvPew6HsaebYnZj', # Black, Non-Southern, Female - 'Cecily'
    'WSF' : 'qqKpdUwkD3h8VyDLKQyz', # White, Southern, Female - 'Cassie'
    'BSM' : '4m3xt3xfssayzO1e9shv', # Black, Southern, Male - 'Mr. Pete'
    'WSM' : 'D4xQvkd2SmpDZJ8sEwvA', # White, Southern, Male - 'Rhett Suton'
    'BNM' : 'pQh9V7vKVWKF3pBFDSc5', # Black, Non-Southern, Male - 'Miles'
    'BSF' : 'fLQhkOW7F9KVKAjYCbhr', # Black, Southern, Female - 'CiCi'
    'WNM' : 'ljX1ZrXuDIIRVcmiVSyR', # White, Non-Southern, Male - 'Michael'
    'WNF' : 'l4Coq6695JDX9xtLqXDE', # White, Non-Southern, Female - 'Lauren'
}


# This is a test block that makes sure I got all of the voice keys right
# # for name in voice_keys.keys():
# #     print(name)
# #     print(client.voices.get(voice_keys[name]).name)


# VOICE_BEING_USED = voice_keys['WNM']
VOICE_BEING_USED = 'JBFqnCBsd6RMkjVDRZzb', # temporarily testing with a free voice

# with open("pronunciation_guide.pls", "rb") as f:
#     pronunciation_dictionary = client.pronunciation_dictionaries.create_from_file(
#         file=f.read(), name="Pseudoword Dictionary"
#     )

pronunciation_dictionary = client.pronunciation_dictionaries.get('y94uKypoHq7oFFtu8A1U')

print(pronunciation_dictionary.name)
print(pronunciation_dictionary.rules)
print(pronunciation_dictionary.id)
print(pronunciation_dictionary.latest_version_id)

# words = ['Normal', 'Changed']

# for word in words:
#     response = client.text_to_speech.convert(
#         text=word,
#         voice_id=VOICE_BEING_USED,
#         model_id="eleven_flash_v2",
#         output_format='mp3_44100_64',
#         # previous_text="Here is a word: ",
#         # next_text=".",
#         pronunciation_dictionary_locators=[
#             PronunciationDictionaryVersionLocator(
#                 pronunciation_dictionary_id=pronunciation_dictionary.id,
#                 version_id=pronunciation_dictionary.version_id,
#             )
#         ],
#     )

#     with open(f'output/{word}.mp3', 'wb') as f:
#         for chunk in response:
#             f.write(chunk)


