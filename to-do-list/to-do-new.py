import tkinter
import tkinter.messagebox
import pickle

root=tkinter.Tk()
root.title('To-Do List')

def add_task():
	task=entry_task.get()
	if task !='':
		listbox_tasks.insert(tkinter.END,task)
		entry_task.delete(0,tkinter.END)
	else:
		tkinter.messagebox.showwarning(title='Warning!', message='You must enter a task.')

def delete_task():
	try:
		task_index = listbox_tasks.curselection()[0]
		listbox_tasks.delete(task_index)
	except:
		tkinter.messagebox.showwarning(title='Warning!', message='You must select a task.')
		

def load_tasks(n):
	try:
		tasks= pickle.load(open('{}.docx'.format(n),'rb+'))
		for task in tasks:
			listbox_tasks.insert(tkinter.END, task)
	except:
		tkinter.messagebox.showwarning(title='Warning!', message='Cannot find tasks.dat')
				

def save_tasks():
	tasks= listbox_tasks.get(0,listbox_tasks.size())
	listbox_tasks.delete(0, tkinter.END)
	pickle.dump(tasks, open('tasks.docx','rb+'))



# create GUI
def ml(file_name,load_val):
    frame_tasks= tkinter.Frame(root)
    frame_tasks.pack()

    listbox_tasks= tkinter.Listbox(frame_tasks,height=10,width=50,bg='grey')
    listbox_tasks.pack(side=tkinter.LEFT)

    scrollbar_tasks= tkinter.Scrollbar(frame_tasks)
    scrollbar_tasks.pack(side= tkinter.RIGHT, fill= tkinter.Y)

    listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
    scrollbar_tasks.config(command=listbox_tasks.yview)

    entry_task= tkinter.Entry(root,width=50)
    entry_task.pack()

    button_add_task=tkinter.Button(root,text='Add task', command=add_task ,bg='blue',fg='white')
    button_add_task.pack()

    button_delete_task=tkinter.Button(root,text='Delete task', width=48, command=delete_task, bg='crimson',fg='white' )
    button_delete_task.pack()

    button_load_tasks=tkinter.Button(root,text='Load tasks', width=48, command=load_tasks, bg='green' )
    button_load_tasks.pack()

    if load_val==True:
        load_tasks(file_name)

    button_save_tasks=tkinter.Button(root,text='Save tasks', width=48, command=save_tasks, bg='cyan' )
    button_save_tasks.pack()


def ex_file_name():
    global file_name
    file_name= tkinter.Entry(root,width=50)
    file_name.pack()
    
    
    ok=tkinter.Button(root,text='sub',command=identify)
    ok.pack()
   
def identify():
    global file_name
    name_file=file_name.get()
    if name_file!='':
        print('yes')
        ml(name_file,True)


button_ex=tkinter.Button(root,text='pre-existing',width=50,command=ex_file_name)
button_ex.pack(side=tkinter.LEFT)

button_new=tkinter.Button(root,text='new-file',width=50,command=ml)
button_new.pack(side=tkinter.RIGHT)

root.mainloop()