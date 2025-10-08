import getpass, socket
import app_config
from ui_tk import run_ui
from core import handle
from script_runner import run_script

args = app_config.get_config()
u = getpass.getuser()
h = socket.gethostname()
PROMPT = args.prompt if args.prompt else f"{u}@{h}$ "

def start(out, destroy):
    out("[debug] Startup parameters:\n")
    out(f"[debug] VFS    = {repr(args.vfs)}\n")
    out(f"[debug] Prompt = {repr(PROMPT)}\n")
    out(f"[debug] Script = {repr(args.script)}\n\n")
    run_script(args.script, out, handle, PROMPT, destroy)

run_ui(PROMPT, handle, on_start=start, title=f"Эмулятор - [{u}@{h}]")