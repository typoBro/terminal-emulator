import tkinter as tk

def run_ui(prompt, on_command, on_start=None, title=None):
    w = tk.Tk()
    w.title(title or "Эмулятор")
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

    def destroy():
        w.destroy()

    def on_enter(event=None):
        s = e.get()
        e.delete(0, "end")
        out(s + "\n")
        on_command(s, out, destroy, prompt)

    e.bind("<Return>", on_enter)
    if on_start:
        on_start(out, destroy)
    else:
        out(prompt)
    w.mainloop()