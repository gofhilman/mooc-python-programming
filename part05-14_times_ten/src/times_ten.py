# Write your solution here
def times_ten(start_index: int, end_index: int):
    dictionary = {}
    for index in range(start_index, end_index + 1):
        dictionary[index] = index * 10
    # dictionary = {index: index * 10 for index in range(start_index, end_index + 1)}
    return dictionary


if __name__ == "__main__":
    d = times_ten(3, 6)
    print(d)
