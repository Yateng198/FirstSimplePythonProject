def read_numbers(filename):
    numbers1 = []
    with open(filename, "r") as f:
        for line in f:
            # print(line, end="")
            try:
                numbers1.append(float(line))
            except ValueError:
                pass
                # break
    return numbers1


numbers = read_numbers("data.txt")
print(numbers)

for c in "some string":
    print(c, end="")