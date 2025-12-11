#   multifactorgui.py
import tkinter as tk

# main window
root = tk.Tk()
root.wm_geometry("300x300")
root.title("Authentication")

# ----- Frames -----
frame_login = tk.Frame(root)
frame_login.grid(row=0, column=0, sticky="news")

frame_auth = tk.Frame(root)
frame_auth.grid(row=0, column=0, sticky="news")

# ----- Login Widgets -----
lbl_username = tk.Label(frame_login, text="Username:", font="Courier")
lbl_username.pack()

ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(padx=75, pady=10)

lbl_password = tk.Label(frame_login, text="Password:", font="Courier")
lbl_password.pack(padx=50, pady=10)

ent_password = tk.Entry(frame_login, bd=3, show="*")   # masks password input
ent_password.pack(padx=75, pady=10)

# ----- Auth Frame Widgets -----
lbl_show_password = tk.Label(frame_auth, text="", font="Courier")
lbl_show_password.pack(pady=20)

# ----- Functions -----
def test_my_button():
    # get the password from the entry box
    user_password = ent_password.get()
    # configure the label to display it
    lbl_show_password.config(text=f"Your password is: {user_password}")
    # raise the auth frame
    frame_auth.tkraise()

# ----- Button -----
btn_login = tk.Button(frame_login, text="Login", command=test_my_button)
btn_login.pack(padx=75, pady=10)

# show login frame first
frame_login.tkraise()

root.mainloop()
