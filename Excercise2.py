
height = int(input("Enter a height: "))

def printPine(height):
    for i in range(1, height + 1):
        spaces = '  ' * (height - i)
        leaves = '* ' * (2 * i - 1)
        print(spaces + leaves)

    trunk_height = 3
    trunk_spaces = '  ' * (height - 1)

    for _ in range(trunk_height):
        print(trunk_spaces + "*")

printPine(height)