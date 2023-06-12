import tkinter
import tkinter.messagebox
top = tkinter.Tk()
top.geometry('200x100')

input_text = tkinter.StringVar()
input_text.set("Tkinter")

text_field = tkinter.Entry(top, textvariable=input_text)
text_field.pack()

def clicked(event=None):
    message = "Hello "+ input_text.get()
    tkinter.messagebox.showinfo('Greetings', message)

button = tkinter.Button(top, text='Enter', command = clicked)
button = tkinter.Button(top, text="quit", command=close_win)

button.pack()
top.mainloop()