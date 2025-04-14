## In this code, calculationg error analysis of proposed multiplier, calculationg NMED, MRED

wrong = 0
sed = 0
mred = 0
max_diff = 0
max_diff_combinations = []

for i in range(256):
    for j in range(256):
        z = (i * j)
        pdt = BMFA(i, j)  # Approximate multiplier output
        diff = abs(pdt - z)

        sed += diff

        if z != 0:
            red = diff / z
            mred += red

        if diff != 0:
            wrong += 1

        if diff > max_diff:
            max_diff = diff
            max_diff_combinations = [(i, j)]
        elif diff == max_diff:
            max_diff_combinations.append((i, j))

med = sed / 65536
ert = (wrong / 65536) * 100
crt = 65536 - wrong
psrt = (crt / 65536) * 100
pmax = 65025  # 255 * 255
Nmed = med / pmax
Mred = mred / 65536

print("Total combination:", ((i + 1) * (j + 1)))
print("Total wrong combination:", wrong)
print("Total correct combination:", crt)
print("Error rate:", ert, "%")
print("Pass rate:", psrt, "%")
print("Total error distance:", sed)
print("Mean error distance:", med)
print("Normalized mean error distance:", Nmed)
print("Mean relative error distance:", Mred)
print("Maximum error distance:", max_diff)
print("Combinations with maximum error distance:", max_diff_combinations)
