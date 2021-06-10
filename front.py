from tkinter import *
#from tkinter.ttk import *
from tkinter import scrolledtext
from tkinter import Menu

window = Tk()

window.title("SEARCH@gs_ANYTHING HERE")
window.geometry('700x300')

txt = scrolledtext.ScrolledText(window, width=40, height=10)

txt.grid(column=25, row=100)

lbl = Label (window, text="www.GUNJAN.in", font=("Times new Roman", 40))

lbl.grid(column=25, row=25)

txt = Entry(window, width=100)

txt.grid(column=25, row=50)


def clicked():
    lbl.configure(text="Request is Applied  !!",font=("Times new Roman",10))
    lbl.grid(column=10,row=75)

btn = Button(window, text="Gunjan_Search", bg='White', fg='Black',command=clicked)

btn.grid(column=25, row=75)

# Creating a photoimage object to use image 
photo = PhotoImage(file = r"C:\mr\gunu.png") 

# Resizing image to fit on button 
photoimage = photo.subsample(20,20) 

# here, image option is used to 
# set image on button 
# compound option is used to align 
# image on LEFT side of button 
btn2=Button(window, text = 'MIKE', image = photoimage, 
					compound = LEFT) 
btn2.grid(column=50,row=50)
#mainloop() 


menu = Menu(window)

new_item = Menu(menu)
new_item1 = Menu(menu)
new_item2 = Menu(menu)
new_item3 = Menu(menu)

new_item.add_command(label='Images')
new_item.add_separator()
new_item.add_command(label='HIstroy')
new_item.add_separator()
new_item.add_command(label='new_ignotic tab')
new_item.add_separator()
new_item.add_command(label='help')
new_item.add_separator()
new_item.add_command(label='more tools')
new_item.add_separator()
new_item.add_command(label='Zoom - & +')
new_item.add_separator()
new_item.add_command(label='setting')
new_item.add_separator()
new_item.add_command(label='Exit')
new_item.add_separator()
new_item1.add_command(label='version 1.0')
new_item1.add_separator()
new_item2.add_command(label='MY GUNU IMAGE')
new_item2.add_separator()
new_item2.add_command(label='MY GUNU TUBE')
new_item2.add_separator()
new_item2.add_command(label='MPG PROGRAMMING')
new_item2.add_separator()
new_item3.add_command(label='gunjanshrimali1234@gmail.com')
new_item3.add_separator()
new_item3.add_command(label='gunjanshrimali407@gmail.com')
new_item3.add_separator()
new_item3.add_command(label='mpgsite09@gmail.com')

menu.add_cascade(label='Menu', menu=new_item)
menu.add_cascade(label='Gmail', menu=new_item3)
menu.add_cascade(label='GUNJAN APP', menu=new_item2)
menu.add_cascade(label='SIGN UP', menu=new_item1)

window.config(menu=menu)

window.mainloop()
