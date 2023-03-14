from gtts import gTTS
from playsound import playsound

text = '안녕하세요, 이태윤입니다'

tts = gTTS(text=text, lang ='ko',slow = True)
tts.save('./studyPython/output/hi.mp3')
print('생성 완료')
playsound('./studyPython/output/hi.mp3')
print('음성출력 완료')