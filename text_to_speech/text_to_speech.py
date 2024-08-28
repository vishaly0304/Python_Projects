# importing important python modules
import pyttsx3  # text to speech library that works offline

# creating an object for pyttsx3 
engine= pyttsx3.init()

# sea how many voices you have in your computer
for voice in engine.getProperty("voices"):
    print(voice)

voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)  #setting the voice
# For Changing speech rate
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-10)


# Creating function for converting text to speech
def speak(audio):
    engine.say(audio)
    #engine.save_to_file(audio, 'test1.mp3') # to save that audio as a mp3 file
    engine.runAndWait()

# Ask the user to enter text
Text= input("Enter your text now: ")

speak(Text)