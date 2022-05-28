rects = {}


def create_rect(w, h):
    rects[w * h] = [w, h]


a, b, c, d = list(map(int, input().split()))

create_rect(max(a, c), b + d)
create_rect(max(a, d), b + c)
create_rect(max(b, d), a + c)
create_rect(max(b, c), a + d)

min = next(iter(rects))
for area in rects:
    if area < min:
        min = area

res = rects[min]
print("{} {}".format(res[0], res[1]))
