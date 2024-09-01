def roman_to_decimal(roman):
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    decimal_value = 0
    prev_value = 0

    for c in roman[::-1]:
        current_value = roman_values[c]
        if current_value < prev_value:
            decimal_value -= current_value
        else:
            decimal_value += current_value
        prev_value = current_value
    return decimal_value

def decimal_to_roman(num):
    roman_symbols = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),(100, "C"), (90, "XC"), (50, "L"), (40, "XL"),(10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1,"I")]
    
    roman_numeral = ""
    for value, symbol in roman_symbols:
        while num >= value:
            roman_numeral += symbol
            num -= value
    return roman_numeral

def convert_input(text, text_base):
    if text_base == 'r':
        # Convert Roman to decimal
        return roman_to_decimal(text)
    elif text.startswith("0b"):
        # Convert binary to decimal
        return int(text, 2)
    elif text.startswith("0o"):
        # Convert octal to decimal
        return int(text, 8)
    elif text.startswith("0x"):
        # Convert hexadecimal to decimal
        return int(text, 16)
    else:
        # Convert the provided base to decimal
        return int(text, int(text_base))

def base_conversion(text, text_base, output_base):
    # convert the input base on the base
    decimal_value = convert_input(text, text_base)

    # Handle conversion from decimal to Roman numeral
    if output_base == 'r':
        return decimal_to_roman(decimal_value)
    else:
        # Function to convert decimal to any base
        def decimal_to_base(n, base):
            if n == 0:
                return "0"
            digits = "0123456789abcdefghijklmnopqrstuvwxyz"
            result = ""
            while n > 0:
                result = digits[n % base] + result
                n //= base
            return result

        return decimal_to_base(decimal_value, int(output_base))

print(base_conversion("0o15", 8, 'r'))
print(base_conversion("XIV", 'r', 7))
print(base_conversion("101", 2, 16)) 
print(base_conversion("19", 10, 'r'))

