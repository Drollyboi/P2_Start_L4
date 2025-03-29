import tkinter
from fileinput import close
from tkinter import colorchooser



window = tkinter.Tk()
window.title("colorchooser")
window.geometry("300x200")

# label maken
label = tkinter.Label(window, text="Welkom bij de kleurenkiezer!")
label.pack()

# Functie om tekst van label aan te passen
def kies_kleur():
    kleur = colorchooser.askcolor()[1]
    window.config(bg=kleur)
# Knop aanmaken
button = tkinter.Button(window, text="Kleurenkiezer!", command=kies_kleur)
button.pack()

window.mainloop()