from tkinter import *
from PIL import Image, ImageTk


root = Tk()
menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About")

# Window settings
root.title("Student Form")
root.iconbitmap("pixel2.ico")
bg_img = Image.open("background.jpg")   # your background image
bg_img = bg_img.resize((1600,1600))
bg = ImageTk.PhotoImage(bg_img)

bg_label = Label(root, image=bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

 # profile image
profile_img = Image.open("profile.png")  
profile_img = profile_img.resize((100,100))
profile = ImageTk.PhotoImage(profile_img)

rofile_label = Label(root, image=profile, bg='#95613C')
profile_label = Label(root, image=profile, bd=0)
profile_label.pack(pady=8)

# Title
text_label = Label(root, text="Charigad Meteor", font=('Arial',18,'bold'), bg= "#95613C", fg='black')
text_label.pack(pady=10, padx=20)

# Email
email_label = Label(root, text="Email", font=('Arial',18,'bold'), bg='#95613C')
email_label.pack(pady=(20,5))

email_entry = Entry(root, font=('Arial',18,'bold'))
email_entry.pack(pady=(5,10))

# Password
password_label = Label(root, text="Password", font=('Arial',18,'bold'), bg='#95613C')
password_label.pack(pady=(20,5))

password_entry = Entry(root, font=('Arial',18,'bold'), show="*")
password_entry.pack(pady=(5,10))

# Login Button
login_btn = Button(root, text="Login", font=('Arial',18,'bold'), bg='#95613C', fg='white')
login_btn.pack(pady=(5,10))

root.mainloop()