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
    stopped = False
    def wrap_destroy():
        nonlocal stopped
        stopped = True
        destroy()
    out(prompt)
    for s in cmds:
        out(s + "\n")
        handle(s, out, wrap_destroy, prompt, echo_prompt=False)
        if stopped:
            return
        out(prompt)
    if not cmds:
        return
