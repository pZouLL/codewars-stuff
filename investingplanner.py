import sys
def get_interest(Inves , Interest , taxrate) :
    Inves = float(Inves)
    Interest = float(Interest)
    Interest_last = Inves * Interest 
    taxrate = float(taxrate)
    Interest_last1 = Interest_last * taxrate  
    Interest_last2 = Interest_last - Interest_last1
    total_per_year = Inves + Interest_last2
    return total_per_year


invest1 = input("Money Going To Be Invested : ")
interest1 = input("Interest Rate : ")
tax1 = input("Tax Rate : ")
desired1 = float(input("Desired Sum : "))
loop =1
interest_per_year = invest1
year = 0
while loop != 2 :
    if int(invest1) == int(desired1) :
        print("0 Years")
        loop = 30
        sys.exit()
    elif int(desired1) < int(invest1):
        print("Desired Sum Is Smaller Than Invest")
        sys.exit()

    else:
        interest_per_year = get_interest(interest_per_year , interest1 , tax1)
        print(interest_per_year)
        year += 1 
        print("After" , year , "Year :  " , interest_per_year)
        if interest_per_year > desired1 :
            print("It will take :" , year, "Years")
            loop = 2