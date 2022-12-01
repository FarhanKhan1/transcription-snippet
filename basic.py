import os #importing os module for navigation into os
import speech_recognition as sr #importing modeule for transcription 
try:    
    r = sr.Recognizer() #starting with object creation 
    AUDIO_FILE = os.getcwd() + '/movie.wav' #Let's read the audio file, note: Please replace file name with your file name 
    print(AUDIO_FILE) # This will show if we have the correct path to our file
    with sr.AudioFile(AUDIO_FILE) as source: #opening audio file using "AudioFile" method
        audio = r.record(source)  # read the entire audio file
        print(r.recognize_google(audio)) #passing audio file to one of the available API/speech recognition engine (for me, i am using google engine)

except Exception as err:
    print(err)
