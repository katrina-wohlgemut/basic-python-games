#!/usr/bin/env python
# coding: utf-8

# # President Card Game - Command-line Version

# In[163]:


# import libraries
import random


# In[164]:


def create_deck():
    '''
    Create card deck with appropriate types of cards.
    '''
    deck = []
    for i in range(13):
        deck.append(["spades", i+2])
        deck.append(["hearts", i+2])
        deck.append(["diamonds", i+2])
        deck.append(["clubs", i+2])
        
    return deck


# In[165]:


def deal_cards(n, deck):
    '''
    Return n cards from deck for player and remove cards from deck.
    '''
    cards = []
    num = int(52/n)
    for i in range(n):
        player_cards = random.sample(deck, num)
        cards.append(player_cards)
        for j in player_cards:
            deck.remove(j)
    
    return cards


# In[166]:


def display_cards(player_cards, name):
    '''
    Show cards given to the player.
    '''
    print(name, "here are your cards:")
    ind = 1
    for i in player_cards:
        print(ind, i)
        ind += 1
    


# In[167]:


def invalid(played):
    '''
    Check if numbers match on cards.
    '''
    num = played[0][1]
    
    for i in played:
        if i[1] != num:
            return True
    
        
    return False


# In[168]:


def alreadyChose(played, card):
    '''
    Make sure cards have not already been chosen.
    '''
    for i in played:
        if i == card:
            return True
        
    return False


# In[169]:


def pick_cards(player_cards, num_cards):
    '''
    Choose num_cards from player_cards. 
    Must choose a valid card.
    '''
    played = []
    length = len(player_cards)
    for i in range(num_cards):
        x = int(input("Enter card number: "))
        while x < 1 or x > length or alreadyChose(played, player_cards[x-1]):
            print("Invalid input.")
            x = int(input("Enter card number: "))
        played.append(player_cards[x-1])
        if player_cards[x-1][1] == 2 and i == num_cards - 2:
            break
            
    
    while invalid(played):
        print("Invalid cards.")
        played = pick_cards(player_cards, num_cards)
        
    return played


# In[170]:


def play_round(cards, player_turn, names, n):
    '''
    Play a single round of all players.
    '''
    print()
    print("Fresh round")
    print("Turn:", names[player_turn])
    display_cards(cards[player_turn], names[player_turn])
        
    num_cards = int(input("How many cards are you playing? "))
    while num_cards > 4 or num_cards < 1:
        print("Invalid number of cards.")
        num_cards = int(input("How many cards are you playing? "))
        
    played = pick_cards(cards[player_turn], num_cards)
    
    for i in played:
        cards[player_turn].remove(i)
    
    if len(cards[player_turn])==0:
        winner = player_turn
        return cards, player_turn, winner
        
    last_played = played[0][1]
    if last_played == 2:
        return cards, player_turn, -1
    end_at = player_turn
    if player_turn == n - 1:
        player_turn = 0
    else:
        player_turn += 1
    playing = []
    for i in range(n):
        playing.append(True)
        
    winner = -1
    print()
    
    # implement President rules
    while True:
        # update player turn
        while playing[player_turn] == False:
            if player_turn == n - 1:
                player_turn = 0
            else:
                player_turn += 1
            if player_turn == end_at:
                return cards, player_turn, winner
        if player_turn == end_at:
            return cards, player_turn, winner
        
        print("Turn:", names[player_turn])
        display_cards(cards[player_turn], names[player_turn])
        
        if len(cards[player_turn]) < num_cards:
            print(names[player_turn], "must pass.")
            choice = "pass"
        else:
            choice = input("Pass or play? ").lower()
            
        if choice == "pass":
            playing[player_turn] = False
            if player_turn == n - 1:
                player_turn = 0
            else:
                player_turn += 1
        elif choice == "play":
            played = pick_cards(cards[player_turn], num_cards)
            # 2 is special card
            if played[0][1] == 2:
                for i in played:
                    cards[player_turn].remove(i)
                if len(cards[player_turn])==0:
                    winner = player_turn
                    break
                return cards, player_turn, winner
            elif played[0][1] < last_played:
                print("Need higher cards.")
            # rule in President if you play same numbers
            elif played[0][1] == last_played:
                print()
                print("Burn!")
                for i in played:
                    cards[player_turn].remove(i)
                if len(cards[player_turn])==0:
                    winner = player_turn
                    break
                return cards, player_turn, winner
            else:
                for i in played:
                    cards[player_turn].remove(i)
                if len(cards[player_turn])==0:
                    winner = player_turn
                    return cards, player_turn, winner
                last_played = played[0][1]
                end_at = player_turn
                if player_turn == n - 1:
                    player_turn = 0
                else:
                    player_turn += 1
        else:
            print("Invalid input. Try again.")
        print()
        
        
     


# In[171]:


# set up game
deck = create_deck()
num = int(input("Enter the number of players (2-10): "))
while num > 10 or num < 2:
    print("Invalid number of players.")
    num = input("Enter the number of players (2-10): ")
cards = deal_cards(num, deck)
names = []
for i in range(num):
    print("Player", i)
    names.append(input("Please enter your name: "))
    print()
winner = -1
player_turn = 0
while winner == -1:
    cards, player_turn, winner = play_round(cards, player_turn, names, num)
print(names[winner], "won!")


# In[ ]:




