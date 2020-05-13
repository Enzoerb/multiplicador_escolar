def mid_operation(multiplicador, multiplicando):
    higher = max((int(multiplicador), int(multiplicando)))
    higher = str(higher)
    lower = min((int(multiplicador), int(multiplicando)))
    lower = str(lower)
    mid_numbers = list()
    for place, index in enumerate(range(len(lower)-1, -1, -1)):
        parsial_result = 0
        for mult_place, mult_index in enumerate(range(len(higher)-1, -1, -1)):
            parsial_result += int(lower[index])*int(higher[mult_index])*(10**mult_place)
        parsial_result = str(parsial_result) + ' '*place
        mid_numbers.append(parsial_result)
    return mid_numbers


def final_sum(mid_numbers):
    numbers_to_sum = [int(number.replace(' ', '0')) for number in mid_numbers]
    result = sum(numbers_to_sum)
    return result


def school_multiplication(multiplicador, multiplicando):
    mid_numbers = mid_operation(multiplicador, multiplicando)
    result = final_sum(mid_numbers)
    return result


if __name__ == '__main__':
    result = school_multiplication(3456, 8765)
    print(result)
