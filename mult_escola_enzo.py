def signal(number):
    number_signal = 1

    if number < 0:
        number_signal *= -1

    return number_signal


def ten_potence(number):
    number = float(number)
    number = str(number)

    period_location = number.find('.')

    if int(float(number)) == float(number):
        potence = (len(number)-2) - period_location
    else:
        potence = (len(number)-1) - period_location

    number_ten_potence = 10**potence

    return number_ten_potence


def format_to_multiplication(number):

    if int(number) == float(number):
        number = int(number)
    else:
        number = int(str(number).replace('.', ''))

    return abs(number)


def mid_numbers(multiplicador, multiplicando):

    higher = max((multiplicador, multiplicando))
    higher = str(higher)

    lower = min((multiplicador, multiplicando))
    lower = str(lower)

    mid_numbers = list()
    for place, index in enumerate(range(len(lower)-1, -1, -1)):
        parsial_result = 0
        for mult_place, mult_index in enumerate(range(len(higher)-1, -1, -1)):
            parsial_result += int(lower[index])*int(higher[mult_index])*(10**mult_place)
        parsial_result *= 10**place
        mid_numbers.append(parsial_result)

    return mid_numbers


def mid_operation(multiplicador, multiplicando):
    multiplicador = float(multiplicador)
    multiplicando = float(multiplicando)

    mid_information = dict()
    mid_information['signal'] = 1
    mid_information['ten_potence'] = 1
    mid_information['mid_numbers'] = list()

    mid_information['signal'] = signal(multiplicador)*signal(multiplicando)
    multiplicador = abs(multiplicador)
    multiplicando = abs(multiplicando)

    mid_information['ten_potence'] = ten_potence(multiplicador) * ten_potence(multiplicando)
    multiplicador = format_to_multiplication(multiplicador)
    multiplicando = format_to_multiplication(multiplicando)

    mid_information['mid_numbers'] = mid_numbers(multiplicador, multiplicando)

    return mid_information


def final_sum(mid_information):
    mid_sum = sum(mid_information['mid_numbers'])
    mid_signal = mid_sum*mid_information['signal']
    result = mid_signal / mid_information['ten_potence']
    return result


def school_multiplication(multiplicador, multiplicando):
    mid_numbers = mid_operation(multiplicador, multiplicando)
    result = final_sum(mid_numbers)
    return result


if __name__ == '__main__':
    result = school_multiplication(98765, 12345)
    print(result)
    result = school_multiplication(1388739.81, -22740)
    print(result)
