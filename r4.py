import tkinter
import json

def submit():
    user= entry_username.get()
    pas= entry_password.get()

    if not user or not pas:
        lbl_result.config(text="enter both user and pas ", fg="red",bg="#590505")
        return

    users=load_users()
    if username in users:
        lbl_result.config(text="username already submit", fg="red",bg="#590505")
    else:
        users[username] = password
        save_users(users)
        lbl_result.config(text="submit done", fg="green",bg="#590505")

def login():
    user=entry_user.get()
    pas=entry_pas.get()

    if not user or not pas:
        lbl_result.config(text="enter both user and pas ", fg="red")
        return

    users=load_users()
    if user in users and users[user]==pas:
        lbl_result.config(text="login done", fg="green")
    else:
        lbl_result.config(text="wrong username or password", fg="red")
        
def delete_account():
    username=entry_username.get()
    if not username:
        lbl_result.config(text="enter a username", fg="red")
        return
    users=load_users()
    if username in users:
        del users[username]
        save_users(users)
        lbl_result.config(text="account has been deleted ", fg="green")
    else:
        lbl_result.config(text="username not found.", fg="red")
        
def load_users():
        with open("users.json") as f:
            users=json.load(f)
        users={}
        return users

def save_users(users):
    with open("users.json", "w") as f:
        json.dump(users, f)


root=tk.Tk()
root.title("login_ submit _delete account")
root.geometry("400x300")
root.configure(bg="cyan1")

# Create widgets
label_username=tk.Label(root,text="User:",bg="#897dca")
label_username.pack()

entry_username=tk.Entry(root)
entry_username.pack()

label_password=tk.Label(root,text="Pass:",bg="#897dca")
label_password.pack()

entry_password=tk.Entry(root,show="*")
entry_password.pack()

lbl_result=tk.Label(root,text="",fg="purple")
lbl_result.pack()

btn_login=tk.Button(root,text="login",command=login,bg="#ffc1f4")
btn_login.pack()

btn_submit=tk.Button(root,text="submit",command=submit,bg="#ffc1f4")
btn_submit.pack()

btn_delete_account=tk.Button(root,text="delete acc",command=delete_account,bg="#c1ffc1")
btn_delete_account.pack()

# Run the main loop
root.mainloop()

