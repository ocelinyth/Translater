from tkinter import*
from tkinter import ttk
from methods import MyTranslator


app = Tk()
app.geometry('800x600')
app.title(" ")
app.resizable(0,0)
app.config(bg='black')
app.wm_iconbitmap('iconfortk.ico')

def get():
    s = srcLangs.get()
    t = targetLangs.get()
    message = sourceText.get(1.0,END)
    translator = MyTranslator()
    text = translator.run(txt=message,src=s,dest=t)
    targetText.delete(1.0,END)
    targetText.insert(END,text)

def swap():
    tart=targetText.get(1.0,END)
    srct=sourceText.get(1.0,END)
    s = srcLangs.get()
    t = targetLangs.get()
    srcLangs.set(t)
    targetLangs.set(s)
    sourceText.delete(1.0,END)
    targetText.delete(1.0,END)
    sourceText.insert(END,tart)
    targetText.insert(END,srct)

photo = PhotoImage(file = r"C:\Users\YunusEmreTosun\Documents\Atom\Translater\swap.png")

appname = Label(app,text='SÖZLÜK',font=('arial',20,'bold'),bg='green',fg='white',height=2)
appname.pack(side=TOP,fill=BOTH,pady=0)

version = Label(app,text='beta version',font=('arial',10),bg='green').place(x=700,y=40)

frame  = Frame(app).pack(side=BOTTOM)
sourceText =  Text(frame,font=('arial',10),height=11,wrap=WORD)
sourceText.pack(side=TOP,padx=5,pady=20)

transBtn=Button(frame,text='Çevir',font=('arial',10,'bold'),fg='white',bg='green',activebackground='black',relief=GROOVE,command=get)
transBtn.pack(side=TOP,pady=0)

swapBtn=Button(frame,text='Takas',image=photo,fg='white',bg='green',activebackground='black',relief=GROOVE,command=swap)
swapBtn.pack(side=TOP,pady=5)

langs= MyTranslator().allangs
srcLangs = ttk.Combobox(frame,values=langs,width=10)
srcLangs.place(x=290,y=295)
srcLangs.set(langs[21])

targetLangs = ttk.Combobox(frame,values=langs,width=10)
targetLangs.place(x=427,y=295)
targetLangs.set(langs[96])

targetText =  Text(frame,font=('arial',10),height=11,wrap=WORD)
targetText.pack(side=TOP,padx=5,pady=20)



app.mainloop()
