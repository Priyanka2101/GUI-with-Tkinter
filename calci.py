from tkinter import *
root = Tk()
root.title('Calculator')
scrollbar = Scrollbar(root)


tb = Entry(root,font=('cursive',30,'bold'), fg='purple', bg='pink', justify='center', bd=50).grid(columnspan=4)

b7= Button(root,padx=30,pady=8,bd=8,fg='black',bg='purple',justify='center',font=('cursive',30,'bold'),text='7').grid(row=1,column=0)
b8= Button(root,padx=30,pady=8,bd=8,fg='black',bg='purple',justify='center',font=('cursive',30,'bold'),text='8').grid(row=1,column=1)
b9= Button(root,padx=30,pady=8,bd=8,fg='black',bg='purple',justify='center',font=('cursive',30,'bold'),text='9').grid(row=1,column=2)
bC= Button(root,padx=30,pady=8,bd=8,fg='black',bg='white',justify='center',font=('cursive',30,'bold'),text='C').grid(row=1,column=3)

b4= Button(root,padx=30,pady=8,bd=8,fg='black',bg='purple',justify='center',font=('cursive',30,'bold'),text='4').grid(row=2,column=0)
b5= Button(root,padx=30,pady=8,bd=8,fg='black',bg='purple',justify='center',font=('cursive',30,'bold'),text='5').grid(row=2,column=1)
b6= Button(root,padx=30,pady=8,bd=8,fg='black',bg='purple',justify='center',font=('cursive',30,'bold'),text='6').grid(row=2,column=2)
bplus= Button(root,padx=30,pady=8,bd=8,fg='black',bg='white',justify='center',font=('cursive',30,'bold'),text='+').grid(row=2,column=3)

b1= Button(root,padx=30,pady=8,bd=8,fg='black',bg='purple',justify='center',font=('cursive',30,'bold'),text='1').grid(row=3,column=0)
b2= Button(root,padx=30,pady=8,bd=8,fg='black',bg='purple',justify='center',font=('cursive',30,'bold'),text='2').grid(row=3,column=1)
b3= Button(root,padx=30,pady=8,bd=8,fg='black',bg='purple',justify='center',font=('cursive',30,'bold'),text='3').grid(row=3,column=2)
bminus= Button(root,padx=30,pady=8,bd=8,fg='black',bg='white',justify='center',font=('cursive',30,'bold'),text='-').grid(row=3,column=3)

b0= Button(root,padx=30,pady=8,bd=8,fg='black',bg='purple',justify='center',font=('cursive',30,'bold'),text='0').grid(row=4,column=0)
bdot= Button(root,padx=30,pady=8,bd=8,fg='black',bg='purple',justify='center',font=('cursive',30,'bold'),text='.').grid(row=4,column=1)
bdiv= Button(root,padx=36,pady=8,bd=8,fg='black',bg='purple',justify='center',font=('cursive',30,'bold'),text='/').grid(row=4,column=2)
bmul= Button(root,padx=36,pady=8,bd=8,fg='black',bg='white',justify='center',font=('cursive',30,'bold'),text='*').grid(row=4,column=3)

bequals= Button(root,padx=108,pady=8,bd=5,fg='black',bg='purple',justify='center',font=('cursive',30,'bold'),text='=').grid(row=5,column=0,columnspan=2)
bclose= Button(root,padx=38,pady=8,bd=5,fg='black',bg='white',justify='center',font=('cursive',30,'bold'),text=')').grid(row=5,column=2)
bopen= Button(root,padx=38,pady=8,bd=5,fg='black',bg='white',justify='center',font=('cursive',30,'bold'),text='(').grid(row=5,column=3)

root.mainloop()