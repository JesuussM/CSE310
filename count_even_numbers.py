def count_even(numbers):
    count = 0
    for item in numbers:
        if item % 2 == 0:
            count += 1
    return count

nums = [1, 2, 3, 4, 5, 6, 7]
print(f"Number of even values: {count_even(nums)}")