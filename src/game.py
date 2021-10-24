import random
types = ["Unter","Ober","Koenig","Zehn","Sau"]
colours = ["Herz","Grün","Eichel","Schellen"]

cards = []
atout = None

for col in colours:
    for type in types:
        cards.append((type,col))

player1_cards = []
player2_cards = []
round = 0

def hand_out_cards(player_cards):
    while(len(player_cards) < 4):
        j = random.randrange(0,len(cards))
        if(cards[j] in player1_cards):
            continue
        else:    
            player_cards.append(cards[j])    

def play(card1,card2):
    