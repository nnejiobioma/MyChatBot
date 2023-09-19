
#Import tkinter(This is used for the GUI interface)
from tkinter import *

#Click function select
def select(event):
    b=event.widget
    value=b['text']

    for i in range(6):
        if value==correct_answers[i]:
            questionArea.delete(1.0,END)
            questionArea.insert(END,questions[i+1])

            answerOptionButtonA.config(text=first_option[i+1])
            answerOptionButtonB.config(text=second_option[i+1])
            answerOptionButtonC.config(text=third_option[i+1])
            answerOptionButtonD.config(text=fourth_option[i+1])
            #adding prices label
            priceLabel.config(image=priceImages[i])

#creating pop up window on another window with that help of Toplevel
        else:
            root1=Toplevel()
            root1.config(bg='black')
            root1.geometry('500x400+140+30')
            root1.title('You won 0 pound')
            imgLabel=Label(root1,image=centerImage,bd=0)
            imgLabel.pack()

            root1.mainloop()
            break



#QUESTIONS
questions = [
    "Which component of a computer is responsible for storing data permanently?",
    "Which of the following is a type of software?",
    "Which of the following is not an input device?",
    "Which device is used to input data into a computer?"
    ]

first_option = [
    "RAM",
    "Mouse",
    "Monitor",
    "Monitor"
    ]

second_option = [
    "CPU",
    "Keyboard",
    "Scanner",
    "Printer"
    ]

third_option = [
    "Hard Disk",
    "MS Office",
    "Mouse",
    "Keyboard"
    ]

fourth_option = [
    "CD-ROM",
    "Monitor",
    "Joystick",
    "Speaker"
    ]
correct_answers = [
    "Hard Disk",
    "MS Office",
    "Monitor",
    "Keyboard"
    ]


#call tkinter
root=Tk()

#method o add dimeters
root.geometry('1270x650+0+0')

#Edits or modifies title
root.title('QuizGAME by ReactJav')

#provide background color
root.config(bg='black')

#--------------------------------------------

#slpit frame
leftframe=Frame(root,
                bg='black',
                padx=90)
leftframe.grid(row=0,column=0)

topFrame=Frame(leftframe,
               bg='black',
               pady=15)
topFrame.grid()

#------------
#adding image to top frame
#import image
image50=PhotoImage(file='QuizGAME/assets/50-50.png')

#create button to add th 50-50 image
lifeline50Button=Button(topFrame,
                        image=image50,bg='black',
                        bd=0,
                        activebackground='black',
                        width=180,
                        height=80)
lifeline50Button.grid(row=0,column=0)

#creating audience image
imageaudience=PhotoImage(file='QuizGAME/assets/audiencePole.png')

#creating button for audience image
lifelineaudience=Button(topFrame,
                        image=imageaudience,
                        bg='black',
                        bd=0,
                        activebackground='black',
                        width=180,
                        height=80)
lifelineaudience.grid(row=0,column=1)

#create phone a friend button
#creating phone a friend image
imagephonefriend=PhotoImage(file='QuizGAME/assets/phoneAFriend.png')

#creating button for audience image
lifelinephonefriend=Button(topFrame,
                           image=imagephonefriend,
                           bg='black',
                           bd=0,
                           activebackground='black',
                           width=180,
                           height=80)
lifelinephonefriend.grid(row=0,column=3)

#-------------
#center frame creation
centerFrame=Frame(leftframe,
                  bg='black',
                  pady=15)
centerFrame.grid(row=1,column=0)

#------------------------------
#ADDING IMAGE TO CENTER RAME
centerImage=PhotoImage(file='QuizGAME/assets/center.png')

#since the center imge will not be clickable "Label" was used
logoImage=Label(centerFrame,
                image=centerImage,
                bg='black',
                width=300,
                height=200)
logoImage.grid(row=0,column=0)
#-----------------------------
#BOTTOM FRAME

bottomFrame=Frame(leftframe)
bottomFrame.grid(row=2,column=0)

#Adding image to bottom from
layoutImage=PhotoImage(file='QuizGAME/assets/lay.png')

#creating button for audience image
layoutLabel=Button(bottomFrame,
                           image=layoutImage,
                           bg='black',
                           bd=0)
layoutLabel.grid(row=0,column=3)

#---------------------------------------------

#RIGHT FRAME
rightframe=Frame(root,
                 bg='black',
                 pady=25,
                 padx=50)
rightframe.grid(row=0,column=1)

