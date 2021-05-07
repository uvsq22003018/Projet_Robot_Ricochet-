#########################################
# groupe MPCI 5
# Riyad KENZI
# Yanis MOHELLIBI
# Dany TANG
#Florian GONDRY
#https://github.com/Danyt13/Projet_Robot_Ricochet-
########################################


import tkinter as tk 
import random as rd


c = 37.625                          
n = 16                           
cases = []  
COTE = c*n+2                     

# Création des murs 
def mur1 ():
    for n in range(1):    
        a = rd.randint(1,13)
        if a == 1 :
            canvas.create_line((77,0),(77,40),fill="black",width= 4)
        if a == 2 :
            canvas.create_line((77+c,0),(77+c,40),fill="black",width= 4)
        if a == 3 :
            canvas.create_line((77+2*c,0),(77+2*c,40),fill="black",width= 4)
        if a == 4 :
            canvas.create_line((77+(3*c),0),(77+(3*c),40),fill="black",width= 4)
        if a == 5 :
            canvas.create_line((77+(4*c),0),(77+(4*c),40),fill="black",width= 4)
        if a == 6 :
            canvas.create_line((77+(5*c),0),(77+(5*c),40),fill="black",width= 4)
        if a == 7 :
            canvas.create_line((77+(6*c),0),(77+(6*c),40),fill="black",width= 4)
        if a == 8 :
            canvas.create_line((77+(7*c),0),(77+(7*c),40),fill="black",width= 4)
        if a == 9 :
            canvas.create_line((77+(8*c),0),(77+(8*c),40),fill="black",width= 4)
        if a == 10 :
            canvas.create_line((77+(9*c),0),(77+(9*c),40),fill="black",width= 4)
        if a == 11 :
            canvas.create_line((77+(10*c),0),(77+(10*c),40),fill="black",width= 4)
        if a == 12 :
            canvas.create_line((77+(11*c),0),(77+(11*c),40),fill="black",width= 4)
        else :
            canvas.create_line((77+(12*c),0),(77+(12*c),40),fill="black",width= 4)

def mur2():
    for n in range(1):    
        a = rd.randint(1,13)
        if a == 1 :
            canvas.create_line((77,566),(77,603),fill="black",width= 4)
        if a == 2 :
            canvas.create_line((77+c,566),(77+c,603),fill="black",width= 4)
        if a == 3 :
            canvas.create_line((77+(2*c),566),(77+(2*c),603),fill="black",width= 4)
        if a == 4 :
            canvas.create_line((77+(3*c),566),(77+(3*c),603),fill="black",width= 4)
        if a == 5 :
            canvas.create_line((77+(4*c),566),(77+(4*c),603),fill="black",width= 4)
        if a == 6 :
            canvas.create_line((77+(5*c),566),(77+(5*c),603),fill="black",width= 4)
        if a == 7 :
            canvas.create_line((77+(6*c),566),(77+(6*c),603),fill="black",width= 4)
        if a == 8 :
            canvas.create_line((77+(7*c),566),(77+(7*c),603),fill="black",width= 4)
        if a == 9 :
            canvas.create_line((77+(8*c),566),(77+(8*c),603),fill="black",width= 4)
        if a == 10 :
            canvas.create_line((77+(9*c),566),(77+(9*c),603),fill="black",width= 4)
        if a == 11 :
            canvas.create_line((77+(10*c),566),(77+(10*c),603),fill="black",width= 4)
        if a == 12 :
            canvas.create_line((77+(11*c),566),(77+(11*c),603),fill="black",width= 4)
        else :
            canvas.create_line((77+(12*c),566),(77+(12*c),603),fill="black",width= 4)

