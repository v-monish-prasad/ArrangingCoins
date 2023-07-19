def arrangingCoins(num):
    iterator = 1

    while num >= iterator:
        num -= iterator
        iterator += 1

    return iterator - 1


if __name__ == "__main__":
    number = int(input())

    print(arrangingCoins(number))
