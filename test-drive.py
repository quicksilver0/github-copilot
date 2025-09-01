# Write a program that converts a Roman numeral to an integer. Make it accept a Roman numberal from a user and print the integer value.
def roman_to_integer(roman):
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    integer_value = 0
    prev_value = 0
    
    for char in reversed(roman):
        current_value = roman_numerals[char]
        
        if current_value < prev_value:
            integer_value -= current_value
        else:
            integer_value += current_value
            
        prev_value = current_value
        
    return integer_value
if __name__ == "__main__":
    roman_input = input("Enter a Roman numeral: ").upper()
    try:
        result = roman_to_integer(roman_input)
        print(f"The integer value of the Roman numeral {roman_input} is {result}.")
    except KeyError:
        print("Invalid Roman numeral entered.")# Example usage:
    # print(roman_to_integer("XIV"))  # Output: 14
    