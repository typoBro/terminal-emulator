import os

def run_script(path, out, handle, prompt, destroy):
    if not path or not os.path.isfile(path):
        out(prompt)
        return
    try:
        lines = open(path, "r", encoding="utf-8").read().splitlines()
    except Exception as ex:
        out(f"[debug] Failed to read script: {ex}\n")
        out(prompt)
        return
    cmds = []
    for line in lines:
        s = line.strip()
        if not s:
            continue
        if s.startswith("#"):
            continue
        cmds.append(s)
    for s in cmds:
        out(prompt + s + "\n")
        if s.strip() == "exit":
            destroy()
            return
        handle(s, out, destroy, prompt)