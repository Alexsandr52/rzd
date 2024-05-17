import json
import streamlit as st
import requests
from pydub import AudioSegment

url="https://pars1vali-rzd-b134.twc1.net/audio"

# def _convert_mp3(file_mp3):
#     audio_mp3 = AudioSegment.from_file(file_mp3, format="mp3")
#     audio_wav = audio_mp3.export("output_audio.wav", format="wav")

def send_audio(uploaded_file):
    # file_name = uploaded_file.name.lower()
    # if file_name.endswith('.mp3'):
    #     uploaded_file = _convert_mp3(uploaded_file)

    files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
    response = requests.post(url, files=files)

    if response.status_code == 200:
        response_json = json.loads(response.text)
        st.write(response_json)
        st.success(f"File '{uploaded_file.name}' uploaded successfully!")
    else:
        st.error(f"Failed to upload file. Status code: {response.status_code}")


st.title("РЖД для служебных переговоров")
uploaded_file = st.file_uploader("Загрузите аудио", type=['wav','mp3'] )

if uploaded_file is not None:
    with st.spinner("Обработка"):
        send_audio(uploaded_file)

