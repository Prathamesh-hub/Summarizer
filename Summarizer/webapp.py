import streamlit as st
import requests
from streamlit_lottie import st_lottie
import json
import os
import Audiodownloader as ad
import Translation as tl
import Summarize as sm
import Transcriptgenerator as tg
import VideotoAudio as vta

languages=('bengali', 'bhojpuri', 'chinese (simplified)', 'english', 'french', 'german', 'greek', 'gujarati', 'hindi', 'japanese', 'kannada', 'sanskrit', 'marathi', 'punjabi')





st.set_page_config(page_title='Video Summarizer', page_icon=":page_with_curl:")

hide_mainmenu = """
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
"""
st.markdown(hide_mainmenu, unsafe_allow_html=True)


if 'summary_youtube' not in st.session_state:
    st.session_state['summary_youtube']=""
    st.session_state['translation']=''

st.title('Video Summarizer')
st.header('For YouTube Videos')



ytlink = st.text_input('Paste youtube link')
summarizebtn = st.button("Summarize", type="primary")


selectlang = st.selectbox(
    'Select language for translation',
    languages,
    index=12
    )
translatebtn = st.button("Translate", type="primary")

st.header('For Video Files')

uploaded_file = st.file_uploader("Choose a file")
summarizevdo = st.button("Summarize",key='summarizevdo', type="primary")

code=""



if summarizebtn :
    if "youtube.com" not in ytlink:
        st.header('Please, Enter valid link')
    else:
        load = st.image('Loading.gif', caption='Please wait....')
        audio_file = ad.youtube_audio_downloader(ytlink)
        transcript = tg.transcribe(audio_file)
        summary = sm.summarizemain(transcript)
        st.session_state['summary_youtube']=summary
        load.empty()
        os.remove(audio_file)
        os.remove(transcript)


translatedsummary=""
if translatebtn :
    translatedsummary= tl.translate1(st.session_state.summary_youtube, language= selectlang)
    st.session_state.translation=translatedsummary




if summarizevdo :
    vta.video_to_audio(uploaded_file.name)
    transcript_file = tg.transcribe("audio.mp3")
    summary = sm.summarizemain (transcript_file)
    st.session_state.summary_youtube=summary
    os.remove(transcript_file)
    os.remove("audio.mp3")

if summarizebtn or st.session_state.summary_youtube != "":
    try: 
        st.video(ytlink)
    except:
        st.image('error.gif', caption='Provided link was invalid....')

txt = st.text_area(
    "SUMMARY:",
    value= st.session_state.summary_youtube,
    height=350,
    disabled= True
    )
st.download_button('Download summary', st.session_state.summary_youtube)

trans = st.text_area(
    "Translation:",
    value= st.session_state.translation,
    height=350,
    disabled= True
    )
st.download_button('Download translation', st.session_state.translation)
