import streamlit as st
import trans
import os

auth_key = st.secrets['auth_key']
def ex(url):
    if st.button('apply'):
        try:
            name=trans.transcribe(url)
            fileid=trans.fileId(name,auth_key)
            transid=trans.transcribeId(fileid,auth_key)
            st.write('Wait for the transcription...')
            transcribe=trans.text_output(transid,auth_key)
            st.snow()
            st.write('Transription:')
            st.write(transcribe)
            os.remove(name)
        except:
            st.warning('paste a valid yt-url')

           
        
if __name__ == '__main__':
    st.title('Audio Transcription powered by NeuralSpace')
    url = st.text_input('Enter URL of YouTube video:')
    ex(url)
    