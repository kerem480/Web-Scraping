import tkinter as tk
from tkinter import ttk

window=tk.Tk()
window.geometry("800x600")

lable=tk.Label(window,text="Team Info System",font="Time 25",fg="Black")
lable.pack()

pw=ttk.Panedwindow(window,orient=tk.HORIZONTAL)
pw.pack(fill=tk.BOTH,expand=True)

frame1=ttk.Frame(pw,width=400,height=300,relief=tk.RIDGE)
frame2=ttk.Frame(pw,width=400,height=300,relief=tk.RIDGE)

pw.add(frame1)
pw.add(frame2)

tabs=ttk.Notebook(window,height=510,width=380)
tabs.place(x=10,y=50)

tab1=ttk.Frame(tabs,width=50,height=50)
tab2=ttk.Frame(tabs,width=50,height=50)

tk.Label(tab1,text="Team Page",font="Ariel 10").pack()
tk.Label(tab2,text="Countries",font="Ariel 10").pack()


tabs.add(tab1,text="Team Info")
tabs.add(tab2,text="Countries")

treeview=ttk.Treeview(tab1)
treeview.place(x=5,y=30)

treeview.insert("","0","item1",text="Real Madrid")
treeview.insert("item1","1","Cristiano Ronaldo",text="Best Player")
treeview.insert("item1","2","6 March 1902",text="Foundation")
treeview.insert("item1","3","Santiago Bernabéu",text="Stadium")
treeview.insert("item1","4","94 Trophies",text="Trophies")

treeview.insert("","1","item2",text="Barcelona")
treeview.insert("item2","5","Lionel Messi",text="Best Player")
treeview.insert("item2","6","29 November 1899",text="Foundation")
treeview.insert("item2","7","Camp Nou",text="Stadium")
treeview.insert("item2","8","74 Trophies",text="Trophies")

treeview.insert("","2","item3",text="Bayern Münich")
treeview.insert("item3","9","Gerd Müller",text="Best Player")
treeview.insert("item3","10","27 February",text="Foundation")
treeview.insert("item3","11","Allianz Arena",text="Stadium")
treeview.insert("item3","12","65 Trophies",text="Trophies")

treeview.insert("","3","item4",text="Liverpool")
treeview.insert("item4","13","Ian Rush",text="Best Player")
treeview.insert("item4","14","3 June 1892",text="Foundation")
treeview.insert("item4","15","Anfield Road",text="Stadium")
treeview.insert("item4","16","73 Trophies",text="Trophies")

treeview.insert("","4","item5",text="Chelsea")
treeview.insert("item5","17","Frank Lampard",text="Best Player")
treeview.insert("item5","18","10 March 1905",text="Foundation")
treeview.insert("item5","19","Stamford Bridge",text="Stadium")
treeview.insert("item5","20","31 Trophies",text="Trophies")

treeview.insert("","5","item6",text="Milan")
treeview.insert("item6","21","Pablo Maldini",text="Best Player")
treeview.insert("item6","22","16 December 1899",text="Foundation")
treeview.insert("item6","23","San Siro",text="Stadium")
treeview.insert("item6","24","52 Trophies",text="Trophies")

treeview.insert("","6","item7",text="İnter")
treeview.insert("item7","25","Javier Zanetti",text="Best Player")
treeview.insert("item7","26","8 March 1908",text="Foundation")
treeview.insert("item7","27","San/Siro",text="Stadium")
treeview.insert("item7","28","42 Trophies",text="Trophies")

treeview.insert("","7","item8",text="Beşiktaş")
treeview.insert("item8","29","Sergen Yalçın",text="Best Player")
treeview.insert("item8","30","19 March 1903",text="Foundation")
treeview.insert("item8","31","Vodafone Park",text="Stadium")
treeview.insert("item8","32","45 Trophies",text="Trophies")


def callBack(event):
    item=treeview.identify("item",event.x,event.y)
    print(item)

treeview.bind("<Double-1>",callBack)


list_box=tk.Listbox(tab2,selectmode=tk.MULTIPLE)

list_box.insert(0,"Spain")
list_box.insert(1,"Germany")
list_box.insert(2,"Italy")
list_box.insert(3,"Turkey")
list_box.insert(4,"Netherlands")
list_box.insert(5,"France")
list_box.insert(6,"Portugal")
list_box.insert(7,"England")
list_box.insert(8,"Russia")

list_box.place(x=5,y=5)


def buttonFunction():
    index_list=list_box.curselection()
    print(index_list)
    for each in index_list:
        print(list_box.get(each))

button2=tk.Button(tab2,text="button",command=buttonFunction)
button2.place(x=140,y=40)


tk.mainloop()