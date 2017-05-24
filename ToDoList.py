from tkinter import *

class Todo(Frame):
        
    def __init__(self, root):
        Frame.__init__(self, root)
        root.title('To-Do')
        root.configure(bg='white')

        self.ment = StringVar()

        self.buttonframe = Frame(root,bg='white')
        self.buttonframe.grid(columnspan=3, padx=20, pady=10)

        self.formframe = Frame(root)
        self.formframe.grid(row=2, columnspan=3)

        self.displaylist = Frame(root, bg='white')
        self.displaylist.grid(row=3, pady=10, padx=(10,20))

        self.label_name = Label(self.formframe, text='Name :', bg='white')
        self.item_name = Entry(self.formframe, textvariable=self.ment)
        
        self.scrollbar = Scrollbar(self.displaylist)
        self.listbox = Listbox(self.displaylist, selectmode=SINGLE, bd=0, width=30, yscrollcommand=self.scrollbar.set)  
        self.scrollbar.config(command=self.listbox.yview)
        
        self.add_item = Button(self.buttonframe, text='Add')
        self.del_item = Button(self.buttonframe, text='Delete')
        self.clear_button = Button(self.buttonframe, text='Clear All')

        self.add_item.bind('<Button-1>', self.add_button)
        self.del_item.bind('<Button-1>', self.del_button)
        self.clear_button.bind('<Button-1>', self.clear_all)

        self.add_item.grid(row=1, ipadx=10)
        self.del_item.grid(row=1, column=1,ipadx=10)
        self.clear_button.grid(row=1, column=2, ipadx=10)

        self.label_name.grid(row=2,sticky=E)
        self.item_name.grid(row=2, column=1)
        self.listbox.grid(row=3, padx=15, pady=5)
        self.scrollbar.grid(row=3, sticky=N+S+E)

        bottombar = Label(root, text='JoshiB  -  2017',bd=1)
        bottombar.grid(row=11, columnspan=5, sticky=E+W)
        return    
    
    def add_button(self, event):
        tasktext = self.ment.get()
        self.listbox.insert(END, tasktext)
        return

    def del_button(self, event):
        item = self.listbox.curselection()
        self.listbox.delete(item)
        return

    def clear_all(self, event):
        self.listbox.delete(0, END)
        return
    
if __name__ == '__main__':
    root = Tk()
    app = Todo(root)
    app.mainloop()
