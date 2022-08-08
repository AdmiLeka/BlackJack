import random

deck_symbol = ["Clubs", "Diamonds", "Spades", "Hearts"]
deck_number_dict = {"Ace": 1, "Two": 2, "Three": 3,
                    "Four": 4, "Five": 5, "Six": 6,
                    "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10,
                    "Jack": 10, "Queen": 10, "King": 10}

class Card:
    def __init__(self, card = 0, number = 0, symbol = 0, value = 0):
        randomKey = random.choice(list(deck_number_dict.keys()))
        self.number = randomKey
        self.value = deck_number_dict[randomKey]
        self.symbol = str(deck_symbol[random.randint(0, len(deck_symbol) - 1)])
        self.card = (f"{self.number} of {self.symbol}")

def generateCard():
    a = Card()
    return a.card, a.value

def noDuplicateCards(appendTo, checkHereToo):
    newCard = generateCard()
    while newCard in appendTo or newCard in checkHereToo:
        newCard = generateCard()
    appendTo.append(newCard)
    return appendTo

def dealersHand(dealerCardzzz):
    noDuplicateCards(dealerCardzzz, playerCards)
    return dealerCards

def dealerCantDraw(dealerCardzz):
    if sumOfCards(dealerCardzz) >= 17:
        return True
    else:
        return False

def isDealerBust(dealerCards):
    if sumOfCards(dealerCards) > 21:
        return True
    else:
        return False

def firstHand(playerCardz, dealerCardz):
    noDuplicateCards(playerCardz, dealerCardz)
    noDuplicateCards(dealerCardz, playerCardz)
    noDuplicateCards(playerCardz, dealerCardz)
    noDuplicateCards(dealerCardz, playerCardz)
    return playerCardz, dealerCardz

def hitOrStand():
    done = False
    while not done:
        choice = input("You want to hit or stand?: ")
        if choice.lower() == "hit" or choice.lower() == "stand":
            done = True
            return choice
        else:
            print('Please type "hit" or "stand".')

def sumOfCards(cards = ()):
    total = []
    for i in range(len(cards)):
        total.append(int(cards[i][1]))
    if 1 in total and sum(total) + 10 <= 21:
        return sum(total) + 10
    else:
        return sum(total)

def printSum(cards = ()):
    total = []
    for i in range(len(cards)):
        total.append(int(cards[i][1]))
    if 1 in total and sum(total) + 10 <= 21:
        print(f"{sum(total)} or {sum(total) + 10}")
    else:
        print(f"{sum(total)}")

def playOrNot():
    yesOrNo = str(input("Want to keep playing?\nY / N: "))
    if yesOrNo.lower() == 'y':
        return True
    else:
        print("Thank you for playing!")
        return False

yourBalance = 1000

def isItANatural(playerCards, dealerCards):
    if sumOfCards(playerCards) == 21 and sumOfCards(dealerCards) != 21:
        print(f"Natural Blackjack! You just won 1,5x your bet ammount!")
        global yourBalance, playerBet
        yourBalance += 1.5 * playerBet
        gamemode = playOrNot()
        return True
    else:
        return False
