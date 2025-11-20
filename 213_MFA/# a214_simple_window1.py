#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk
def test_my_button():
    frame_auth.tkraise()
    password=ent_Authorization.get()
    lbl_Auth.config(text=password)

# main window
root = tk.Tk()
root.wm_geometry("1000x1000")
root.title("Authorization")

# create empty frame
frame_login = tk.Frame(root)
frame_login.grid(row=0,column=0, sticky= 'news')

lbl_username = tk.Label(frame_login, text='Username:')
lbl_username.pack(pady=50)

ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=50)

lbl_password = tk.Label(frame_login, text= 'password', font ='courier')
lbl_password.pack(pady=50)


ent_Authorization = tk.Entry(frame_login, bd=3)
ent_Authorization.pack(pady=5)

# CODE TO ADD

Btn_login = tk.Button(frame_login, text='login', command=test_my_button)
Btn_login.pack(pady=50)



frame_auth = tk.Frame(root)
frame_auth.grid(row=0,column=0, sticky= 'news')

lbl_Auth=tk.Label(frame_auth)
lbl_Auth.pack()


frame_login.tkraise()






    
root.mainloop()    
