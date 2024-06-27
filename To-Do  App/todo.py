from tkinter import *
from tkinter.messagebox import *
from sqlite3 import *

root = Tk()
root.title("My To-Do List")
root.geometry("1000x600+50+50")
root.configure(bg="light blue")
f = ("Times New Roman", 50, "bold")
f1 = ("Times New Roman", 25, "bold")
f2 = ("Times New Roman", 25)
f3 = ("Times New Roman", 10)

label1 = Label(root, text="To-Do List", font=f)
label1.place(x=350, y=20)

lab1_create = Label(root, text="Enter the Task: ", font=f1)
lab1_create.place(x=350, y=120)
ent_create = Entry(root, font=f2)
ent_create.place(x=350, y=160)

listbox = Listbox(root, font=f2, width=40, height=10)
listbox.place(x=350, y=280)

def refresh_tasks():
    listbox.delete(0, END)
    con = None
    try:
        con = connect("todolist.db")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM todo")
        rows = cursor.fetchall()
        for row in rows:
            listbox.insert(END, row[0])
    except Exception as e:
        showerror("Issue", e)
    finally:
        if con is not None:
            con.close()

def save():
    con = None
    try:
        con = connect("todolist.db")
        cursor = con.cursor()
        sql = "INSERT INTO todo (task) VALUES (?)"
        task = ent_create.get()
        cursor.execute(sql, (task,))
        con.commit()
        showinfo("Success", "Task added successfully")
        ent_create.delete(0, END)
        refresh_tasks()
    except Exception as e:
        if con is not None:
            con.rollback()
        showerror("Issue", e)
    finally:
        if con is not None:
            con.close()

def delete_task():
    con = None
    try:
        con = connect("todolist.db")
        cursor = con.cursor()
        selected_task = listbox.get(ACTIVE)
        cursor.execute("DELETE FROM todo WHERE task=?", (selected_task,))
        con.commit()
        showinfo("Success", "Task deleted successfully")
        refresh_tasks()
    except Exception as e:
        if con is not None:
            con.rollback()
        showerror("Issue", e)
    finally:
        if con is not None:
            con.close()

btn_add = Button(root, text="Add Task", width=20, font=f3, command=save)
btn_add.place(x=350, y=220)
btn_delete = Button(root, text="Delete Task", width=20, font=f3, command=delete_task)
btn_delete.place(x=350, y=250)

refresh_tasks()

root.mainloop()