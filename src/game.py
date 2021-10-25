import random
import cardvalue as CV
types = [CV.CardValue.UNTER,CV.CardValue.OBER,CV.CardValue.KÖNIG,CV.CardValue.ZEHNER,CV.CardValue.SAU]
colours = [CV.CardColour.HERZ,CV.CardColour.EICHEL,CV.CardColour.GRÜN,CV.CardColour.SCHELLEN]

cards = []
atout = None

for col in colours:
    for type in types:
        cards.append((type,col))

player1_cards = []
player2_cards = []

round = 0

def hand_out_cards(player_cards):
    while(len(player_cards) < 7):
        j = random.randrange(0,len(cards))
        player_cards.append(cards[j])
        cards.remove(cards[j])

def choose_atout():
    j = random.randrange(0,len(cards))
    atout = cards[j]
    cards.remove(cards[j])
    
hand_out_cards(player1_cards)
print(player1_cards)
card = ("Unter", "Grün")

def play(card1,card2):
    if(card2[1] != card1[1] & card2[1] != atout[1]):
        return 1


    if(card1[1] == atout[1] & card2[1] == atout[1]):
        if(card1[0] > card2[0]):
            return 1
        else: 
            return -1
    elif(card1[1] == atout[1]):
        return 1
    elif(card2[1] == atout[1]):
        return -1
    else:
        if(card1[0] > card2[0]):
            return 1
        else: 
            return -1        


    