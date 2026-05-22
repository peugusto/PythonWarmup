def positive():
    numbers = [1, 2, 3, -4, 0, 4, 0, -9, 999, 42]
    count_positive = 0
    sum = 0

    for i in numbers:
        if not i >= 0:
            continue
        if i == 999:
            break
        count_positive += 1
        sum += i

    print(f"sum: {sum}")
    print(f"count: {count_positive}")


if __name__ == "__main__":
    positive()
