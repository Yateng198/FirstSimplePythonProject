empty_list = []
print(empty_list)

numbers = [4, 5.232, -1, 6.8, 9, 12]
print(numbers)

names = ['yateng', 'dennis', 'Bob']
print(names)

print(numbers[1])
print(numbers[4])

print('For #1')
for x in numbers:
    print(x)

print('Length of numbers =', len(numbers))

print('\nFor #2')
for i in range(len(numbers)):
    print(f'numbers[{i}] = {numbers[i]}')

print(numbers[5])
print(numbers[-1])

print('\nFor #3')
for i in range(len(numbers) - 1, -1, -1):
    print(f'numbers[{i}] = {numbers[i]}')

print('\nFor #4')
for i in range(1, len(numbers) + 1):
    print(f'numbers[{-i}] = {numbers[-i]}')

print('\nFor #5')
for x in reversed(numbers):
    print(x)

print('\nFor #6')
total = 0
for x in numbers:
    total += x
print(total)

# print("\nwhile loop #1")
# answer = ""
# print(names)
# while answer != "exit":
#     answer = input("Enter a name please!")
#     names.append(answer)
# print(names)

# print("\nwhile loop #2")
# print(names)
# answer = input("Enter a name please!")
# while answer != "exit":
#     names.append(answer)
#     answer = input("Enter a name: ")
# print(names)

# print("\nwhile loop #3")
# print(names)
# while True:
#     answer = input("Enter a name: ")
#     if answer == "exit":
#         break
#     names.append(answer)
# print(names)

# print("\nwhile loop #4")
# print(numbers)
# while True:
#     answer = input("Enter a number: ")
#     if answer == "exit":
#         break
#     numbers.append(float(answer))
# print(numbers)

# print(names)
# names_upper1 = []
# for name in names:
#     names_upper1.append(name.upper())
# print(names_upper1)


# print(names)
# names_upper1 = []
# for i in range(len(names)):
#     names[i] = names[i].upper()
# print(names)

names_uppers = [name.upper() for name in names]
print(names_uppers)
names_lower = [name.lower() for name in names_uppers]
print(names_lower)


