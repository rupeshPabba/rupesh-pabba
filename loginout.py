import tkinter as tk
import time
root=tk.Tk()

def login():
    global t1,name_info,id_info
    name_info=E1.get()
    id_info=E2.get()
    t1=time.time()
    print(name_info)
    print(id_info)


    
def logout():
    global t2
    t2=time.time()
    f=t2-t1
    f=f/3600
    print(f,end=" ")
    print("hr")
    
    


name_var=tk.StringVar()
pass_var=tk.StringVar()
l1=tk.Label(root,text="NAME",fg="black")
l1.grid(row=1,column=1)
l2=tk.Label(root,text="ID",fg="black")
l2.grid(row=2,column=1)
E1=tk.Entry(root,textvariable=name_var)
E1.grid(row=1,column=2)
E2=tk.Entry(root,textvariable=pass_var)
E2.grid(row=2,column=2)
b1=tk.Button(root,text="LOGIN",fg="white",bg="blue",command=login)
b1.grid(row=4,column=1)
b2=tk.Button(root,text="LOGOUT",fg="white",bg="blue",command=logout)
b2.grid(row=4,column=2)
root.mainloop()
