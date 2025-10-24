# Copy here code of line function from previous exercise
def line(length, string):
    if string == "":
        string = "*"
    print(length * string[0])

def box_of_hashes(height):
    # You should call function line here with proper parameters
    while height > 0:
        line(10, "#")
        height = height - 1

    # for iteration in range(height):
    #     line(10, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
