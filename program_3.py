def calculate_total_purchase():
    # Owen Eigen,  9/12/2024,  Total Purchase
    #item prices
    price1 = float(input('Input price of item 1: '))
    price2 = float(input('Input price of item 2: '))
    price3 = float(input('Input price of item 3: '))
    price4 = float(input('Input price of item 4: '))
    price5 = float(input('Input price of item 5: '))
    #calculation
    TAX = .07
    sub_total = price1 + price2 + price3 + price4 + price5
    total_tax = sub_total*TAX
    final_price = sub_total + total_tax

    #display to user
    print(f'Sub total = ${sub_total:,.2f}')
    print(f'Sales tax = ${total_tax:,.2f}')
    print(f'Your total is ${final_price:,.2f}')


calculate_total_purchase()