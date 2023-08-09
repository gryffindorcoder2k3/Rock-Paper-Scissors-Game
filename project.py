# Rock paper scissors game
import random
from tkinter import *
from PIL import Image,ImageTk
w=Tk()

# setting the opening window
w.geometry("800x600+100+50")
w.config(background="green")
w.state("zoomed")
w.title("Rock Paper Scissors")

# Setting scores=0
player_score=0
comp_score=0

player=Label(w,text="Player",font=(20))
player.place(x=300,y=100)
scores=Label(w,text=str(player_score)+" || "+str(comp_score),font=(20))
scores.place(x=600,y=100)
computer=Label(w,text="Computer",font=(20))
computer.place(x=850,y=100)

# function for reset button
def reset():
  global player_score,comp_score
  player_score=0
  comp_score=0
  scores.config(text=str(player_score)+" || "+str(comp_score))

# function for rock button
def rock():
  image2=Image.open("img/rock.png")
  resize_image2=image2.resize((200,200), Image.Resampling.LANCZOS)
  img2= ImageTk.PhotoImage(resize_image2)
  l2=Label(image=img2)
  l2.image=img2
  l2.place(x=250,y=200)
  update_scores(0)

# function for rock button
def paper():
  image1=Image.open("img/paper.png")
  resize_image1=image1.resize((200,200), Image.Resampling.LANCZOS)
  img1= ImageTk.PhotoImage(resize_image1)
  l1=Label(image=img1)
  l1.image=img1
  l1.place(x=250,y=200)
  update_scores(1)

# function for scissors button
def scissors():
  image3=Image.open("img/scissors.png")
  resize_image3=image3.resize((200,200), Image.Resampling.LANCZOS)
  img3= ImageTk.PhotoImage(resize_image3)
  l3=Label(image=img3)
  l3.image=img3
  l3.place(x=250,y=200)
  update_scores(2)

# Function for computer to play rock
def rockComp():
  image2=Image.open("img/rock.png")
  resize_image2=image2.resize((200,200), Image.Resampling.LANCZOS)
  img2= ImageTk.PhotoImage(resize_image2)
  l2=Label(image=img2)
  l2.image=img2
  l2.place(x=800,y=200)

# Function for computer to play paper
def paperComp():
  image1=Image.open("img/paper.png")
  resize_image1=image1.resize((200,200), Image.Resampling.LANCZOS)
  img1= ImageTk.PhotoImage(resize_image1)
  l1=Label(image=img1)
  l1.image=img1
  l1.place(x=800,y=200)

# Function for computer to play scissors
def scissorsComp():
  image3=Image.open("img/scissors.png")
  resize_image3=image3.resize((200,200), Image.Resampling.LANCZOS)
  img3= ImageTk.PhotoImage(resize_image3)
  l3=Label(image=img3)
  l3.image=img3
  l3.place(x=800,y=200)

# Fucntion to player rock,paper or scissors for the computer
def predict():
  pred=random.randint(0,2)
  return pred

# Function updates the score according to the play made by user and computer
def update_scores(user_input):
  global player_score,comp_score
  pred=predict()
  if user_input==0:
    if pred==0:
      rockComp()
      scores.config(text=str(player_score)+" || "+str(comp_score))
    elif pred==1:
      comp_score+=1
      paperComp()
      scores.config(text=str(player_score)+" || "+str(comp_score))
    else:
      player_score+=1
      scissorsComp()
      scores.config(text=str(player_score)+" || "+str(comp_score))
  elif user_input==1:
    if pred==1:
      paperComp()
      scores.config(text=str(player_score)+" || "+str(comp_score))
    elif pred==0:
      player_score+=1
      rockComp()
      scores.config(text=str(player_score)+" || "+str(comp_score))
    else:
      comp_score+=1
      scissorsComp()
      scores.config(text=str(player_score)+" || "+str(comp_score))
  else:
    if pred==2:
      scissorsComp()
      scores.config(text=str(player_score)+" || "+str(comp_score))
    elif pred==0:
      comp_score+=1
      rockComp()
      scores.config(text=str(player_score)+" || "+str(comp_score))
    else:
      player_score+=1
      paperComp()
      scores.config(text=str(player_score)+" || "+str(comp_score))
  
  # If score reaches five the winner is announced
  if(player_score==5):
    l1=Label(w,text="Player Wins!",font=(100),padx=30,pady=30)
    l1.place(x=540,y=0)
    scores.config(text=str(player_score)+" || "+str(comp_score))
    w.after(2000,l1.destroy)
    player_score=0
    comp_score=0
  elif(comp_score==5):
    l1=Label(w,text="Computer Wins!",font=(100),padx=30,pady=30)
    l1.place(x=520,y=0)
    scores.config(text=str(player_score)+" || "+str(comp_score))
    w.after(2000,l1.destroy)
    player_score=0
    comp_score=0

# Code for all the button on screen
r=Button(w,text="Rock",font=(16),bg="white",command=rock)
r.place(x=300,y=500)
p=Button(w,text="Paper",font=(16),bg="white",command=paper)
p.place(x=600,y=500)
s=Button(w,text="Scissors",font=(16),bg="white",command=scissors)
s.place(x=900,y=500)
restart=Button(w,text="Restart",font=(20),bg="white",command=reset)
restart.place(x=580,y=300)

w.mainloop()