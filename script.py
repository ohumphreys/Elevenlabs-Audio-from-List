from dotenv import load_dotenv
import os
import csv
from elevenlabs.client import ElevenLabs
from elevenlabs import PronunciationDictionaryVersionLocator, VoiceSettings

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
    'BNM' : '6OzrBCQf8cjERkYgzSg8', # Black, Non-Southern, Male - 'Young Jamal'
    'BSF' : 'fLQhkOW7F9KVKAjYCbhr', # Black, Southern, Female - 'CiCi'
    'WNM' : 'ljX1ZrXuDIIRVcmiVSyR', # White, Non-Southern, Male - 'Michael'
    'WNF' : 'l4Coq6695JDX9xtLqXDE', # White, Non-Southern, Female - 'Lauren'
}

# This is just used for testing
# # for name in voice_keys.keys():
# #     print(name)
# #     print(client.voices.get(voice_keys[name]).name)

VOICE_BEING_USED = voice_keys['BSF']
# VOICE_BEING_USED = 'JBFqnCBsd6RMkjVDRZzb' # temporarily testing with a free voice



# pronunciation dictionary of pseudowords that I set up on my account
pro_dict = client.pronunciation_dictionaries.get('4GgzLpWGrKPg1pz24qgj') 
assert pro_dict.latest_version_id == 'DZ3zZE8nVMTctoMwHgun' # may have changed by time of use

# pro_dict = client.pronunciation_dictionaries.get('y94uKypoHq7oFFtu8A1U') # different dictionary, used for testing

def record_word(word: str):
    
    # correct capitalization for non-pseudowords
    if (word[0] != '/'):
        word = word.title()
    
    response = client.text_to_speech.convert(
        text=word,
        voice_id=VOICE_BEING_USED,
        model_id="eleven_flash_v2",
        language_code='en',
        voice_settings=VoiceSettings(speed=0.8),
        output_format='mp3_44100_128',
        pronunciation_dictionary_locators=[
            PronunciationDictionaryVersionLocator(
                pronunciation_dictionary_id=pro_dict.id,
                version_id=pro_dict.latest_version_id,
            )
        ],
    )

    with open(f'output/{FOLDER_PREFIX}/{word.strip("/")}.mp3', 'wb') as f:
        for chunk in response:
            f.write(chunk)
            

# FOLDER_PREFIX = "BSF/pseudo/one syllable"
# with open('input/second_set/One Syllable Pseudo.csv', newline='') as f:
#     words = [row[0] for row in csv.reader(f)]

FOLDER_PREFIX = "rerecords"
words = ['Square']

for word in words:
    record_word(word)


