import shlex

def handle(s, out, destroy, prompt, *, echo_prompt=True):
    try:
        x = shlex.split(s)
    except ValueError as err:
        out(f"parse error: {err}\n")
        if echo_prompt:
            out(prompt)
        return
    if not x:
        if echo_prompt:
            out(prompt)
        return
    c, a = x[0], x[1:]
    if c == "exit":
        destroy()
        return
    if c in ("ls", "cd"):
        out(str([c] + a) + "\n")
    else:
        out(f"{c}: command not found\n")
    if echo_prompt:
        out(prompt)
