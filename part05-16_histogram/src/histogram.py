# Write your solution here
def histogram(string: str):
  unique_chars = []
  for char in string:
    if char not in unique_chars:
      unique_chars.append(char)
  dictionary = {}
  for char in unique_chars:
    frequency = string.count(char)
    dictionary[char] = frequency * "*"
    print(f"{char} {dictionary[char]}")
  # unique_chars = set(string)
  # dictionary = {char: string.count(char) * "*" for char in unique_chars}
  # for key, value in dictionary.items():
  #   print(f"{key} {value}")
