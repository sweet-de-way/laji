import os
import json
import copy
import tkinter as tk 

conversations_mes_data = {
    "content": "",
    "role": "" 
}

conversations_mes = []

conversations = {"messages": conversations_mes, "label": False}

data = []


window = tk.Tk()
window.title('My Window')

frame = tk.Frame(window)
frame.pack(side=tk.LEFT)

frame1 = tk.Frame(window)
frame1.pack()
frame1_t = tk.Frame(frame1)
frame1_t.pack()

frame2 = tk.Frame(window)
frame2.pack()
frame2_t = tk.Frame(frame2)
frame2_t.pack()


frame3 = tk.Frame(window)
frame3.pack(side="right")

var = tk.StringVar()
n = tk.Text(frame)
scroll = tk.Scrollbar(frame, command=n.yview)
n.configure(yscrollcommand=scroll.set)
scroll.pack(side=tk.RIGHT, fill=tk.Y)
n.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

var1 = tk.StringVar()
n1 = tk.Label(frame1, textvariable=var1, bg='green', fg='white', font=('Arial', 12), width=20, height=2)
n1.pack()
var1.set('from')

e1_var = tk.StringVar()
e1 = tk.Listbox(frame1_t, listvariable=e1_var)
e1.pack()

e1_items = []

e1_en = tk.Entry(frame1_t, show=None, font=('Arial', 14))
e1_en.pack()

def e1_func():
    e1.delete(0, tk.END)
    e1_items.append(e1_en.get())
    for n in e1_items:
        e1.insert('end', n)
e1_b = tk.Button(frame1_t, text='添加', width=15, height=2, command=e1_func)
e1_b.pack()


var2 = tk.StringVar()
n2 = tk.Label(frame2, textvariable=var2, bg='green', fg='white', font=('Arial', 12), width=30, height=2)
n2.pack()
var2.set('value')

e2 = tk.Text(frame2_t, show=None, font=('Arial', 14), height=12)
scroll = tk.Scrollbar(frame2_t, command=n.yview)
e2.configure(yscrollcommand=scroll.set)
scroll.pack(side=tk.RIGHT, fill=tk.Y)
e2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


change_kto_var = tk.StringVar()
def change_kto():
    value = change_kto_var.get()
    match value:
        case "True":
            conversations["label"] = True
        case "False":
            conversations["label"] = False
r1 = tk.Radiobutton(frame3, text='True', variable=change_kto_var, value='True', command=change_kto)
r1.pack()
r2 = tk.Radiobutton(frame3, text='False', variable=change_kto_var, value='False', command=change_kto)
r2.pack()

def hit():
    conversations_mes_data["role"] = e1.get(e1.curselection())
    conversations_mes_data["content"] = e2.get("1.0", "end-1c")
    conversations_mes.append(dict(copy.deepcopy(conversations_mes_data)))
    e2.delete("1.0", "end")
    n.delete("1.0", "end")
    n.insert("1.0", "{}".format(conversations))
b = tk.Button(window, text='压入', font=('Arial', 12), width=10, height=1, command=hit)
b.pack()
b.pack(side="right")

def hit1():
    data.append(dict(copy.deepcopy(conversations)))
    conversations_mes.clear()
    e2.delete("1.0", "end")
    n.delete("1.0", "end")
    n.insert("1.0", "{}".format(conversations))
b_new = tk.Button(window, text='新的conversations', font=('Arial', 12), width=15, height=1, command=hit1)
b_new.pack()
b_new.pack(side="right")

def hit2():
    n.delete("1.0", "end")
    n.insert("1.0", "{}".format(data))
b_new = tk.Button(window, text='查看整个data', font=('Arial', 12), width=15, height=1, command=hit2)
b_new.pack()
b_new.pack(side="right")

def hit3():
    base_filename = 'data.json'
    counter = 1
    filename = base_filename
    while os.path.exists(filename):
        filename = f"{os.path.splitext(base_filename)[0]}_{counter}{os.path.splitext(base_filename)[1]}"
        counter += 1
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
b_out = tk.Button(window, text='导出', font=('Arial', 12), width=15, height=1, command=hit3)
b_out.pack()
b_out.pack(side="left")


window.mainloop()
