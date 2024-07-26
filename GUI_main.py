

import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk

##############################################+=============================================================
root = tk.Tk()
root.configure(background="white")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Fake Currency Detection System")

# 43

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('p1.png')
image2 = image2.resize((w, h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)





#
image2 = Image.open('f3.jpg')
image2 = image2.resize((700, 900), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)



lbl = tk.Label(root, text="Fake Currency  Detection System", font=('times', 20,' bold '), height=1, width=30,bg="Black",fg="white")
lbl.place(x=800, y=20)



# label_l1 = tk.Label(root, text="Dental Cavity",font=("Times New Roman", 20, 'italic','bold'),
#                 width=15, height=5)
# label_l1.place(x=750, y=40)

# label_l2= tk.Label(root, text=" Detection System",font=("Times New Roman", 20, 'italic','bold'),
#                 width=15, height=10)
# label_l2.place(x=750, y=40)



#T1.tag_configure("center", justify='center')
#T1.tag_add("center", 1.0, "end")

################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#def clear_img():
#    img11 = tk.Label(root, background='bisque2')
#    img11.place(x=0, y=0)


#################################################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# def cap_video():
    
#     video1.upload()
#     #from subprocess import call
#     #call(['python','video_second.py'])

def reg():
    from subprocess import call
    call(["python","registration.py"])

def log():
    from subprocess import call
    call(["python","login.py"])
  
def window():
  root.destroy()

image2 = Image.open('logo1.png')
image2 = image2.resize((100, 100), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=950, y=150) 



button1 = tk.Button(root, text="Login", command=log, width=15, height=1,font=('times', 17, ' bold '), bg="blue", fg="white")
button1.place(x=900, y=300)

button2 = tk.Button(root, text="Registration",command=reg,width=15, height=1,font=('times', 17, ' bold '), bg="blue", fg="white")
button2.place(x=900, y=380)

button3 = tk.Button(root, text="Exit",command=window,width=15, height=1,font=('times', 17, ' bold '), bg="red", fg="white")
button3.place(x=900, y=460)

root.mainloop()
