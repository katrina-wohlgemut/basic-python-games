#!/usr/bin/env python
# coding: utf-8

# # War Card Game

# In[190]:


# import libraries
import random


# In[191]:


def make_deck():
    '''
    Create classic card deck.
    '''
    deck = []
    for i in range(15):
        if i == 0:
            continue
        deck.append(["clubs", i])
        deck.append(["spades", i])
        deck.append(["hearts", i])
        deck.append(["diamonds", i])
    return deck      


# In[192]:


def deal(n, deck):
    '''
    Return n random cards from deck.
    '''
    player_cards = random.sample(deck, n)
    for i in player_cards:
        deck.remove(i)
    
    return deck, player_cards


# In[193]:


def deal_cards(n, deck):
    '''
    Give each player n cards from the deck.
    '''
    num = int(52 / n)
    player = []
    for i in range(n):
        deck, player_cards = deal(num, deck)
        player.append(player_cards)
    
    return player, deck, num


# In[194]:


def findMax(arr):
    '''
    Determine which card is the highest in arr.
    '''
    m = arr[0]
    ind = 0
    count = 0
    

    for i in arr:
        if i[1] > m[1]:
            m = i
            ind = count
        count += 1

    count = 0
    for i in arr:
        if i[1] == m[1]:
            count += 1
    if count > 1:
        return -1
    else:
        return ind


# In[195]:


def maxScore(arr):
    '''
    Determine max number out of arr
    '''
    ind = 0
    m = arr[0]
    count = 0
    for i in arr:
        if i > m:
            ind = count
            m = i
        count += 1
    return ind


# In[196]:


def player_turn(player_cards):
    '''
    Play a single turn for a player with player_cards
    '''
    print("Here are your cards:")
    index = 1
    for i in player_cards:
        print(index, end ="")
        print(i)
        index += 1
    card_num = int(input("Which card would you like to play? "))
    if card_num < 1 or card_num > len(player_cards):
        print("Invalid input. Please try again.")
        return player_turn(player_cards)
    else:
        card = player_cards[card_num - 1]
        player_cards.remove(card)
        return player_cards, card
        
    


# In[197]:


def play(player, n, num):
    '''
    Play the game num times with n players and find overall winner
    '''
    
    points = []
    pts = n
    for i in range(n):
        points.append(0)
    for i in range(num):
        played = []
        for i in range(n):
            print()
            print("Player", i+1, "turn")
            player[i], card = player_turn(player[i])
            played.append(card)
        winner = findMax(played)
        if winner == -1:
            print()
            print("Tie")
            pts += n
        else:
            print()
            print("The winner is Player", winner+1)
            points[winner] += pts
            pts = n
        
    winner = maxScore(points)
    print("Player", winner + 1, "won!")
        


# deck = make_deck()
# n = int(input("How many players are playing? "))
# player, deck, num = deal_cards(n, deck)
# play(player, n, num)
