import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Function to listen and recognize speech in real-time
def listen_and_recognize():
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")

        # Infinite loop for real-time typing
        while True:
            try:
                print("Say something:")
                audio = recognizer.listen(source)
                print("Recognizing...")

                # Recognizing the speech and printing it
                text = recognizer.recognize_google(audio)
                print(f"You said: {text}")
            except sr.UnknownValueError:
                print("Sorry, I did not understand that.")
            except sr.RequestError:
                print("Could not request results from Google Speech Recognition service.")

# Run the function
if __name__ == "__main__":
    listen_and_recognize()
