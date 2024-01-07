# Реализуйте итератор колоды карт (52 штуки) CardDeck. Каждая
# карта представлена в виде строки типа 2 Пик. При вызове
# функции next() будет представлена следующая карта. По
# окончании перебора всех элементов возникнет
# ошибка StopIteration.

class CardDeck:
    def __init__(self):
        self.length = 52
        self.index = 0
        self.__SUITS = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
        self.__RANKS = [*range(2, 11), 'J', 'Q', 'K', 'A']
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.length:
            rank = self.index % len(self.__RANKS)
            suit = self.index % len(self.__SUITS)
            card = f'{self.__RANKS[rank]} of {self.__SUITS[suit]}'
            self.index += 1
            return card 
        else:
            raise StopIteration
                   
        

deck = CardDeck()

for card in deck:
    print(card)
