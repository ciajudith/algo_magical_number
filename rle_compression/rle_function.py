def rle_compress(string_to_compress):
    if not string_to_compress:
        return ""
    if len(string_to_compress) == 1:
        return string_to_compress + "1"

    compressed_string = ""
    first_char = string_to_compress[0]
    compressed_string += first_char
    count = 0
    for char in string_to_compress:
        if char == first_char:
            count += 1
            continue
        else:
            first_char = char
            compressed_string += str(count) + char
            count = 1
    print(compressed_string)
    return compressed_string

rle_compress("aaabbbcccaaa444    dddddddeeefffff")

