Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
... print("Chatbot : I am your chatbot how can i help you")
... print("Type bye to end the Chatbot")
... hii=["Hello ","yes i am here","Welcome to chatbot"]
... how_are_you=["I am fine ","I am a code ","but i am fine","Almost fine","by gods grace fine"]
... bye=["Byee","Nice to meet you","Take care","Every moment is  memorable to  me"]
... default_question=["Can you please tell me again ","Sorry i cant understand","I cannnot answer the question  you asked"]
... 
... while True:
... 	user=input("You :").lower()
... 	if user=="hii" or user=="hello":
... 		print("Chatbot :",random.choice(hii))
... 	elif user=="how_are_you" or user=="how_r_u":
... 		print("Chatbot :",random.choice(how_are_you))
... 	elif user=="name": 
... 		print("Chatbot : My name is Personal robot")
... 	elif user=="age":
... 		print("Chatbot : I cant tell my age")
... 	elif user=="creator":
... 		print("Chatbot : I was created by python")
... 	elif user=="bye" or user=="byee":
... 		print("Chatbot :",random.choice(bye))
... 		break
... 	else:
