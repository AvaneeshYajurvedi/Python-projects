import random
game_over = False
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
computer = random.choices(cards, k=2)
user = random.choices(cards, k=2)
def adjust_for_ace(hand):
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
adjust_for_ace(user)
adjust_for_ace(computer)
count1 = sum(user)
count2 = sum(computer)
print("User cards:", user, "Total:", count1)
def number_of_cards():
    global game_over
    if count1 == 21 and sorted(user) == [10, 11]:
        print("Computer cards:", computer, "Total:", count2)
        print("You win ")
        game_over = True
    elif count2 == 21 and sorted(computer) == [10, 11]:
        print("Computer cards:", computer, "Total:", count2)
        print("You lose ")
        game_over = True
number_of_cards()
if not game_over:
    choice = (input("Do You Want To Draw Another Card, Press Y for Yes And N for No\n")).lower()
    if choice == "y":
        user.append(random.choice(cards))
        adjust_for_ace(user)
        count1 = sum(user)
        print("User cards:", user, "Total:", count1)
        if count1 == 21:
            print("Computer cards:", computer, "Total:", count2)
            print("You win ")
            game_over=True
        if count1 > 21:
            print("You lose, You Went Over 21 ")
            game_over = True
    if not game_over and (choice == "n" or len(user) ==3):
        while count2 < 17:
            computer.append(random.choice(cards))
            adjust_for_ace(computer)
            count2 = sum(computer)
            if count2 == 21:
                print("Computer cards:", computer, "Total:", count2)
                print("You Lose, Computer Hit A Blackjack")
                game_over = True
            if count2 > 21:
                print("Computer cards:", computer, "Total:", count2)
                print("You Win, Computer Went Over 21")
                game_over = True
def compare():
    if count1 > count2:
        print("Computer cards:", computer, "Total:", count2)
        print("You win ")
    elif count2>count1:
        print("Computer cards:", computer, "Total:", count2)
        print("You lose")
    else:
        print("Computer cards:", computer, "Total:", count2)
        print("Its A Draw")
if not game_over:
    compare()


