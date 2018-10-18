from collections import Counter


def find_majority_element(elements):
    majority = len(elements) / 2
    counts = Counter(elements)
    top = counts.most_common(1)[0]

    return top[0] if top[1] > majority else -1


def main():
    t = int(input("Please enter the number of test cases: "))
    for test in range(t):
        n = int(input("Please enter the number of elements: "))
        items = input("Please enter the elements separated by space: ")
        elements = list(map(int, items.split()))
        if len(elements) is n:
            print(find_majority_element(elements))


if __name__ == '__main__':
    main()
