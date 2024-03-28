import os
import pyttsx3
if __name__ == '__main__':
 print("welcome to robospeaker")
 while True:
  c = input("enter what yu want  to pronounce \n")
  engine = pyttsx3.init()
  engine.say(c)
  engine.runAndWait()
  if c == "q":
   engine.say("bye bye bye friend")
   engine.runAndWait()
   engine = pyttsx3.init()
  break

#
# if __name__ == '__main__':
#     print("welcome to robospeaker")
#     c = input("enter what yu want  to pronounce")
#     command = f"say{c}"
#     os.system(command)