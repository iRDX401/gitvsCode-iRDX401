empty_str = ''

empty_str # This is an empty string variable. It can be used to represent a string with no characters. will give and output as ' '
print(empty_str) # Output: will be an empty line without the quote marks.

character = 'a'
character # Outputs: 'a'
print(character) # Output: a

singlequote_str = "'Python'"
doublequote_str = '"Python"'

singlequote_str

doublequote_str

print(singlequote_str) # Output: 'Python'
print(doublequote_str) # Output: "Python"

#Print multiline
multilinestr = '''
This if the 1st Line
This is 2nd
this is third
'''

print(multilinestr) # Output: This if the 1st Line

subtotal = 512
tax_rate = 0.075
tip_rate = 0.18

tax = subtotal * tax_rate
tip = subtotal * tip_rate
total = subtotal + tax + tip

print(f'Restaurant Bill\n------------------\nSubtotal:\tINR {subtotal:.2f}\nTax:\t\tINR {tax:.2f}\nTip:\t\tINR {tip:.2f}\n------------------\nTotal:\t\tINR {total:.2f}')