gamemode = True
while gamemode:
    print(f"Your available balance is {yourBalance} \nPlace your bet: ")
    betSet = False
    while not betSet:
        try:
            playerBet = int(input())
            if playerBet > yourBalance:
                print(f"This is more than what you currently have. You have {yourBalance} and you bet {playerBet}.\n"
                      f"Please type a number greater or equal to {yourBalance}.\n")
                continue
        except:
            print(f"Please enter an integer lower or the same as {yourBalance}")
            continue
        betSet = True

    playerCards = []
    dealerCards = []
    firstHand(playerCards, dealerCards)
    print(f"Your cards are:")
    for i in range(len(playerCards)):
        print(playerCards[i][0])
    printSum(playerCards)
    print(f"The dealer's first card is {dealerCards[0][0]}")
    print(f"{dealerCards[0][1]}")
    natural = isItANatural(playerCards, dealerCards)
    while sumOfCards(playerCards) < 21 and not natural:
        choice = hitOrStand()
        if choice.lower() == "hit":
            noDuplicateCards(playerCards, dealerCards)
            print(f"Your new card is: {playerCards[-1][0]}")
            print(f"Your new sum is: {sumOfCards(playerCards)}")
        elif choice.lower() == "stand":
            if sumOfCards(playerCards) == sumOfCards(dealerCards) and dealerCantDraw(dealerCards):
                print(f"It's a draw.")
                gamemode = playOrNot()
                break
            elif sumOfCards(playerCards) > sumOfCards(dealerCards) and dealerCantDraw(dealerCards):
                print(f"Your sum is {sumOfCards(playerCards)} and the dealer's sum is {sumOfCards(dealerCards)}\n"
                    f"Dealer can't draw anymore, you win!")
                yourBalance += playerBet
                gamemode = playOrNot()
                break
            elif sumOfCards(playerCards) < sumOfCards(dealerCards) and dealerCantDraw(dealerCards):
                print(
                    f"Your sum: {sumOfCards(playerCards)} is lower than the dealer's sum: {sumOfCards(dealerCards)}\n"
                    f"You lose!")
                yourBalance -= playerBet
                gamemode = playOrNot()
                break
            elif not dealerCantDraw(dealerCards):
                while sumOfCards(dealerCards) < 17:
                    dealersHand(dealerCards)
                if isDealerBust(dealerCards):
                    print(f"You Win! Dealer went bust ({sumOfCards(dealerCards)})!")
                    yourBalance += playerBet
                    gamemode = playOrNot()
                    break
                elif sumOfCards(dealerCards) > sumOfCards(playerCards):
                    print(f"You lose! Dealer's amount is {sumOfCards(dealerCards)} and yours is {sumOfCards(playerCards)}")
                    yourBalance -= playerBet
                    gamemode = playOrNot()
                    break
                elif sumOfCards(dealerCards) < sumOfCards(playerCards):
                    print(f"You win! Dealer's amount is {sumOfCards(dealerCards)} and yours is {sumOfCards(playerCards)}!")
                    yourBalance += playerBet
                    gamemode = playOrNot()
                    break
                elif sumOfCards(dealerCards) == sumOfCards(playerCards):
                    print("It's a draw")
                    gamemode = playOrNot()
                    break
    if sumOfCards(playerCards) == 21 and not isItANatural(playerCards, dealerCards):
        if dealerCantDraw(dealerCards):
            print(f"BlackJack! You win this round! Dealers total is ({sumOfCards(dealerCards)}) and he can't draw more cards.")
            yourBalance += playerBet
            gamemode = playOrNot()
            break
        else:
            while sumOfCards(dealerCards) < 17:
                dealersHand(dealerCards)
            if sumOfCards(dealerCards) < 21:
                print(f"BlackJack! You win this round! Dealer reached only {sumOfCards(dealerCards)} and can't draw anymore!")
                yourBalance += playerBet
                gamemode = playOrNot()
                break
            elif sumOfCards(dealerCards) == 21:
                print(f"Both the dealer and you have 21! It's a draw.")
                gamemode = playOrNot()
                break
            elif sumOfCards(dealerCards) > 21:
                print(f"Dealer went bust ({sumOfCards(dealerCards)})! You win!")
                yourBalance += playerBet
                gamemode = playOrNot()
                break

    elif sumOfCards(playerCards) > 21:
        yourBalance -= playerBet
        print(f"Bust! You scored {sumOfCards(playerCards)}")
        if yourBalance > 0:
            gamemode = playOrNot()
        elif yourBalance <= 0:
            print("Your available balance is 0 or below. The game will now exit. Thank you for playing.")
            gamemode = False

gamemode = False