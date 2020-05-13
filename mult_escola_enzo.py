def mid_operation(multiplicador, multiplicando):
    signal = 1

    multiplicador = str(multiplicador)
    multiplicando = str(multiplicando)
    if multiplicador[0] == '-':
        signal *= -1
        multiplicador = multiplicador.replace('-', '')
    if multiplicando[0] == '-':
        signal *= -1
        multiplicando = multiplicando.replace('-', '')

    higher = max((int(multiplicador), int(multiplicando)))
    higher = str(higher)

    lower = min((int(multiplicador), int(multiplicando)))
    lower = str(lower)

    mid_numbers = [str(signal)]
    for place, index in enumerate(range(len(lower)-1, -1, -1)):
        parsial_result = 0
        for mult_place, mult_index in enumerate(range(len(higher)-1, -1, -1)):
            parsial_result += int(lower[index])*int(higher[mult_index])*(10**mult_place)
        parsial_result = str(parsial_result) + ' '*place
        mid_numbers.append(parsial_result)
    return mid_numbers


def final_sum(mid_numbers):
    numbers_to_sum = [int(number.replace(' ', '0')) for number in mid_numbers[1:]]
    result = sum(numbers_to_sum)*int(mid_numbers[0])
    return result


def school_multiplication(multiplicador, multiplicando):
    mid_numbers = mid_operation(multiplicador, multiplicando)
    result = final_sum(mid_numbers)
    return result


if __name__ == '__main__':
    result = school_multiplication(-98765, -12345)
    print(result)
