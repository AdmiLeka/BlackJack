# BlackJack
The game BlackJack made in Python
This is what it looks like

![Screenshot 2022-08-17 211406](https://user-images.githubusercontent.com/95366089/185224629-65e628b9-e7e5-4f18-abaa-424cc257c6a3.png)

I stored the card symbols in a list, and the values in a dictionary
```
deck_symbol = ["Clubs", "Diamonds", "Spades", "Hearts"]
deck_number_dict = {"Ace": 1, "Two": 2, "Three": 3,
                    "Four": 4, "Five": 5, "Six": 6,
                    "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10,
                    "Jack": 10, "Queen": 10, "King": 10}                    
```
I created a Card Class that produced a random card with a "generateCard" function i wrote
```
16
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
```
In order to not have duplicate cards between the player and the dealer, I wrote this function
```
def noDuplicateCards(appendTo, checkHereToo):
    newCard = generateCard()
    while newCard in appendTo or newCard in checkHereToo:
        newCard = generateCard()
    appendTo.append(newCard)
    return appendTo
```
More in-game pictures

![Screenshot 2022-08-17 211316](https://user-images.githubusercontent.com/95366089/185224655-52a578d7-55ef-4dcd-be19-4ef470cf83df.png)

![Screenshot 2022-08-17 211217](https://user-images.githubusercontent.com/95366089/185224670-24080751-f926-47a2-beac-526d21e960c2.png)
