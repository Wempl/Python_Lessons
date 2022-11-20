from tkinter import *
from tkinter import messagebox
root = Tk()

def btn_click():
    login = loginInput.get()
    password = passField.get()

    info_str = f'Данные: {str(login)}, {str(password)}'
    messagebox.showinfo(title='Название', message=info_str)

    #Окно с ошибкой 
    messagebox.showerror(title='', message='Error always!!!!!!!!!')




root ['bg'] = '#fafafa'
root.title('Название программы')
root.wm_attributes('-alpha', 0.7)
root.geometry('300x250')

root.resizable(width=False, height=False)

canvas = Canvas(root, height=300, width=250)
canvas.pack()

frame = Frame(root, bg='red')
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)

title = Label(frame, text='Текст подсказка', bg='gray', font=40)
title.pack()
btn = Button(frame, text='Кнопка', bg='yellow', command=btn_click)
btn.pack()

loginInput = Entry(frame, bg='white')
loginInput.pack()

passField = Entry(frame, bg='white', show='*')
passField.pack()
root.mainloop() 