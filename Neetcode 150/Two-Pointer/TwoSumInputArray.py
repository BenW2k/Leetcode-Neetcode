def twoSum(numbers, target):
    i = 0
    j = len(numbers) - 1

    print(len(numbers))
    print(j)

    while i < j:
        if numbers[i] + numbers[j] == target:
            return [i, j]
        elif numbers[i] + numbers[j] > target:
            j -= 1
            print( f'{numbers[i]} + {numbers[j]}')
        elif numbers[i] + numbers[j] < target:
            i += 1
            print( f'{numbers[i]} + {numbers[j]}')

numbers = [1,2,3,4,5,10,12]
target = 22

print(twoSum(numbers, target))
