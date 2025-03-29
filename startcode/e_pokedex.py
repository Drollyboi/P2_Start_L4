import tkinter
import requests

pokenaam = requests.get(
    url=f"https://pokeapi.com/ditto",
)

window = tkinter.Tk()
window.title("Pokedex")
window.geometry("300x200")

input = tkinter.Entry(window)
label = tkinter.Label(window, text=pokenaam)

label.pack()
input.pack()


window.mainloop()