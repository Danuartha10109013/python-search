def find_most_frequent_element(data):
    counts = {}
    most_frequent = None
    max_count = 0

    for num in data:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

        if counts[num] > max_count:
            max_count = counts[num]
            most_frequent = num

    return most_frequent

my_list = [2, 2, 2, 4, 4, 6, 6, 6, 6, 8, 8, 8, 8, 8]
most_frequent_element = find_most_frequent_element(my_list)
print(f'Elemen yang paling sering muncul adalah {most_frequent_element}')
