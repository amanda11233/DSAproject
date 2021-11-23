SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 700
CARD_SCALE = 0.6


CARD_WIDTH = 140 * CARD_SCALE
CARD_HEIGHT = 190 * CARD_SCALE



MAT_PERCENT_OVERSIZE = 1.25
MAT_HEIGHT = int(CARD_HEIGHT * MAT_PERCENT_OVERSIZE)
MAT_WIDTH = int(CARD_WIDTH * MAT_PERCENT_OVERSIZE)


VERTICAL_MARGIN_PERCENT = 0.10
HORIZONTAL_MARGIN_PERCENT = 0.10


BOTTOM_Y = MAT_HEIGHT / 2 + MAT_HEIGHT * VERTICAL_MARGIN_PERCENT

START_X  = MAT_WIDTH / 2 + MAT_WIDTH * HORIZONTAL_MARGIN_PERCENT

CARD_VALUES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10" ,"J", "Q", "K"]
CARD_SUITS = ["Clubs", "Hearts", "Spades", "Diamonds"]

#storing the real time values of the card
CARD_REAL_VALUES = { "A" : 20 , "2" : 2, "3": 3, "4" : 4 , "5" : 5, "6": 6, "7": 7, "8": 8, "9":9, "10": 10, "J" : 11, "Q" : 12, "K" : 13}

# Y of the top row
TOP_Y = SCREEN_HEIGHT - MAT_HEIGHT / 2 - MAT_HEIGHT * VERTICAL_MARGIN_PERCENT

# Y of the middle row
MIDDLE_Y = TOP_Y - MAT_HEIGHT - MAT_HEIGHT * VERTICAL_MARGIN_PERCENT

# How far apart each pile goes
X_SPACING = MAT_WIDTH + MAT_WIDTH * HORIZONTAL_MARGIN_PERCENT


CARD_VERTICAL_OFFSET = CARD_HEIGHT * CARD_SCALE * 0.3

PILE_COUNT = 8
BOTTOM_FACE_DOWN_PILE = 7
BOTTOM_FACE_UP_PILE = 11
PLAY_PILE_1 = 1
PLAY_PILE_2 = 3
PLAY_PILE_3 = 4
PLAY_PILE_4 = 5
PLAY_PILE_5 = 6
PLAY_PILE_6 = 7
PLAY_PILE_7 = 100
TOP_PILE_1 = 9
TOP_PILE_2 = 10
TOP_PILE_3 = 11
TOP_PILE_4 = 12


BUTTON_POSITION = MAT_HEIGHT / 2 + MAT_HEIGHT * VERTICAL_MARGIN_PERCENT

FACE_DOWN_IMAGE = ":resources:images/cards/cardBack_red2.png"

TRIALS = {
    1 : ["D#A,C#A,H#A"],
    2 : ["D#K,C#K,H#K"],
    3 : ["D#Q,C#Q,H#Q"],
    4 : ["D#J,C#J,H#J"],
    5 : ["D#10,C#10,H#10"],
    6 : ["D#9,C#9,H#9"],
    7 : ["D#8,C#8,H#8"],
    8 : ["D#7,C#7,H#7"],
    9 : ["D#6,C#6,H#6"],
    10 : ["D#5,C#5,H#5"],
    11 : ["D#4,C#4,H#4"],
    12 : ["D#3,C#3,H#3"],
    13 : ["D#2,C#2,H#2"]
}


RUNS = {
    1 : ["A,K,Q"],
    2 : ["A,2,3"],
    3 : ["J,Q,K"],
    4 : ["10,J,Q"],
    5 : ["9,10,J"],
    6 : ["8,9,10"],
    7 : ["7,8,9"],
    8 : ["6,7,8"],
    9 : ["5,6,7"],
    10 : ["4,5,6"],
    11 : ["3,4,5"],
    12 : ["2,3,4"],
}

COLORS = {
    1 : ["D,D,D"],
    2 : ["H,H,H"],
    3 : ["C,C,C"],
    4 : ["S,S,S"], 
 }
 


 