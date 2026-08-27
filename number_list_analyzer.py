def countEven(numbers):
    count = 0
    for item in numbers:
        if item % 2 == 0:
            count += 1
    return count

def findMax(numbers):
    return max(numbers)

def calculateAverage(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum / len(numbers)

numbers = []

while len(numbers) != 7:
    print("Enter an integer number:")
    integer = input()
    numbers.append(int(integer))

print(f"Numbers: {numbers}")
print(f"Even Count: {countEven(numbers)}")
print(f"Maximum Value: {findMax(numbers)}")
print(f"Average Value: {calculateAverage(numbers)}")
