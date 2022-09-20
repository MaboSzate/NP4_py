hol_volt = 0
mm = -1

with open("be1.txt") as f:
    K, N, B, L=[int(i) for i in f.readline().split(" ")]
    for i in range(N):
        hol, mennyit = [int(i) for i in f.readline().split(" ")]
        B = B - (hol-hol_volt)/100 * L + mennyit
        if B > mm:
            mm = B
        hol_volt = hol

print(mm)


