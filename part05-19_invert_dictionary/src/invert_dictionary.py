# Write your solution here
def invert(dictionary: dict):
  copied_dict = dict(dictionary)
  dictionary.clear()
  for key, value in copied_dict.items():
    dictionary[value] = key

if __name__ == "__main__":
  s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
  invert(s)
  print(s)