from edx_io import edx_io

def sum(a, b):
    return a + b

with edx_io() as io:
    sum = sum(io.next_int(), io.next_int())
    io.writeln(sum)
