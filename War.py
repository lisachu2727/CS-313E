#File: War.py
#Description: HW 3
#Student's Name: Lisa Chu
#Student's UT EID: tc29328
#Course Name: CS 313E
#Unique Number: 50739
#
#Date Created: 2/23/2019
#Date Last Modified: 3/1/19

#importing random class to use shuffle
import random

#creating card class
class Card:
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
        #defining value to compare cards
        self.value = Deck.rankList.index(self.rank)

    def __str__(self):
        return self.rank + self.suit

#creating deck class
class Deck:
    def __init__(self):
        self.cardList = []

        suitList = ['C', 'D', 'H', 'S']
        Deck.rankList = ['2', '3', '4', '5', '6', '7', '8', '9', '10', \
                         'J', 'Q', 'K', 'A']

        #creating 52 card objects
        for suit in suitList:
            for rank in Deck.rankList:
                newCard = Card(rank, suit)
                self.cardList.append(newCard)

    #printing cards in a 4x13 array       
    def __str__(self):
        i = 0
        for card in self.cardList:
            print('%+4s'%(str(card)), end = '')
            i += 1
            if i % 13 == 0:
                print('\n', end = '')
        return ''
                  
    def shuffle(self):
        random.shuffle(self.cardList)

    #taking top card from deck and adding it to player's hand
    def dealOne(self, player):
        player.hand.append(self.cardList.pop(0))
        
        #updating player's hand total
        player.handTotal += 1

#creating player class
class Player:
    def __init__(self):
        self.hand = []
        self.handTotal = 0

    #printing cards in hand in a 4x13 array
    def __str__(self):
        i = 0
        for card in self.hand:
            print('%+4s'%(str(card)), end = '')
            i += 1
            if i % 13 == 0:
                print('\n', end = '')
        return ''

def playGame(deck, player1, player2):
    roundCount = 1

    print('\n')
    print('Initial hands:')
    print('Player 1:')
    print(player1)
    print()
    print('Player 2:')
    print(player2)
    print()
    print()

    #checking whether players have enough cards to do initial comparison
    while len(player1.hand) > 0 and len(player2.hand) > 0:
        print('ROUND ',roundCount,':', sep = '')
        print('Player 1 plays:','%+3s'%player1.hand[0])
        print('Player 2 plays:','%+3s'%player2.hand[0])
        print()

        #if player 2 has a higher rank card
        if player1.hand[0].value < player2.hand[0].value:
            print('Player 2 wins round ', roundCount,': ', \
                  '%+3s'%player2.hand[0], ' > ','%+3s'%player1.hand[0], sep = '')
            print()
            player2.hand.append(player1.hand.pop(0))
            player2.hand.append(player2.hand.pop(0))
            player1.handTotal -= 1
            player2.handTotal += 1

        #if player 1 has a higher rank card
        elif player1.hand[0].value > player2.hand[0].value:
            print('Player 1 wins round ', roundCount,': ', \
                  '%+3s'%player1.hand[0], ' > ','%+3s'%player2.hand[0], sep = '')
            print()
            player1.hand.append(player1.hand.pop(0))
            player1.hand.append(player2.hand.pop(0))
            player1.handTotal += 1
            player2.handTotal -= 1

        #if players have equal rank cards       
        elif player1.hand[0].value == player2.hand[0].value:
            print('War starts:','%+3s'%player1.hand[0], '=', \
                  '%+3s'%player2.hand[0], sep =' ')

            #loop war while player cards are equal
            while player1.hand[0].value == player2.hand[0].value:
                
                #checking to see if players have enough cards to declare war
                if len(player1.hand) >= 4 and len(player2.hand) >= 4:
                    print('Player 1 puts','%+3s'%player1.hand[1], 'face down')
                    print('Player 2 puts','%+3s'%player2.hand[1], 'face down')
                    print('Player 1 puts','%+3s'%player1.hand[2], 'face down')
                    print('Player 2 puts','%+3s'%player2.hand[2], 'face down')
                    print('Player 1 puts','%+3s'%player1.hand[3], 'face down')
                    print('Player 2 puts','%+3s'%player2.hand[3], 'face down')
                    print('Player 1 puts','%+3s'%player1.hand[4], 'face up')
                    print('Player 2 puts','%+3s'%player2.hand[4], 'face up')
                    print()

                #if player 2 has a higher rank card
                if player1.hand[4].value < player2.hand[4].value:
                    print('Player 2 wins round ', roundCount,': ', \
                          '%+3s'%player2.hand[4], ' > ','%+3s'%player1.hand[4], '\n', \
                          sep = '')
        
                    for i in range(5):                   
                        player2.hand.append(player1.hand.pop(0))
                    for i in range(5):
                        player2.hand.append(player2.hand.pop(0))

                    player1.handTotal -= 5
                    player2.handTotal += 5

                #if player 1 has a higher rank card
                elif player1.hand[4].value > player2.hand[4].value:
                    print('Player 1 wins round ', roundCount, ': ', \
                          '%+3s'%player1.hand[4], ' > ','%+3s'%player2.hand[4], '\n', \
                          sep = '')
                    
                    for i in range(5):
                        player1.hand.append(player1.hand.pop(0))
                    for i in range(5):
                        player1.hand.append(player2.hand.pop(0))

                    player1.handTotal += 5
                    player2.handTotal -= 5
                    
        roundCount += 1

        #printing out current hands of both players
        print('Player 1 now has',player1.handTotal,'card(s) in hand:')
        print(player1)     
        print('Player 2 now has',player2.handTotal,'card(s) in hand:')
        print(player2)
        print()
        print()

    #testing to see who wins at the end
    if len(player1.hand) > len(player2.hand):
        print('Game over.  Player 1 wins!')
    else:
        print('Game over.  Player 2 wins!')
      
def main():

    cardDeck = Deck()               # create a deck of 52 cards called "cardDeck"
    print("Initial deck:")
    print(cardDeck)                 # print the deck so we can see that you built it correctly
    
    random.seed(15)                 # leave this in for grading purposes
    cardDeck.shuffle()              # shuffle the deck
    print("Shuffled deck:")
    print(cardDeck)                 # print the deck so we can see that your shuffle worked
    
    player1 = Player()              # create a player
    player2 = Player()              # create another player

    for i in range(26):             # deal 26 cards to each player, one at 
       cardDeck.dealOne(player1)    #   a time, alternating between players
       cardDeck.dealOne(player2)
    
    playGame(cardDeck,player1,player2)
    
    print ("\n\nFinal hands:")    
    print ("Player 1:")
    print (player1)                 # printing a player object should print that player's hand
    print ("\nPlayer 2:")
    print (player2)                 # one of these players will have all of the cards, the other none
    
main()
                

        

        
                
                
    
