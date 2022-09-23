import speech_recognition 
import pyttsx3
robot_ear =speech_recognition.Recognizer()
engine = pyttsx3.init()   #KHOI TẠO
robot_brain=""

while True:
    with speech_recognition.Microphone() as mic:
        robot_ear.adjust_for_ambient_noise(mic)
        print("robot: I'm Listening")
        audio = robot_ear.listen(mic,timeout=3,phrase_time_limit=3)
    print("Jarver ...")

    try:
        you =robot_ear.recognize_google(audio,language='vi-VN')
    except:
        you =""
    print("you say :"+you)

    if you =="":
        robot_brain ="I can't hear you, try again"
    elif you =="hello":
        robot_brain="hello huy handsome"
    elif "robot" in you:
        robot_brain="Yes sir"
    elif "đi" in you:
        robot_brain="đi mua đồ an thôi"
    elif "Linh" in you:
        robot_brain=" người yêu của ông chủ"
    elif "đói" in you:
        robot_brain =" đi mua đồ ăn đi"
    elif "tạm biệt" in you:
        robot_brain="goodbye sir"
        engine.say(robot_brain)
        engine.runAndWait()
        break
    else:
        robot_brain ="Im fine thank you and you"
    print("robot_brain"+robot_brain)



    engine.say(robot_brain)
    engine.runAndWait()