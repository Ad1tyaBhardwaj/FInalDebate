import gtts
text= input("Enter Text: ")
sound = gtts.gTTS(text,lang="en")
sound.save("Welcome.mp3")