def rotate(rotate_by, elements):
    return elements[rotate_by:] + elements[0:rotate_by]


def main():
    t = int(input("Please enter the number of test cases: "))
    for test in range(t):
        n = int(input("Please enter the number of elements: "))
        d = int(input("Please enter the number of elements to rotate by: "))
        items = input("Please enter the elements separated by spaces: ")
        elements = list(map(int, items.split()))
        if len(elements) is n:
            print(rotate(d, elements))


if __name__ == '__main__':
    main()
