import tkinter 
from tkinter.font import Font
import requests

# creating the api and getting data for quiz 

response = requests.get("https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=boolean")
data = response.json()

questions =[]
answer=[]
for x in range(0,9):
 t =data["results"][x]["question"]
 questions.append(t)
 z =data["results"][x]["correct_answer"]
 answer.append(z)







# creating the basic widow 
root = tkinter.Tk()
root.title("Quiz app game")
root.maxsize(900,600)
root.minsize(900,600)
photo = tkinter.PhotoImage(file="img1.png")
canvas = tkinter.Canvas(width=900 , height=600,)
canvas.create_image(450,300,image=photo)
canvas.place(x=0,y=0)



# creating the grid 
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
root.rowconfigure(0,weight=1)
root.rowconfigure(1,weight=1)



# creating the score 
score = 0

# creating the check functions and loop 


# creting the text box

x = 0
my_font = Font(size=10)

  
def showquestion(x):
 if x ==9:
  scorebox = tkinter.Label(height=9,width=40,text=f"your final score is {score}",background="#fff6cf",font=my_font)
  scorebox.grid(row=0,column=0,sticky='s',columnspan=2)
  
 else: 
   
   textbox = tkinter.Label(height=9,width=40,text=questions[x],background="#fff6cf",font=my_font)
   textbox.grid(row=0,column=0,sticky="s",columnspan=2)

 
def nextquestion():
  global x
  x = x+1
  showquestion(x)



def checktrue():
    global score
    print(score)
    if data["results"][x]["correct_answer"] == "True" :
     score = score + 1 
def checkfalse():
    global score
    print(score)
    if data["results"][x]["correct_answer"] == "False":
     score = score + 1 
     
# creating the buttons 


nxtbtn = tkinter.Button(root,height=10,width=20,background="yellow",text="next",fg="black",command=nextquestion)
nxtbtn.grid(row=1,column=0,sticky="s",columnspan=2)
wrbtn = tkinter.Button(root,height=10,width=20,background="red2",text="False",fg="white",command=checkfalse)
wrbtn.grid(row=1,column=0,sticky="ws")
ribtn = tkinter.Button(root,height=10,width=20,background="green2", text="True",fg="white",command=checktrue)
ribtn.grid(row=1,column=1,sticky="es")
print(score)
root.mainloop()
