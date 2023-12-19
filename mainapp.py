import sys
sys.path.append('/path/to/test') 

from tools.numbers.simp import addnumbers, subnumbers
from tools.numbers.comp import sum_of_digits, ispal
from tools.col import myzip

def main() :
    pass

simp_functions_called = False

def check_simp_functions_called():
    if not simp_functions_called:
        raise Exception("Cannot call functions in comp module before calling at least one function in simp module.")

# input number for ispal func here please:
number_to_check_ispal = 565

# input for myzip function :
list1 = [2, 5, 1]
list2 = ['tomato', 'cucumber', 'lettuce']

# Call a function from the simp module and set the flag
result_add = addnumbers(5, 5)   # Adding numbers function
simp_functions_called = True
result_sub = subnumbers(30, 6)  # Subtracting numbers function

# Call the check function before calling a function from the comp module
check_simp_functions_called()

# Try calling a function from the comp module before calling a function from the simp module
try:
    result_sum = sum_of_digits(43)  # Sum of digits function
    check_simp_functions_called()
except Exception as e:
    print(f"Exception: {e}")

result_ispal = ispal(number_to_check_ispal)  # Ispal function
result_zip = myzip(list1, list2)             # Myzip function

# Print results
print("Add Result:", result_add)
print("Subtraction Result:", result_sub)
print("Sum Of Digits:", result_sum)
print(f"Is {number_to_check_ispal} A Palindrome:", result_ispal)
for pair in result_zip:
    print(pair)

if __name__ == "__main__":
    main() 