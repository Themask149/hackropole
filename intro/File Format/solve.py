import hashlib

def solve():
    i_list=b""
    q_list=b""
    with open("file-format.iq", "rb") as f:
        while True:
            i = f.read(4)
            if not i:
                break
            i_list+=i
            q = f.read(4)
            q_list+=q
    full=i_list+q_list
    sha256=hashlib.new("sha256")
    sha256.update(full)
    return sha256.hexdigest()

print(solve())
