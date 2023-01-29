import tkinter
from tkinter import messagebox

root = tkinter.Tk()
root.withdraw()

count = 0 

msg_box = messagebox.showwarning("É amigo, você se lascou", "Acabas de ser Hackeado")

if msg_box == 'ok':
    msg_box = messagebox.showwarning("UM MOMENTO AMIGO!!", 'Para sair do Hack, é preciso que responda as questões abaixo com bastante atenção')

if msg_box == 'ok':
    msg_box = messagebox.askquestion("...", "jdjaddaa")

while msg_box == 'no':
    count += 1
    msg_box = messagebox.askquestion("...", "skdnadadnwidin")
    if (count == 5):
        msg_box = messagebox.showerror("Praga")
        break

if msg_box == 'yes':
    msg_box = messagebox.showinfo("Muito bem")