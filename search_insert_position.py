def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    inserted_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            return mid_index

        if mid_number < number_to_find:
            left_index = mid_index + 1
            inserted_index = left_index
        else:
            right_index = mid_index - 1
            inserted_index = mid_index

    return inserted_index


elements = [1,3,5,6]
print(binary_search(elements, 7))
elements = [1,3]
print(binary_search(elements, 2))
elements = [1,3]
print(binary_search(elements, 0))
elements = [1,3,18,22]
print(binary_search(elements, 25))
elements = [1,3,5,6]
print(binary_search(elements, 5))