#!/usr/bin/env python
# coding: utf-8

# # Uno User vs Computer Card Game - Command-line Version

# In[41]:


# import libraries
import random
import copy


# In[42]:


def create_deck():
    '''
    Create the classic Uno deck.
    '''
    deck = []
    for i in range(10):
        if i == 0:
            continue
        deck.append(['R', i])
        
    for i in range(10):
        if i == 0:
            continue
        deck.append(['Y', i])
        
    for i in range(10):
        if i == 0:
            continue
        deck.append(['G', i])
        
    for i in range(10):
        if i == 0:
            continue
        deck.append(['B', i])
      
    # S represents skip, C represents change direction, + represents adding cards
    deck.append(['RS', 0, True])
    deck.append(['RC', 0, True])
    deck.append(['R+', 2, True])
    deck.append(['YS', 0, True])
    deck.append(['YC', 0, True])
    deck.append(['Y+', 2, True])
    deck.append(['GS', 0, True])
    deck.append(['GC', 0, True])
    deck.append(['G+', 2, True])
    deck.append(['BS', 0, True])
    deck.append(['BC', 0, True])
    deck.append(['B+', 2, True])
    
    # A stands for all colours
    for i in range(4):
        deck.append(['A', 0])
        deck.append(['A+', 4, True])
        
    return deck


# In[43]:


def deal_cards(deck):
    '''
    Deal out 7 cards to a player
    '''
    player_cards_orig = random.sample(deck, 7)
    player_cards = copy.deepcopy(player_cards_orig)
    return player_cards


# In[44]:


def remove_cards(deck, player_cards):
    '''
    Remove the dealt cards from the deck
    '''
    for i in player_cards:
        deck.remove(i)
    return deck


# In[45]:


def cardInvalid(card_played, top_card):
    '''
    Check if the card played was invalid based on top card
    '''
    if len(card_played[0]) == 2:
        if card_played[0][0] == top_card[0][0] or (len(top_card[0]) == 2 and card_played[0][1] == top_card[0][1] and card_played[1] == top_card[1]) or card_played[0][0] == 'A':
            return False
        else:
            return True
    if len(top_card[0]) == 2:
        if card_played[0][0] == top_card[0][0] or (len(card_played[0]) == 2 and card_played[0][1] == top_card[0][1]) or card_played[0][0] == 'A':
            return False
        else:
            return True
        
    if (card_played[0][0] != top_card[0][0] and card_played[1] != top_card[1] and card_played[0][0] != 'A'):
        return True

    return False


# In[46]:


def print_cards(player_cards):
    '''
    Print out player_cards
    '''
    counter = 1
    for i in player_cards:
        print(counter, "[",i[0], i[1], "]")
        counter += 1


# In[47]:


def player_turn(deck, player_cards, top_card):
    '''
    Implement a single player turn
    deck: state of current deck
    player_cards: current player's cards
    top_card: most recently played card
    '''
    print("Here are your cards: ")
    print_cards(player_cards)
    print("The current top card is ", "[", top_card[0], top_card[1], "]")
    
    response = input("Do you want to play a card? (y/n) ")
    if response == 'y':
        card_num = int(input("Enter number of card: "))
        if card_num < 1 or card_num > len(player_cards):
            print("Invalid input. Try again.")
            return player_turn(deck, player_cards, top_card)
        card_played = player_cards[card_num - 1]
        
        if cardInvalid(card_played, top_card):
            print("Invalid card. Try again.")
            return player_turn(deck, player_cards, top_card)      
        
    elif response == 'n':
        print("You must pick up a card.")
    else:
        print("Incorrect input. Try again.")
        return player_turn(deck, player_cards, top_card)
        
        
    if response == 'y':
        player_cards.pop(card_num - 1)
        if card_played[0] == 'A' or card_played[0] == 'A+':
            colour = input("Which colour would you like? ")
            while colour != 'R' and colour != 'Y' and colour != 'G' and colour != 'B':
                print("Invalid input. Try again.")
                colour = input("Which colour would you like?")
                
        if card_played[0] == 'A':
            card_played[0] = colour
        elif card_played[0] == 'A+':
            card_played[0] = colour + '+'
    else:
        card_orig = random.sample(deck, 1)
        card = copy.deepcopy(card_orig)
        new_card = card[0]
        print("Your new card is: [", new_card[0], new_card[1], "]")
        deck.remove(new_card)
        player_cards.append(new_card)
        card_played = top_card
        
    print("Your cards are now: ")
    print_cards(player_cards)
        
    return deck, player_cards, card_played


