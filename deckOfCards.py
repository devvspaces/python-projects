import random
class Card(object):
	def __init__(self,value,suit):
		self.value=value
		self.suit=suit
	def show(self):
		print(f"{self.value} of {self.suit}")

class Deck(object):
	def __init__(self):
		self.cards=[]
		self.build()
	def build(self):
		for i in ["Spades","Clubs","Diamonds","Hearts"]:
			for j in range(1,14):
				self.cards.append(Card(j,i))
		random.shuffle(self.cards)
	def showDeck(self):
		for i in self.cards:
			i.show()
	def draw(self):
		return self.cards.pop()
	def __len__(self):
		return len(self.cards)

class Player(object):
	def __init__(self,deck,name=None):
		self.num=4
		if name==None:
			self.num=1
		self.hand=[]
		self.name=name
		self.deck=deck
		self.build()
	def drawDeck(self):
		self.hand.append(self.deck.draw())
		return self
		
	def build(self):
		for i in range(self.num):
			self.drawDeck()
			
	def showHand(self):
		for a,i in enumerate(self.hand):
			print(a)
			i.show()

deck=Deck()
print("1. Play with computer")
print("2. Show Deck")
x=eval(input("Give me your option: "))
if x==1:
	name=input("Your name: ")
	player=Player(deck,name)
	computer=Player(deck,"AI")
	played=Player(deck)
	toss=random.randint(0,1)
	win="None"
	while win=="None":
		c=len(played.hand)
		card1=played.hand[c-1]
		print("Down card is: ")
		card1.show()
		cardN=card1.value
		cardS=card1.suit
		if toss%2==0:
			print("Computers turn")
			for i in computer.hand:
				if i.value==cardN or i.suit == cardS:
					played.hand.append(i)
					computer.hand.remove(i)
					break
			else:
				computer.drawDeck()
			if len(computer.hand)==0:
				win=="Computer"
		else:
			print(f'{name} turn')
			print("Select the card you want to play, if you are not playing input 'q'")
			player.showHand()
			q="q"
			p=eval(input("Selected option :"))
			if p!="q":
				picked=player.hand[p]
				if picked.value!=cardN and picked.suit != cardS:
					print("Can't play card")
				else:
					played.hand.append(picked)
					player.hand.remove(picked)
			else:
				player.drawDeck()
				
		if len(player.hand)==0:
			win="Player"
		if len(deck)==0:
			win="Draw"
			
		toss+=1
	print(win)
else:
	deck.showDeck()