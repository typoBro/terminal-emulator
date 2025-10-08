import shlex

def handle(s, out, destroy, prompt):
    try:
        x = shlex.split(s)
    except ValueError as err:
        out(f"parse error: {err}\n")
        out(prompt)
        return
    if not x:
        out(prompt)
        return
    c, a = x[0], x[1:]
    if c == "exit":
        destroy()
        return
    elif c in ("ls", "cd"):
        out(str([c] + a) + "\n")
    else:
        out(f"{c}: command not found\n")
    out(prompt)