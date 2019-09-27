def binary_search(input_array, value):
    index = -1
    first_index = 0
    last_index = len(input_array) - 1
    while(first_index <= last_index):
        mid_index = first_index + int((last_index-first_index)/2)
        mid_value = input_array[mid_index]
        if value == mid_value:
            index = mid_index
            break
        elif value > mid_value:
            first_index = mid_index + 1
        else:
            last_index = mid_index - 1
    return index


test_list = [1,3,9,11,15,19,29,32,37,38,41,42]
test_val1 = 25
test_vals = [25, 1,3,9,11,15,19,29,32,37,38,41,42, 500, -25]
#print(binary_search(test_list, test_val1))
for val in test_vals:
    print(binary_search(test_list, val))
