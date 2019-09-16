from tkinter import *

# main function   
#-----------
root = Tk()
#-----------

#head Text
#------------------------------------------
Label(root, text="Fahrenheit converter").pack(ipadx = 5, ipady = 5, side = TOP)
Label(root, text="by Jessica Nicole Voxny404").pack(ipadx = 5, ipady = 5, side =BOTTOM)
Label(root, text="Enter degrees:  ").pack(ipadx = 0, ipady = 0, side = LEFT)
#------------------------------------------

# Fahrenheit converter
#-------------------------------------
def evaluate(event):
    fahrenheit = float(user.get())
    celsius = (fahrenheit-32)*5/9
    res.config(text= round (celsius,2,))
#--------------------------------------

#user entry point
#------------------------------    
user = Entry(root, text="Red")
user.bind("<Return>", evaluate)
user.pack(side = LEFT)
res = Label(root)
res.pack(side = BOTTOM)
#-------------------------------

# text button
#-------------------------------------------------
Label(root, text="Celsius").pack(side = BOTTOM)
#-------------------------------------------------

#Loop to main function
#---------------------
root.mainloop()
#---------------------
#made in Germany by Jessica Nicole Voxny404 
