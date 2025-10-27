# Write your solution here
def longest(string_list):
  longest_string = ""
  max_length = 0
  for string in string_list:
	if len(string) > max_length:
	  longest_string = string
	  max_length = len(string)
  return longest_string