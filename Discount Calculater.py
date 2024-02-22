def discountcal():
    orgprice=int(input("This is Discount Calculater!What is the original price? "))
    discount=int(input("What is discount? "))
    finalprice=(orgprice-orgprice*discount/100)
    print("Your final price is", +finalprice)

discountcal()

