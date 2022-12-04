from tkinter import *
from tkinter import messagebox
import tkinter

logins = ["user0", "user1"]
passwords = ["pass0", "pass1"]

#функций которые должны производится при вводе логина и пароля
def messagebox1():
    messagebox.showinfo("Внимание!", "Данные пересохранены!")


def messagebox0():
    messagebox.showinfo()



#действие очищающие окно
def state_score():
    destroy_object =[t1, log, regist]
    for object_name in destroy_object:
        object_name.destroy()



#создает окно ввода логина и пароля 
def far():
    state_score()
    def enter():
        if login not in logins:
            messagebox1()
        else:
            messagebox0()
        if passwords[logins.index(login)] != password:
            messagebox1()

    login = tkinter.StringVar()
    password = tkinter.StringVar()

    login_label = Label(text="Дата - ")
    password_label = Label(text="Время - ")
    passwordы_label4 = Label(text="Слушатели - ")
    passwordыы_label3 = Label(text="Преподаватель - ")
    passwordыыы_label2 = Label(text="Сумма сбора - ")
    passwordыыыы_label1 = Label(text="Ганарар - ")

    message_button = Button(text="Создать")
    message_button.grid(row=2, column=4, padx=5, pady=5, sticky="e")
    message_button.config(command=enter)

    login_label.grid(row=0, column=0, sticky="w")
    password_label.grid(row=1, column=0, sticky="w")
    passwordы_label4.grid(row=2, column=0, sticky="w")
    passwordыы_label3.grid(row=3, column=0, sticky="w")
    passwordыыы_label2.grid(row=4, column=0, sticky="w")
    passwordыыыы_label1.grid(row=5, column=0, sticky="w")

    login_entry = Entry(textvariable=login)
    password_entry = Entry(textvariable=password_label)
    password_entry1 = Entry(textvariable=passwordы_label4)
    password_entry2 = Entry(textvariable=passwordыы_label3)
    password_entry3 = Entry(textvariable=passwordыыы_label2)
    password_entry4 = Entry(textvariable=passwordыыыы_label1)

    login_entry.grid(row=0, column=1, padx=5, pady=5)
    password_entry.grid(row=1, column=1, padx=5, pady=5)
    password_entry1.grid(row=2, column=1, padx=5, pady=5)
    password_entry2.grid(row=3, column=1, padx=5, pady=5)
    password_entry3.grid(row=4, column=1, padx=5, pady=5)
    password_entry4.grid(row=5, column=1, padx=5, pady=5)

    

#первоначальное окно 
root = Tk()
root.title("Предприятие 2022")
root.geometry("500x200+600+300")

t1 = Label(text="Перспективная версия предприятия",fg='white', bg="blue")
t1.config(font=('Times', 25))
t1.pack()



log = Button(text="Мероприятия", background="#555", foreground="#ccc", padx="15", pady="7", font="13")
log.config(command=far)
log.pack()



regist = Button(text="                                                                                                                                                                         ", background="#555", foreground="#ccc", font="20", pady="10", padx="10")
regist.config(command=state_score)
regist.pack()



root.mainloop()