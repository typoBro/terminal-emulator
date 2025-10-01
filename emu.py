import tkinter as tk
import shlex, getpass, socket

u = getpass.getuser()
h = socket.gethostname()
p = f"{u}@{h}$ "

w = tk.Tk()
w.title(f"Эмулятор - [{u}@{h}]")

t = tk.Text(w, wrap="word", state="disabled")
t.pack(fill="both", expand=True)
e = tk.Entry(w)
e.pack(fill="x")
e.focus()

def out(s):
    t.config(state="normal")
    t.insert("end", s)
    t.see("end")
    t.config(state="disabled")
    
out(p)

def run(event=None):
    s = e.get()
    e.delete(0, "end")

    out(s + "\n")

    try:
        x = shlex.split(s)
    except ValueError as err:
        out(f"parse error: {err}\n")
        out(p)
        return

    if not x:
        out(p)
        return

    c, a = x[0], x[1:]
    if c == "exit":
        w.destroy()
        return
    elif c in ("ls", "cd"):
        out(str([c] + a) + "\n")
    else:
        out(f"{c}: command not found\n")

    out(p)

e.bind("<Return>", run)

w.mainloop()