# Write your solution here
def most_common_character(string):
  char = ""
  max_qty = 0
  for char_iter in string:
    qty = string.count(char_iter)
    if qty > max_qty:
      char = char_iter
      max_qty = qty
  return char
