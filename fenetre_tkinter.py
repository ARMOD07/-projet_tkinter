from tkinter import *
import webbrowser
 

def open_chanel():
    webbrowser.open_new("https://www.youtube.com/")
    pass
 
#cree un fenetre
window= Tk()
# Création de la fenêtre principale

# Définit le titre de la fenêtre
window.title("Mon application")
# Définit la taille initiale de la fenêtre
window.geometry("600x500")

# Définit la taille minimale de la fenêtre
window.minsize(480,360)

# Définit la couleur de fond de la fenêtre
window.config(background='#41B67F')

# Crée un cadre
frame=Frame(window,bg='#41B67F')

#ajouter un text
text=Label(window, text="Binvenue",font=("Courier",40), bg='white',background='#41B67F')
text.pack(expand=YES)

#ajouter un second text:
text2=Label(window, text="C'est Amira MOHAMMEDI",font=("Courier",40), bg='white',background='#41B67F')
text2.pack(expand=YES)

#AJouter un 1 er button:
buton=Button(frame,text="ouvrir ytb",font=("Courier",25),bg='white',fg='#41B67F',command=open_chanel)
buton.pack()
# Pack le cadre
frame.pack()

# Affiche la fenêtre
window.mainloop()