def mur3():
    for n in range(1):
        a = rd.randint(1,13)
        if a == 1 :
            canvas.create_line((0,77),(40,77),fill="black",width= 4)
        if a == 2 :
            canvas.create_line((0,77+c),(40,77+c),fill="black",width= 4)
        if a == 3 :
            canvas.create_line((0,77+(2*c)),(40,77+(2*c)),fill="black",width= 4)
        if a == 4 :
            canvas.create_line((0,77+(3*c)),(40,77+(3*c)),fill="black",width= 4)
        if a == 5 :
            canvas.create_line((0,77+(4*c)),(40,77+(4*c)),fill="black",width= 4)
        if a == 6 :
            canvas.create_line((0,77+(5*c)),(40,77+(5*c)),fill="black",width= 4)
        if a == 7 :
            canvas.create_line((0,77+(6*c)),(40,77+(6*c)),fill="black",width= 4)
        if a == 8 :
            canvas.create_line((0,77+(7*c)),(40,77+(7*c)),fill="black",width= 4)
        if a == 9 :
            canvas.create_line((0,77+(8*c)),(40,77+(8*c)),fill="black",width= 4)
        if a == 10 :
            canvas.create_line((0,77+(9*c)),(40,77+(9*c)),fill="black",width= 4)
        if a == 11 :
            canvas.create_line((0,77+(10*c)),(40,77+(10*c)),fill="black",width= 4)
        if a == 12 :
            canvas.create_line((0,77+(11*c)),(40,77+(11*c)),fill="black",width= 4)
        else :
            canvas.create_line((0,77+(12*c)),(40,77+(12*c)),fill="black",width= 4)

def mur4():
    for n in range(1):
        a = rd.randint(1,13)
        if a == 1 :
            canvas.create_line((565,40+c),(603,40+c),fill="black",width= 4)
        if a == 2 :
            canvas.create_line((565,40+(2*c)),(603,40+(2*c)),fill="black",width= 4)
        if a == 3 :
            canvas.create_line((565,40+(3*c)),(603,40+(3*c)),fill="black",width= 4)
        if a == 4 :
            canvas.create_line((565,40+(4*c)),(603,40+(4*c)),fill="black",width= 4)
        if a == 5 :
            canvas.create_line((565,40+(5*c)),(603,40+(5*c)),fill="black",width= 4)
        if a == 6 :
            canvas.create_line((565,40+(6*c)),(603,40+(6*c)),fill="black",width= 4)
        if a == 7 :
            canvas.create_line((565,40+(7*c)),(603,40+(7*c)),fill="black",width= 4)
        if a == 8 :
            canvas.create_line((565,40+(8*c)),(603,40+(8*c)),fill="black",width= 4)
        if a == 9 :
            canvas.create_line((565,40+(9*c)),(603,40+(9*c)),fill="black",width= 4)
        if a == 10 :
            canvas.create_line((565,40+(10*c)),(603,40+(10*c)),fill="black",width= 4)
        if a == 11 :
            canvas.create_line((565,40+(11*c)),(603,40+(11*c)),fill="black",width= 4)
        if a == 12 :
            canvas.create_line((565,40+(12*c)),(603,40+(12*c)),fill="black",width= 4)
        else :
            canvas.create_line((565,40+(13*c)),(603,40+(13*c)),fill="black",width= 4)


# Création des pions
def Pionblue():
    x = rd.randint(0, 561)
    y = rd.randint(0, 561)
    canvas.create_oval((x, y), (x+c, y+c), fill="blue")


def Pionred():
    x = rd.randint(0, 561)
    y = rd.randint(0, 561)
    canvas.create_oval((x, y), (x+c, y+c), fill="red")

def Pionyellow():
    x = rd.randint(0, 561)
    y = rd.randint(0, 561)
    canvas.create_oval((x, y), (x+c, y+c), fill="yellow")

def Piongreen():
    x = rd.randint(0, 561)
    y = rd.randint(0, 561)
    canvas.create_oval((x, y), (x+c, y+c), fill="green")


fen = tk.Tk()
fen.title('Robot Ricochet')

canvas = tk.Canvas(fen, width = COTE, height = COTE, bg = 'white')
canvas.grid(row = 0, column = 0, columnspan=2, padx=3, pady=3)

for ligne in range(n):          
    transit=[]
    for colonne in range(n):    
        transit.append(canvas.create_rectangle(colonne*c+2, ligne*c+2, (colonne+1)*c+2, (ligne+1)*c+2))
    cases.append(transit)       

canvas.create_rectangle((265, 340), (340, 265), fill="black")

Pionblue(), Pionyellow(), Pionred(), Piongreen()
mur1(), mur2(), mur3(), mur4()



fen.mainloop() 