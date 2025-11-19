def my_min(numbers):
    minNumber = numbers[0]
    for number in numbers[1:]: #[1:] so it skips the first one
        if minNumber > number:
            minNumber = number
    return minNumber

l = [1,4,6,2,9, -1, 5]

print (my_min(l))