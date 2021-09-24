import pyttsx3
friend=pyttsx3.init()
#friend.say(" ehy madafucker how are you ?. are you fine???")
for i in range(0,5):
    spech=input()
    friend.say(spech)
    friend.runAndWait()