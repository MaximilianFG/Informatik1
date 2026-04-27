for a in range(10):
    print(a + 1)

print("-----------------")

for b in range(10):
    print(10 - b)

print("-----------------")

for c in range(10):
    print(-5 + c)

print("-----------------")

for d in range(100):
    if d == 0:
        continue
    if d % 7 == 0:
        print(d)
print("-----------------")
for e in range(11):
    print(e**2)


for f in range(1001):
    f = f / 1000
    if f % 0.125 == 0:
        print(f)
