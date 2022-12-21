# Speech-to-Text Transcription of YouTube Videos powered by NeuralSpace API

This project allows users to transcribe the audio of any YouTube video into text using NeuralSpace's speech to text API. It takes as input a YouTube URL and returns a transcript of the audio in the video.

### Try Transcribing:
web_app: https://blessontomjoseph-transcription-neuralspace-app-qxqa4t.streamlit.app/



### Installation
clone this repository and run the following commands:

```bash
echo 'auth_key = "<your_NeuralSpace_auth_key>"' >> .streamlit/secrets.toml
```

this adds your NeuralSpace authentication key in the appropriate directory


```bash
pip install jj
docker build -t <image_name> .
docker run <image_name>
```
this creates a docker image and runs the image
