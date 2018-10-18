def segregate(elements):
    return sorted(elements)


def main():
    t = int(input("Please enter the number of test cases: "))
    for test in range(t):
        n = int(input("Please enter the number of elements: "))
        items = input("Please enter the elements separated by spaces: ")
        elements = list(map(int, items.split()))
        if len(elements) is n:
            print(*segregate(elements), sep=" ")


if __name__ == '__main__':
    main()
