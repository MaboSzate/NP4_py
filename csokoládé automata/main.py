with open("be3.txt") as f:
    AR, N = [int(i) for i in f.readline().split()]
    E = [int(i) for i in f.readline().split()]

kell_meg = AR
out = []
while kell_meg > 0 and E:
    maxc = max(E)
    if maxc > kell_meg:
        E.remove(maxc)
    else:
        kell_meg = kell_meg - maxc
        E.remove(maxc)
        out.append(maxc)


if len(E) <= 3 and kell_meg==0:
    print(out)
else:
    print("NEM LEHET")


