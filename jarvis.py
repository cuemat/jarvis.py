print("Task 1")
#What is an A.I. assistant? 
#Can you give me some examples? 
#Have you ever wondered how cool it would be to have your own A.I. assistant? 
#What would you want to make your A.I. assistant do for you? 
#Imagine how easier it would be to make the assistant solve math calculations? 
#Let us create an Assistant who can solve the math problems for you.
#Create a project, do one of the following:
       #Open the link below
           #https://github.com/cuemat/jarvis.py
       #Download the code, take the required help from the teacher.
#Let us install packages in the terminal before importing them into our program

#pip install pttsx3
#It is a text-to-speech conversion library in Python.

#pip install SpeechRecognition==1.2.3 
#Library for performing speech recognition with the Google Speech Recognition API.
#pipwin install pyaudio
#Pyaudio helps us input audio through the microphone.
#PyAudio, you can easily use Python to play and record audio on a variety of platforms.       

#After installing all the packages let us import them.
#Uncomment the following lines
#import pyttsx3
#import speechrecognition as sr

print("Task 2")

#What was the text to speech module called?
#Uncomment the following line to initialise text to speech.
#engine=pyttsx3.init()
#Use engine.say() to let the assistant say whatever you’d want it to.
    engine.say(“Hello”)
#Let us use it to create a function speak
#Each time we call the function our assistant speaks.
#Create a user defined function speak with a parameter “audio”
#“audio” is the message we want the assistant to speak.
#def <function_name(parameter):>
        #What is the variable in which we have initialised text to speech?
        #Let us make the engine say the message we want it to say
        #Uncomment the following line
        #engine.say(audio)
        #We want the assistant to speak the entire statement hence we use the following method.
        #engine.runAndWait()
#Let us call the function.
speak("Any message you'd want")

#Have you understood how to make Jarvis speak? 
#Can you create another function called wish me and make Jarvis wish you?


print("Task 3")

#What is the module used to recognize speech? 
#Create a user defined function takecommand().
#This function would use the module speech recognition.
#def <name of the function>:
#sr.Recognizer will help the assistant recognize the voice
#Uncomment the line below
        #r=sr.Recognizer()
#Command would be our voice
#How do you think the assitant can hear us?
#Let the assistant know that the voice through the microphone is the source.
  #with sr.Microphone() as source:
#Print listening as the assistant is listening now.

#Next step is to record the command and store it in a variable.

#Duration can be any value and is measured in seconds.
#Let us print the recorded audio in case the message was recorded as something else.

#The message is successfully recorded and let us try and recognize the message stored in audio.
#try:
#Print Recognizing as hear the assitant is trying to recognize what is the command

#Let us try and recognize the command stored in audio, and store it in a variable called query

       #print(f”you’ve said {query}”)
#Incase of an exception let us ask the user to repeat the command
#Uncomment the line below
#except Exception as e:
       #print(e)
       #Use speak function to let the user know the assitant has not understood what they've said.
       #return none
       #return “None”


print("Task 4")

#Let us make our assistant do math problems.
#Let us create a function called eval.
#Eval is used to evaluate the problem and solve it.
#How do you think we’ll do it?
#We’ll use if else.

#What do you think op1,oper or op2 is? 
#op1,op2 are operators and oper is operand.
#Let us convert the op1,op2 to integers.

#Let us check the operand using if else statement.
  

print("Task 5")
#In the main function let us call the wishme function
#if __name__=="__main__":
#call wish me funtion
#Let us call the takecommand function 
#We want to call the function each time we run the program and we want the function to be called repeatedly.
#What loop would you use? 

#Let us make our assistant do math problems.
#We need to set an invoke for the task.
#What do you think is an invoke command? 

#What is the variable in which we have stored our command? 
#let us check if the word “solve” is in query.

#Make your assistant ask the math problem to be solved.
#Which function is created for letting the assistant speak.
#Uncomment the line below
       #speak(“What is the math problem  you want me to solve, please use this format 3 plus 3”)
#We are using a specific structure “3 plus 3” or “99 minus 88”
#Let us make sure the operator is in between operands.
#Operators indicate what action or operation to perform. 
#The operands indicate the value.
#Let us now store the command in a variable called “prob”.
#What is the name of the function that takes the command? 
    
#What is the method that splits a string into a list? 

#Let us use the split function to create a list.

#If the problem is 5 plus 5, what would be the list? [Wait for the student to respond].
#Let us call the function eval with the above split method.

#Let us create a command to make the assistant go offline.
#How can we do it? 
#Create an invoke for offline.









