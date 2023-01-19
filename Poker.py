import random

class PokerGame:
  def __init__(self, players = 2):
    nums = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    suits = ['D', 'C', 'S', 'H']
    self.cards = []
    self.player_cards = []
    self.cards_on_table = []
    
    for x in range(0, len(suits)):
      for y in range(0, len(nums)):
        self.cards.append(nums[y]+suits[x])
    random.shuffle(self.cards)
    
    for x in range(0, players):
      self.player_cards.append([])

  def add_card(self, index):
    self.player_cards[index].append(self.cards.pop(0))

  def add_to_table(self):
    self.cards_on_table.append(self.cards.pop(0))
  
  
  def IsStraightFlush(self, cards):
    num, suit = splitter(cards)
    order = True
    same_suit = True
    for x in range(0, len(num)-1):
      if (num[x]!=num[x+1]-1):
        if (num[x]==1 and num[len(num)-1]==13):
          pass
        else:
          order = False
      if (suit[x]!=suit[x+1]):
        same_suit = False

    if (order == False or same_suit == False):
      return False
    else:
      return True

      
  def IsFourofaKind(self, cards):
    num, suit = splitter(cards)
    counter = 0
    bool = False
    for x in range(0, len(num)):
      for y in range(x, len(num)):
        if (num[x]==num[y]):
          counter+=1
      if (counter == 4):
        bool = True
        break
      else: 
        counter = 0
    return bool


  def IsFullHouse(self, cards):
    num, suit = splitter(cards)
    counter = 0
    bool = True
    for x in range(0, len(num)):
      for y in range(0, len(num)):
        if (num[x]==num[y]):
          counter+=1
      if (counter<=1):
        bool = False
        break
      counter = 0
    
    return bool
    
  def IsFlush(self, cards):
    num, suit = splitter(cards)
    same_suit = True
    for x in range(0, len(num)-1):
      if (suit[x]!=suit[x+1]):
        same_suit = False

    if (same_suit == False):
      return False
    else:
      return True

    
  def IsStraight(self, cards):
    num, suit = splitter(cards)
    order = True
    for x in range(0, len(num)-1):
      if (num[x]!=num[x+1]-1):
        if (num[x]==1 and num[len(num)-1]==13):
          pass
        else:
          order = False

    if (order == False):
      return False
    else:
      return True

    
  def IsThreeofaKind(self, cards):
    num, suit = splitter(cards)
    counter = 0
    bool = False
    for x in range(0, len(num)):
      for y in range(x, len(num)):
        if (num[x]==num[y]):
          counter+=1
      if (counter == 3):
        bool = True
        break
      else: 
        counter = 0
    return bool

    
  def IsTwoPairs(self, cards):
    num, suit = splitter(cards)
    counter = 0
    singles = []
    for x in range(0, len(num)):
      for y in range(0, len(num)):
        if (num[x]==num[y]):
          counter+=1
      if (counter<=1):
        singles.append(num[x])
      counter = 0

    if (len(singles)<=1):
      return True
    else:
      return False
    
  def IsOnePair(self, cards):
    num, suit = splitter(cards)
    counter = 0
    bool = False
    for x in range(0, len(num)):
      for y in range(x, len(num)):
        if (num[x]==num[y]):
          counter+=1
      if (counter == 2):
        bool = True
        break
      else: 
        counter = 0
    return bool


    

class TexasHoldem(PokerGame):
  def __init__(self, players = 2):
    PokerGame.__init__(self, players)

  def deal(self):
    for x in range(0, 2):
      for y in range(0, len(self.player_cards)):
        PokerGame.add_card(self, y)

    for x in range(0, 5):
      PokerGame.add_to_table(self)
    print(self.player_cards)
    print(self.cards_on_table)
    
  def hand(self):
    temp = []
    temp2 = []
    deck = []
    deck2 = []
    for w in range (0, len(self.player_cards)):
      temp = self.player_cards[w]+self.cards_on_table
      for x in range(0, len(temp)):
        for y in range(0, len(temp)):
          for z in range(0, len(temp)):
            if (z!=x and z!=y):
              temp2.append(temp[z])
          if (PokerGame.IsStraightFlush(self, temp2)==True):
            deck.append(8)
          elif (PokerGame.IsFourofaKind(self, temp2)==True):
            deck.append(7)
          elif (PokerGame.IsFullHouse(self, temp2)==True):
            deck.append(6)
          elif (PokerGame.IsFlush(self, temp2)==True):
            deck.append(5)
          elif (PokerGame.IsStraight(self, temp2)==True):
            deck.append(4)
          elif (PokerGame.IsThreeofaKind(self, temp2)==True):
            deck.append(3)
          elif (PokerGame.IsTwoPairs(self, temp2)==True):
            deck.append(2)
          elif (PokerGame.IsOnePair(self, temp2)==True):
            deck.append(1)
          temp2.clear()
      temp.clear()

      deck.sort(reverse=True)
      if(len(deck)!=0):
        if (deck[0]==8):
          deck2.append("Straight Flush")
        elif (deck[0]==7):
          deck2.append("Four of a Kind")
        elif (deck[0]==6):
          deck2.append("Full House")
        elif (deck[0]==5):
          deck2.append("Flush")
        elif (deck[0]==4):
          deck2.append("Straight")
        elif (deck[0]==3):
          deck2.append("Three of a Kind")
        elif (deck[0]==2):
          deck2.append("Two Pairs")
        elif (deck[0]==1):
          deck2.append("One Pair")
      else:
        deck2.append("High Cards")
      deck.clear() 
    print(deck2)
    
def splitter(cards):
  num = []
  suit = []
  for x in range(0, len(cards)):
    card = list(cards[x])
    num.append(card[0])
    suit.append(card[1])
  for x in range(0, len(num)):
    if (num[x]=="A"):
      num[x] = 1
    elif (num[x]=="T"):
      num[x] = 10
    elif (num[x]=="J"):
      num[x] = 11
    elif (num[x]=="Q"):
      num[x] = 12
    elif (num[x]=="K"):
      num[x] = 13
    else:
      num[x] = int(num[x])
  num.sort()
  suit.sort()

  return(num, suit)