#ADDING IMAGE TO RIGHT FRAME
priceImage=PhotoImage(file='QuizGAME/assets/Picture0.png')
priceImage1=PhotoImage(file='QuizGAME/assets/Picture1.png')
priceImage2=PhotoImage(file='QuizGAME/assets/Picture2.png')
priceImage3=PhotoImage(file='QuizGAME/assets/Picture3.png')
priceImage4=PhotoImage(file='QuizGAME/assets/Picture4.png')
priceImage5=PhotoImage(file='QuizGAME/assets/Picture5.png')
priceImage6=PhotoImage(file='QuizGAME/assets/Picture6.png')
priceImage7=PhotoImage(file='QuizGAME/assets/Picture7.png')
priceImage8=PhotoImage(file='QuizGAME/assets/Picture8.png')
priceImage9=PhotoImage(file='QuizGAME/assets/Picture9.png')
priceImage10=PhotoImage(file='QuizGAME/assets/Picture10.png')
priceImage11=PhotoImage(file='QuizGAME/assets/Picture11.png')
priceImage12=PhotoImage(file='QuizGAME/assets/Picture12.png')
priceImage13=PhotoImage(file='QuizGAME/assets/Picture13.png')
priceImage14=PhotoImage(file='QuizGAME/assets/Picture14.png')
priceImage15=PhotoImage(file='QuizGAME/assets/Picture15.png')

#Object list variable creation for price images

priceImages = [
    priceImage1,
    priceImage2,
    priceImage3,
    priceImage4,
    priceImage5,
    priceImage6,
    priceImage7,
    priceImage8,    
    priceImage9,    
    priceImage10,
    priceImage11,
    priceImage12,
    priceImage13,
    priceImage14,
    priceImage15
]

#adding label to image
priceLabel=Label(rightframe,
                 image=priceImage,
                 bg='black')
priceLabel.grid(row=0,column=0)

#--------------------------------------------
#CREATING QUESTION AREA
questionArea=Text(bottomFrame,
                  font=('arial',18,'bold'),
                  width=34,height=2,
                  wrap='word',
                  bg='black',
                  fg='white',
                  bd=0)
questionArea.place(x=70,y=10)

#INSERTING QUESTION TO QUESTION AREA
questionArea.insert(END,questions[0])


#CREATION ANSWER OPTION
#Option A
answerOptionButtonA=Button(bottomFrame,text=first_option[0],
                          bg='black',
                          fg='white',
                          font=('arial',18,'bold'),
                           bd=0,
                           activebackground='black',
                           activeforeground='white',
                           cursor='hand2',
                           )
answerOptionButtonA.place(x=100,y=100)

#Option B
answerOptionButtonB=Button(bottomFrame,text=second_option[0],
                          bg='black',
                          fg='white',
                          font=('arial',18,'bold'),
                           bd=0,
                           activebackground='black',
                           activeforeground='white',
                           cursor='hand2')
answerOptionButtonB.place(x=370,y=100)

#option C
answerOptionButtonC=Button(bottomFrame,text=third_option[0],
                          bg='black',
                          fg='white',
                          font=('arial',18,'bold'),
                           bd=0,
                           activebackground='black',
                           activeforeground='white',
                           cursor='hand2')
answerOptionButtonC.place(x=100,y=180)

#option D
answerOptionButtonD=Button(bottomFrame,text=fourth_option[0],
                          bg='black',
                          fg='white',
                          font=('arial',18,'bold'),
                           bd=0,
                           activebackground='black',
                           activeforeground='white',
                           cursor='hand2')
answerOptionButtonD.place(x=370,y=180)

#BINDING OPTION BUTTONS
answerOptionButtonA.bind('<Button-1>',select)
answerOptionButtonB.bind('<Button-1>',select)
answerOptionButtonC.bind('<Button-1>',select)
answerOptionButtonD.bind('<Button-1>',select)


#CREATING OPTION LABEL
#labelA
labelOptionA=Label(bottomFrame,text='A:',
                   bg='black',
                   fg='white',
                   font=('arial',18,'bold'),
                   bd=0,
                   )
labelOptionA.place(x=60,y=110)

#label B
labelOptionB=Label(bottomFrame,text='B:',
                   bg='black',
                   fg='white',
                   font=('arial',18,'bold'),
                   bd=0,
                   )
labelOptionB.place(x=330,y=110)

#label C
labelOptionC=Label(bottomFrame,text='C:',
                   bg='black',
                   fg='white',
                   font=('arial',18,'bold'),
                   bd=0,
                   )
labelOptionC.place(x=60,y=190)

#label D
labelOptionD=Label(bottomFrame,text='D:',
                   bg='black',
                   fg='white',
                   font=('arial',18,'bold'),
                   bd=0,
                   )
labelOptionD.place(x=330,y=190)





#Helps the GUI interface to remain visible
root.mainloop()