# In[48]:


def computer_turn(deck, player_cards, top_card):
    '''
    Implement the computer's turn by playing the first valid card to play
    '''
    played = False
    card_num = 1
    for i in player_cards:
        if cardInvalid(i, top_card) == False:
            card_played = i
            played = True
            break
        card_num += 1
            
    if played:
        player_cards.pop(card_num - 1)
        while card_played[0][0] == 'A' and len(player_cards) > 0:
            if card_played[0] == 'A':
                card_played[0] = player_cards[0][0][0]
            elif card_played[0] == 'A+':
                card_played[0] = player_cards[0][0][0] + '+'
        if card_played[0] == 'A':
            card_played[0] = 'R'
        elif card_played[0] == 'A+':
            card_played[0] = 'R+'
    else:
        card_orig = random.sample(deck, 1)
        card = copy.deepcopy(card_orig)
        new_card = card[0]
        deck.remove(new_card)
        player_cards.append(new_card)
        card_played = top_card
        
    return deck, player_cards, card_played
    
    


# In[49]:


def play(deck, player1_cards, player2_cards, top_card):
    '''
    Play a turn based on player and computer cards
    '''
    done = False
    player = 1
    
    while done == False:
        print()
        # skip turn
        if len(top_card[0]) > 1 and top_card[0][1] == 'S' and top_card[2] == True:
            if player == 1:
                player = 2
            elif player == 2:
                player = 1
            top_card[2] = False
        # change direction
        elif len(top_card[0]) > 1 and top_card[0][1] == 'C' and top_card[2] == True:
            if player == 1:
                player = 2
            elif player == 2:
                player = 1
            top_card[2] = False
        # pick up
        elif len(top_card[0]) > 1 and top_card[0][1] == '+' and top_card[2] == True:
            if player == 1:
                print("Pick up", top_card[1])
                cards_orig = random.sample(deck, top_card[1])
                cards = copy.deepcopy(cards_orig)
                for i in range(top_card[1]):
                    deck.remove(cards[i])
                    player1_cards.append(cards[i])
                print("Player1 cards are now:")
                print_cards(player1_cards)
                player = 2
            else:
                cards_orig = random.sample(deck, top_card[1])
                cards = copy.deepcopy(cards_orig)
                for i in range(top_card[1]):
                    deck.remove(cards[i])
                    player2_cards.append(cards[i])
                player = 1
            top_card[2] = False
            print()
            
                
        if player == 1:
            print("Player 1 turn")
            deck, player1_cards, top_card = player_turn(deck, player1_cards, top_card)
            num_cards = len(player1_cards)
            if num_cards == 1:
                print("Player1 has UNO")
            elif num_cards == 0:
                print("Player1 won!")
                done = True
            player = 2
        else:
            print("Computer turn")
            deck, player2_cards, top_card = computer_turn(deck, player2_cards, top_card)
            num_cards = len(player2_cards)
            if num_cards == 1:
                print("Computer has UNO")
            elif num_cards == 0:
                print("Computer won!")
                done = True
            player = 1
            
        if len(deck) == 0:
            print("Ran out of cards!")
            deck = create_deck()
            for i in player1_cards:
                deck.remove(i)
            for i in player2_cards:
                deck.remove(i)
            deck.remove(top_card)


# In[50]:


# set up and play game
deck = create_deck()
player1_cards = deal_cards(deck)
deck = remove_cards(deck, player1_cards)
player2_cards = deal_cards(deck)
deck = remove_cards(deck, player2_cards)
list_card = random.sample(deck, 1)
top_card = list_card[0]
deck.remove(top_card)
while top_card[0][0] == 'A':
    list_card = random.sample(deck, 1)
    top_card = list_card[0]
    deck.remove(top_card)
play(deck, player1_cards, player2_cards, top_card)


# In[ ]:




