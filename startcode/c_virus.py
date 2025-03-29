from tkinter import messagebox

message = ['You like my virus?', 'No?', 'How dare you!', 'Now i will steal all your files!!!', 'Oh wait...', 'I cant...', 'Be nice and delete some files :)', 'Then send me to some of your friends :D']

for message in message:
    messagebox.showinfo('Virus alert!', message)