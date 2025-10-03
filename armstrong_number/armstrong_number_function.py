def is_an_armstrong_number(number):
    is_armstrong = False

    quotient, remainder = number // 10, number % 10
    list_of_remainders = [remainder]
    while quotient > 0:
        quotient, remainder = quotient // 10, quotient % 10
        list_of_remainders.append(remainder)
    list_of_remainders.reverse()

    power = len(list_of_remainders)
    calculate = 0
    for remainder in list_of_remainders:
        calculate += remainder ** power
        # or I can simply do :
        # calculate = sum([remainder ** power for remainder in list_of_remainder])
    if calculate == number:
        is_armstrong = True

    return is_armstrong, list_of_remainders, calculate, power
