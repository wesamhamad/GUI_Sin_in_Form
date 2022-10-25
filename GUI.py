class Placeholder_State(object):
    __slots__ = 'normal_color', 'normal_font', 'placeholder_text', 'placeholder_color', 'placeholder_font', 'with_placeholder'


def add_placeholder_to(entry, placeholder, color="grey", font=None):
    normal_color = entry.cget("fg")
    normal_font = entry.cget("font")

    if font is None:
        font = normal_font

    state = Placeholder_State()
    state.normal_color = normal_color
    state.normal_font = normal_font
    state.placeholder_color = color
    state.placeholder_font = font
    state.placeholder_text = placeholder
    state.with_placeholder = True

    def on_focusin(event, entry=entry, state=state):
        if state.with_placeholder:
            entry.delete(0, "end")
            entry.config(fg=state.normal_color, font=state.normal_font)

            state.with_placeholder = False

    def on_focusout(event, entry=entry, state=state):
        if entry.get() == '':
            entry.insert(0, state.placeholder_text)
            entry.config(fg=state.placeholder_color, font=state.placeholder_font)

            state.with_placeholder = True

    entry.insert(0, placeholder)
    entry.config(fg=color, font=font)

    entry.bind('<FocusIn>', on_focusin, add="+")
    entry.bind('<FocusOut>', on_focusout, add="+")

    entry.placeholder_state = state

    return state


from tkinter import *

root = Tk()
root.title("Sin in")
root.geometry("350x270")


Label(root, text="Sin in",font="Helvetica 15 bold").place(x=150,y=2)

email = Label(root, text="Email address")
email.place(x=80,y=40)
email.config(font=("arial",13,"bold"))

Pass = Label(root, text="Password")
Pass.place(x=80,y=100)
Pass.config(font=("arial",13,"bold"))

emailvalue = StringVar
Passvalue = StringVar
checkvalue = StringVar

emailentry = Entry(root, textvariable=emailvalue,width=25)
emailentry.place(x=80,y=60)
add_placeholder_to(emailentry,'Enter email')

Passentry = Entry(root, textvariable=emailvalue,width=25)
Passentry.place(x=80,y=120)
add_placeholder_to(Passentry,'Enter password')

checkbtn =Checkbutton(text="Remember me", variable=checkvalue)
checkbtn.place(x=80,y=150)
checkbtn.config(font=("arial",11,"bold"))

button1 = Button(root, text="Sumbmit",width = 23,height = 2 ,bg ='blue')
button1.place(x=80,y=170)

Forgot1 = Label(root, text="Forgot",fg="gray")
Forgot2 = Label(root, text="password?",fg="#177ccf")

Forgot1.place(x=218,y=210)
Forgot2.place(x=252,y=210)

Forgot1.config(font=("arial",10))
Forgot2.config(font=("arial",10))

root.mainloop()
