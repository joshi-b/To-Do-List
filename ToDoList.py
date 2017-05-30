from tkinter import *
import os.path

class Todo(Frame):
        
    def __init__(self, root):
        Frame.__init__(self, root)
        root.title('To-Do')
        root.configure(bg='white')

        self.ment = StringVar()
        self.itemlist = []

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
        self.edit_item = Button(self.buttonframe, text='Edit')
        self.clear_button = Button(self.buttonframe, text='Clear All')

        self.add_item.bind('<Button-1>', self.add_button)
        self.del_item.bind('<Button-1>', self.del_button)
        self.edit_item.bind('<Button-1>', self.edit_button)
        self.clear_button.bind('<Button-1>', self.clear_all)

        self.add_item.grid(row=1, ipadx=10)
        self.del_item.grid(row=1, column=1,ipadx=10)
        self.edit_item.grid(row=1, column=2, ipadx=10)
        self.clear_button.grid(row=2, columnspan=3, ipadx=57)

        self.label_name.grid(row=3,sticky=E)
        self.item_name.grid(row=3, column=1)
        self.listbox.grid(row=4, padx=15, pady=5)
        self.scrollbar.grid(row=4, sticky=N+S+E)

        bottombar = Label(root, text='joshi-b  -  2017',bd=1)
        bottombar.grid(row=11, columnspan=5, sticky=E+W)

        if os.path.exists('to-do-items.txt'):
            self.load_data()
        else:
            self.file.open('to-do-items.txt', 'w')

        self.file.close()
        return

    def load_data(self):
        self.file = open('to-do-items.txt', 'r')
        self.file.seek(0)

        line = self.file.readline()
        while line != "":
            self.itemlist.append(line)
            line = self.file.readline()
        self.file.close()

        for x in self.itemlist:
            self.listbox.insert(END, x)
        return
    
    def add_button(self, event):
        self.file = open('to-do-items.txt', 'a')
        tasktext = self.ment.get()
    
        if tasktext == "":
            return
        
        self.listbox.insert(END, tasktext)
        self.itemlist.append(tasktext)
        self.file.write(str(tasktext) + '\n')
    
        self.item_name.delete(0, 'end')

        self.file.close()
        return

    def del_button(self, event):
        self.file = open('to-do-items.txt', 'w+')
        
        item_num = self.listbox.curselection()
        self.listbox.delete(item_num)
        item_num = item_num[0]

        tasktext = self.itemlist[item_num]
        self.itemlist.remove(tasktext)
        
        self.file.truncate()

        for x in self.itemlist:
            self.file.write(x)
        
        self.file.close()
        return
    
    def edit_button(self, event):
        self.file = open('to-do-items.txt', 'w')
        
        self.item_name.delete(0, 'end')
        
        item_num_t = self.listbox.curselection()
        self.listbox.delete(item_num_t)
        
        item_num = item_num_t[0]
        item = self.itemlist[item_num]

        self.itemlist.remove(self.itemlist[item_num])
        
        self.item_name.insert(0, item)

        for x in self.itemlist:
            self.file.write(x)

        self.file.close()
        return

    def clear_all(self, event):
        self.file = open('to-do-items.txt', 'w')
        self.listbox.delete(0, END)
        self.itemlist = []

        self.file.truncate()
        self.file.close()
        return
    
if __name__ == '__main__':
    root = Tk()
    app = Todo(root)
    app.mainloop()
