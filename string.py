price = 49.99
discount = 0.15
discounted_price = price * (1-discount)
message = f"the discounted price is Rs. {discounted_price: .5f}" #5 decimals
print(message)

import speech_recognition as sr

recognizer = sr.Recognizer()

def listen_for_command():
    with sr.Microphone() as source:
        print("Listening for commands...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
        except sr.RequestError:
            print("Sorry, there was an issue with the service.")
    
listen_for_command()
