def selection_sort(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                temp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = temp

def delete(mylist, value_index):
    pass

if __name__ == '__main__':
    nums = [5, 12, 2, 4, 24, 90, 10, 123, 1]
    print(nums)
    selection_sort(nums)
    print(nums)
