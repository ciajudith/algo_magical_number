def custom_sort(list_to_sort):
    count_letter_list = []
    for i in range(len(list_to_sort)):
        count_letter_list.append((i, list_to_sort[i], len(list_to_sort[i])))
    ordered_list = []

    while len(ordered_list) != len(list_to_sort):
        indice_minimum = 0
        minimum = count_letter_list[0][2]
        mot_minimum = count_letter_list[0][1]

        for i in range(len(count_letter_list)):
            current_length = count_letter_list[i][2]
            current_word = count_letter_list[i][1]

            if current_length < minimum:
                minimum = current_length
                mot_minimum = current_word
                indice_minimum = i
            elif current_length == minimum and current_word < mot_minimum:
                mot_minimum = current_word
                indice_minimum = i

        ordered_list.append(count_letter_list[indice_minimum][1])
        count_letter_list.pop(indice_minimum)

    print(ordered_list)


custom_sort(["rerte", "tertert", "frege", "gregee", "gesgege","ayy"])
