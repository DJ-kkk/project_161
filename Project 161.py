from tkinter import *
root =  Tk()

root.title("Health diagnostic center ")
root.geometry("1600x1000")




question1_radioButton=StringVar(value="0")
                                
question1_r1=Radiobutton(root, text = "yes", variable=question1_radioButton, value="yes",bg = "salmon")
question1_r1.place(relx=0.5 ,ewly=0.25 , anchor = CENTER)



if question1_radioButton.get()=="yes":
    score = score+10
    print(score)
    



if score <= 10:
    messagebox.showinfo("Report","You dont need to visit a doctor")
    



elif score> 10 and score <=30:
    messagebox.showinfo("Report","You might perhaps have to visit a doctor")
    
    
    
    
else :
    messagebox.showinfo("Report","I strongly advise you visit  a doctro")