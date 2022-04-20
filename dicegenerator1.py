from tkinter import*
import tkinter as tk1
import random
import os
#import pygame


window= tk1.Tk()
window.title("nopan vieritys")
window.geometry('500x400')

l = tk1.Label(window, bg="white", fg="black", width=50, text="Noppan numero",borderwidth=2, relief="groove")
l.pack()
d=tk1.Label(window, fg="black", bg="lightblue", width=50, text=" ",  borderwidth=3, relief="groove")
d.pack()
k=tk1.Entry(window, fg="black", bg="lightblue", width=30, text="insert number: ", borderwidth=3, relief="groove")
k.insert(0, "Noppan määrä:")
k.pack()

# pygame.mixer.init()

def print_dice(num): 
    from_k=k.get()
    numerot=[]
    nopat=[3,4,6,8,10,12,20]
#     pygame.mixer.music.load("audio/MOREDICE.wav")
#     pygame.mixer.music.play(loops=0)
    try:
        for x in range (int(from_k)):
            luku=random.randint(1,nopat[num])
            numerot.append(luku)


#tehda maximi label:if luku==nopat[num]:
#                   numerot.append(luku)
            
        t=""
        for y in numerot :
            t+=str(y)+","
        l.config(text= t)
        d.config(text="Olit heittänyt noppaa D"+ str(nopat[num]))
    except:
        l.config(text="numero: " +str(nopat[num]))
            
        
b =tk1.Button(window, text= 'd3', command=lambda:print_dice(0))
b.pack()
x =tk1.Button(window, text= 'd4', command=lambda:print_dice(1))
x.pack()
s=tk1.Button(window, text= 'd6', command=lambda:print_dice(2))
s.pack()
m=tk1.Button(window, text='d8', command=lambda:print_dice(3))
m.pack()
r=tk1.Button(window, text= 'd10', command=lambda:print_dice(4))
r.pack()
t=tk1.Button(window, text='d12', command=lambda:print_dice(5))
t.pack()
u=tk1.Button(window, text='d20', command=lambda:print_dice(6))
u.pack()

window.mainloop()