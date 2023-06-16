from tkinter import *
import string
from random import randint , choice



def gen_password():
    password_min=6
    password_max=12
    all_char=string.ascii_letters + string.punctuation + string.digits
    password= "".join(choice(all_char)for x in range( randint(password_min,password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0,password)





#cree la fenetre
window= Tk()

window.title("Génerateur de Mots passe")
window.geometry("720x480")
#window.iconbitmap("logo.ico")
window.config(background='#4065A4')

#cree frame proncipal
frame=Frame(window,bg='#4065A4')

#creation d'image

width=300
height=300
image=PhotoImage(file="im.png").zoom(35).subsample(32)
canvas= Canvas(window,width=width,height=height,bg='#4065A4',bd=0,highlightthickness=0)
canvas.create_image(width/2,height/2,image=image)
#canvas.pack(expand=YES)
canvas.grid(row=0,column=0,sticky=W)

#cree une sous boite
right_frame=Frame(frame,bg='#4065A4')


#cree le titre:

label_titre=Label(frame,text="mots pass",font=("Helvetica",20),bg='#4065A4',fg='white')
label_titre.grid(row=0,column=1,sticky=W)

#afficher dans la fenetre:
label_titre.pack()


#cree un champ entree
password_entry=Entry(frame,text="mots pass",font=("Helvetica",20),bg='#4065A4',fg='white')
password_entry.pack()

#cree un Boutton:

boutton_password=Button(frame,text="mots pass",font=("Helvetica",20),bg='#4065A4',fg='white',command=gen_password)
boutton_password.pack(fill=X)
#afficher dans la fenetre:
label_titre.pack()

#afficher la frame:
#frame.pack(expand=YES)

frame.grid(row=0, column=1, sticky="nsew")


#creation un barre de menu:
menu_bar=Menu(window)
#cre un premier menu
fil_menu=Menu(menu_bar,tearoff=0)
fil_menu.add_command(label="nouveau",command=gen_password)
fil_menu.add_command(label="quitter",command=window.quit)
menu_bar.add_cascade(label="fichier",menu=fil_menu)


#config fenetre bar
window.config(menu=menu_bar)

#afficher la fenetre:
window.mainloop()