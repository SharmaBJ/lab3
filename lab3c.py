#!/usr/bin/env python3
'''Lab 3 Inv 2 function operate '''
# Author ID: bsharma60@myseneca.ca

def operate(number1, number2, operator):
    operations = {
        'add': number1 + number2,
        'subtract': number1 - number2,
        'multiply': number1 * number2
    }
    return operations.get(operator, 'Error: function operator can be "add", "subtract", or "multiply"')

if __name__ == '__main__':
    print(operate(10, 5, 'add'))
    print(operate(10, 5, 'subtract'))
    print(operate(10, 5, 'multiply'))
    print(operate(10, 5, 'divide'))


