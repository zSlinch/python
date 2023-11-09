def calculate():
    operation = input('''Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division >> ''')
    
    n1 = int(input('número 1:>> '))
    n2 = int(input('numero 2:>> '))

    if operation == '+':
        print('{} + {} = ' .format(n1 , n2))
        print(n1 + n2)

    elif operation == '-':
        print('{} - {} = ' .format(n1 , n2))
        print(n1 - n2)

    elif operation == '*':
        print('{} * {} = ' .format(n1 , n2))
        print(n1 * n2)

    elif operation == '/':
        print('{} / {} = ' .format(n1 , n2))
        print(n1 / n2)

    else:
        print('se voce nao colocou alguns desses operadores rode o programa novamente')
    again()

def again():
    calc_again = input(''' Do you want to calculate again?
    Please type Y for YES or N for NO. ''')
    
    if calc_again.upper() == 'Y':
        calculate()

    elif calc_again.upper() == 'N':
        print('veja novamente')

    else:
        again()

calculate()
        