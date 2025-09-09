from tkinter import Label, Entry, Button,Tk, messagebox 
window= Tk()
window.title('questao 12')
window.config(padx=10,pady=10)
lbl_idade=Label(text='idade:')
lbl_idade.grid(row=0,column=0)
txt_idade= Entry (width=4)
txt_idade.grid(row=0,column=1)
txt_idade.focus()

window.mainloop ()