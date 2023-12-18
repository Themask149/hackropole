import pwn

def exploit():
    conn = pwn.remote("localhost",4000)
    while conn.can_recv(timeout=1):
        rec=conn.recvline()
        print(rec)
        if rec.startswith(b">>> "):
            result = rec[4:-1]
            result=result[::-1]+ b"\n"
            print(result)
            conn.send(result)

exploit()
