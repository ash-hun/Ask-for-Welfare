def STT(mp3, client):
    """
    STT는 Speech to text의 약자로 음성을 텍스트로 바꾸는 기능을 말한다.
    OpenAI 클라이언트를 이용한 메서드를 활용함.
    'whisper-1' 모델을 사용.

    Args:
        mp3 (_type_): 소스 오디오 파일(*.mp3)

    Returns:
        _type_: 변환된 스크립트 파일
    """
    audio_file = open(mp3, "rb")
    transcript = client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file, 
        response_format="text"
    )
    return transcript

def TTS(txt, client):
    """
    TTS는 Text to Speech의 약자로 텍스트를 음성으로 바꾸는 기능을 말한다.
    OpenAI 클라이언트를 이용한 메서드를 활용함.
    'tts-1' 모델을 사용. 'whisper'는 STT 전용인 것 같다.

    Args:
        txt (_type_): 소스 텍스트 파일(*.txt)
    """
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=txt,
    )
    response.stream_to_file("output.mp3")



# if __name__ == "__main__":
#     """
#     Prework to execute 'whisper.py'
#     - pip install git+https://github.com/openai/whisper.git
#     - pip install --upgrade openai
#     - python whisper.py
#     """
#     client = OpenAI()

#     # STT Sample
#     file = './audio/test01.mp3'
#     res = STT(file)
#     print(f"STT test : {res}")

#     # TTS Sample
#     sample = '혜민아 다했다..'
#     TTS(sample)