# Write your solution here
def double_items(numbers: list):
  doubled_list = numbers[:]
  for i in range(0, len(doubled_list)):
    doubled_list[i] = doubled_list[i] * 2
  # doubled_list = [item * 2 for item in numbers]
  return doubled_list

if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)