#AQUINO HEAVEN
#BAET 2102
#SKIP THE THREES

total = 0

for num in range(1, 51):
    if num % 5 == 0:
        continue
    print(num, end=" ")
    total += num

print()
print(f"Sum: {total}")
