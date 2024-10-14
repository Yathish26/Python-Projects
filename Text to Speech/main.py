from gtts import gTTS
import os
import pygame
import random

def text_to_speech():
    # Ask the user to enter the text
    text = input("Enter the text you want to convert to speech: ")

    # Create a gTTS object
    tts = gTTS(text=text, lang='en', slow=False)
    
    ran = random.randint(0, 1000)

    # Save the converted audio to a file
    audio_file = f"output{ran}.mp3"
    tts.save(audio_file)

    # Initialize pygame mixer
    pygame.mixer.init()
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()

    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        continue

if __name__ == "__main__":
    text_to_speech()
