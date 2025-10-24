# Write your solution here
def everything_reversed(oriList: list) -> list:
  update = oriList[::-1]
  iteration = 0
  while iteration < len(update):
    update[iteration] = update[iteration][::-1]
    iteration += 1
  return update

if __name__ == "__main__":
  my_list = ["Hi", "there", "example", "one more"]
  new_list = everything_reversed(my_list)
  print(new_list)
