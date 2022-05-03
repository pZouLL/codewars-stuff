import random
import sys

cards = [1,2,3,4,5,6,7,8,9,10,"ace"] 

def useriface(cards):
    loop = 1 
    while loop == 1:
            print("Your Cards: ",cards)
            acepick = input("Would you like ace to be 11 or 1? : ")
            if acepick == "11":
                index1 =cards.index("ace")
                cards[index1] = 11
                loop = 2
            
            elif acepick == "1":
                index1 = cards.index("ace")
                cards[index1] = 1
                loop = 2
            
            else:
                print("Invalid try again")
    
    return cards

def dealer_random_pick_first():
    dealer_cards = [random.choice(cards) ,  random.choice(cards)]
    if "ace" in dealer_cards:
        dealer_cards[dealer_cards.index("ace")] = 11

    if "ace" in dealer_cards:
        dealer_cards[dealer_cards.index("ace")] = 1

    return dealer_cards


def user_random_pick_first():
    definition = 1
    usercards3 = [random.choice(cards) , random.choice(cards)]
    user_cards = usercards3
    if "ace" in usercards3:
        user_cards = useriface(usercards3)
        definition = 2
    if "ace" in user_cards:
        usercards1 = useriface(usercards3)
        definition = 3
    if definition == 1:
        return usercards3
    elif definition == 2:
        return user_cards
    elif definition == 3:
        return usercards1
   



dealercards = dealer_random_pick_first()
usercards = user_random_pick_first()




print(f"Dealer Card : {dealercards[0]} , Hidden")  
print("")
print("Your Card : ",usercards)

hos = 1
while hos == 1:
    hitorstand = input("Hit Or Stand (H/S) : ")
    if hitorstand.lower() == "h" :
        new_card = random.choice(cards)
        usercards.append(new_card)
        usercards1 = usercards
        if "ace" in usercards:
            usercards1 = useriface(usercards)
        
        if sum(usercards1) > 21:
            print("")
            print("Your Cards:",usercards1)
            print("You Lost")
            sys.exit()
        
        elif sum(usercards1) == 21:
            print("")
            print("Blackjack!")
            print("Your Cards : " , usercards1)
            sys.exit()
        
        else:
            usercards = usercards1
            print("Your Cards:",usercards)
    
    elif hitorstand.lower() == "s" :
        hos = 2 
    
    else:
        print("Invalid, Try Again")

dealerhos = 1 
while dealerhos == 1 :
    if sum(dealercards) < 17:
        new_card = random.choice(cards)
        if new_card == "ace" :
            if sum(dealercards) + 11 <= 21:
                dealercards.append(11)
            else:
                dealercards.append(1)
        
        else:
            new_card = random.choice(cards)
            dealercards.append(new_card)

        print(f"Dealer Card : {dealercards}")  

    else:
        dealercards = dealercards
        print(f"Dealer Card : {dealercards}")  
        if sum(dealercards) <= 21:
            if sum(dealercards) > sum(usercards):
                print("Dealer Win")
            elif sum(dealercards) >= sum(usercards):
                print("You Win")
        else:
            print("Dealer Bust, You Win")
        
        dealerhos = 2 
        
