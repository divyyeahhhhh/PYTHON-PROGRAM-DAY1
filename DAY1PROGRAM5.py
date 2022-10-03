#v1
fresh_loaf = 185
discount = 60

def message():
    amount = float(input("ENTER THE NUMBER OF FRESH LOAVES PURCHASED: "))
    regular = round(fresh_loaf * amount,2)
    discounted = round(regular * discount,2)
    total = round(regular - discounted,2)
    print(f'REGULAR PRICE is {regular}\nAMOUNT OF NEW LOAVES{total}')

message()

#v2
fresh_loaf = 185
discount = 60

def message():
    amount = input("Please enter loaves of yesterday's bread (q to quit): ")
    while True:
        if amount == 'q':
            break
        elif amount != '' and amount != ' ':
            amount = float(amount)
            regular = round(fresh_loaf * amount,2)
            discounted = round(regular * discount,2)
            total = round(regular - discounted,2)
            print(f'Regular price is {regular} \nThe discount is {discounted}\nTotal is {total}')
        amount = input("Please enter loaves of yesterday's bread(q to quit): ")

message()
