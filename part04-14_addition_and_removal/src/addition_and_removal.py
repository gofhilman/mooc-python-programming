# Write your solution here
listing = []
while True:
  print(f"The list is now {listing}")
  user_input = input("a(d)d, (r)emove or e(x)it: ")
  match user_input:
    case "d":
      listing.append(len(listing) + 1)
    case "r":
      listing.pop()
    case "x":
      break
print("Bye!")
