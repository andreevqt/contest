from edx_io import edx_io

def calc(a, b):
    return a + pow(b,2)

with edx_io() as io:
    res = calc(io.next_int(), io.next_int())
    io.writeln(res)
