types = {
    "CONSTANT": False,
    "ASCENDING": False,
    "WEAKLY ASCENDING": False,
    "DESCENDING": False,
    "WEAKLY DESCENDING": False,
    "RANDOM": False
}

lastKey = None


def set_key(key):
    global lastKey
    for k in types:
        if k == key:
            types[k] = True
            lastKey = k
        else:
            types[k] = False


def check_keys(keys):
    return lastKey is None or lastKey in keys


def determine_seq(seq):
    prev = seq[0]
    for i in range(1, len(seq)):
        el = seq[i]
        if check_keys(["CONSTANT"]) and el == prev:
            set_key("CONSTANT")
        elif check_keys(["ASCENDING"]) and el > prev:
            set_key("ASCENDING")
        elif check_keys(["CONSTANT", "ASCENDING", "WEAKLY ASCENDING"]) and el >= prev:
            set_key("WEAKLY ASCENDING")
        elif check_keys(["DESCENDING"]) and el < prev:
            set_key("DESCENDING")
        elif check_keys(["CONSTANT", "DESCENDING", "WEAKLY DESCENDING"]) and el <= prev:
            set_key("WEAKLY DESCENDING")
        else:
            set_key("RANDOM")
        prev = el
    for key in types:
        if types[key]:
            return key


seq = []
while True:
    num = int(input())
    if num == -2000000000:
        break
    seq.append(num)
print(determine_seq(seq))
