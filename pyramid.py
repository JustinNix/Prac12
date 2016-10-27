
def blocks_needed(number_of_blocks):
    if number_of_blocks < 1:
        return 0
    return number_of_blocks + blocks_needed((number_of_blocks-1))

number_of_blocks = print(blocks_needed(int(input("enter number of rows for pyramid: "))))