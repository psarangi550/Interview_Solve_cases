def first():
    second()
    print("First Method Executing")


def second():
    third()
    print("second method executing")


def third():
    forth()
    print("Third method executing")


def forth():
    print("forth method executing")


if __name__ == "__main__":
    first()


# we can write this as


def first_alter(n):
    if n < 1:
        print(f"{n}method executing ")
    else:
        print(f"{n}method executing")
        first_alter(n - 1)


if __name__ == "__main__":
    first_alter(4)
