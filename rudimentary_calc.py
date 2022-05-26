# rudimentary_calc
def main ():
    ### get user input
    first_name = input ('Enter your first name ')
    last_name = input ('Enter your last name ')
    age = int(input('Enter your age '))
    ### generate output
    print (first_name, last_name, 'is', age)
    birth_year = 2019 - age
    print ('You were born in', birth_year)
    ### get user input
    num1 = int(input('Enter an integer '))
    num2 = int(input('Enter another integer '))
    total = num1 + num2
    diff = num1 - num2
    prod = num1 * num2
    quot = num1 / num2
    ### generate output
    print('Sum:', total)
    print('Difference:', diff)
    print('Product:', prod)
    print('Quotient:', quot)
    ### get user input
    print('Suppose', first_name, 'is at a store and you buy a shirt. Enter the price. There is a 20% discount. ')
    original_price = float(input("Enter the item's price "))
    discount = original_price * 0.2
    sale_price = original_price - discount
    ### generate output
    print('The sale price is', sale_price)

main ()
    
