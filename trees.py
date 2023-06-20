height = int(input("How tall is the tree: "))
spaces = height - 1
trunc = height - 1
hash = 1

while height != 0:
    for i in range(spaces):
        print(" ", end="")
    for i in range(hash):
        print("#", end="")
    print()
    spaces -= 1
    hash += 2
    height -= 1
for i in range(trunc):
    print(" ", end="")
print("#")
