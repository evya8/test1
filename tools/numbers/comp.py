def sum_of_digits(number):
   
    str_number = str(abs(number))
    
    
    digit_sum = sum(int(digit) for digit in str_number)

    return digit_sum


def ispal(number):
    
    str_number = str(number)
    reversed_str = str_number[::-1]
    return str_number == reversed_str


