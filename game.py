import arcade 
from constants import  CARD_REAL_VALUES, BOTTOM_FACE_DOWN_PILE, PILE_COUNT, TOP_PILE_1, TOP_PILE_4 , CARD_VERTICAL_OFFSET, PLAY_PILE_1, PLAY_PILE_7, MAT_WIDTH, MAT_HEIGHT,  X_SPACING, MIDDLE_Y,  TOP_Y, START_X, BOTTOM_Y, CARD_SCALE, CARD_HEIGHT, CARD_SUITS, CARD_VALUES, CARD_WIDTH
from cards import Card
import arcade.gui
from time import time
import random
from binaryTree import Node, BinaryTree

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Simple Card Game"


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.AMAZON)
        self.card_list = None
        self.real_card_list = None
        self.binaryTree = None
        self.real_cards = None 
        self.held_cards = None
        self.held_cards_original_position = None
        self.pile_mat_list = None
        self.piles = None
        self.pile_array = None
        self.isShuffled = False
        self.isPlayed = False
        self.sel_winner = None
        self.play_cards= None
        self.shuffle_cards = None

    def get_pile_for_card(self, card):
        for index, pile in enumerate(self.piles):
            if card in pile:
                return index

    def remove_card_from_pile(self, card):
        for pile in self.piles:
            if card in pile:
                pile.remove(card)
                break

    def move_card_to_new_pile(self, card, pile_index):
        """ Move the card to a new pile """
        self.remove_card_from_pile(card)
        self.piles[pile_index].append(card)

       

    def setup(self):
        self.binaryTree = BinaryTree()
        self.card_list = arcade.SpriteList()
 

        self.held_cards = [] 
        self.held_cards_original_position = []

        self.pile_mat_list: arcade.SpriteList = arcade.SpriteList()

        pile = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)
        self.pile_array = []
        self.real_cards = {"Hearts" : [], "Clubs": [], "Spades": [], "Diamonds" : []}
        self.real_card_list = []
        # pile.position = START_X + X_SPACING, BOTTOM_Y
        # self.pile_mat_list.append(pile)
        self.piles = [[] for _ in range(PILE_COUNT)]
        for card in self.card_list:
            self.piles[BOTTOM_FACE_DOWN_PILE].append(card)

        for i in range(4):
            pile = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)
            pile.position = START_X + i * X_SPACING, TOP_Y
            self.pile_mat_list.append(pile)

        # for i in range(7):
        #     pile = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)
        #     pile.position = START_X + i * X_SPACING, MIDDLE_Y
        #     self.pile_mat_list.append(pile)
        
        self.uimanager = arcade.gui.UIManager()
        self.uimanager.enable()
        self.v_box = arcade.gui.UIBoxLayout()
        self.uimanager2 = arcade.gui.UIManager()
        self.uimanager2.disable()

        self.shuffle_cards = arcade.gui.UIFlatButton(text="Shuffle Cards",
                                        width=200)
        self.shuffle_cards.on_click = self.on_click_sort

        self.play_cards = arcade.gui.UIFlatButton(text="Play Cards",
                                        width=200)

        self.sel_winner = arcade.gui.UIFlatButton(text="View Winner",
                                        width=150)
        if (self.isShuffled == True):
           self.play_cards.on_click = self.play_cards_fun

        self.v_box.add(self.shuffle_cards .with_space_around(bottom=20, right = 200))
        self.v_box.add(self.play_cards.with_space_around(bottom=20, right = 200))

        self.uimanager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="right",
                anchor_y="bottom",
                child=self.v_box)
                
        )
        self.uimanager2.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="right",
                anchor_y="bottom",
                child=self.sel_winner.with_space_around(bottom=20, right = 10))
                
        )

        for card_suit in CARD_SUITS:
            for card_value in CARD_VALUES:
                card = Card(card_suit, card_value, CARD_SCALE)
                card.position = START_X, BOTTOM_Y
                card_value = card.value

                # if(card_value == "A"):
                #     card_value = "1"
                # elif card_value == "J":
                #     card_value = "11"
                # elif card_value == "Q":
                #     card_value = "12"
                # elif card_value == "K":
                #     card_value = "13"
                
                # card_value = int(card_value)

                if card.suit == "Hearts":
                    sticker = "H#"
                elif card.suit == "Clubs":
                    sticker = "C#"
                elif card.suit == "Spades":
                    sticker = "S#"
                elif card.suit == "Diamonds":
                    sticker = "D#" 
                                

                real_card_value = sticker + card.value   
 
                self.binaryTree.insert(Node(real_card_value)) 
                self.real_cards[card.suit].append(card_value)
                self.real_card_list.append(real_card_value)
                self.card_list.append(card)

        # print(self.real_card_list)

        

    def play_cards_fun(self, event):
        self.shuffle_cards.on_click = None
        self.uimanager2.enable()
        for n_cards in range(3):
            for idx, pile in enumerate(self.pile_mat_list): 
                cards = arcade.get_sprites_at_point((START_X, BOTTOM_Y), self.card_list)

                if(len(cards) > 0):
                    primary_card = cards[-1]
                    self.held_cards = [primary_card] 
                    self.pull_to_top(self.held_cards[0])
                    self.held_cards[0].position = pile.position
                

                if len(self.piles[idx]) > 0:
                # Move cards to proper position 
                    top_card = self.piles[idx][-1] 
                    for i, dropped_card in enumerate(self.held_cards):
                        dropped_card.position = top_card.center_x, \
                                                top_card.center_y - CARD_VERTICAL_OFFSET * (i + 1)
                else:
                    # Are there no cards in the middle play pile?
                    for i, dropped_card in enumerate(self.held_cards):
                        # Move cards to proper position
                        dropped_card.position = pile.center_x, \
                                                pile.center_y - CARD_VERTICAL_OFFSET * i
                
                for card in self.held_cards: 
                    # Cards are in the right position, but we need to move them to the right list
                    self.move_card_to_new_pile(card, idx)

                for card in self.piles[idx]:
                    card.face_up()

                self.held_cards = [] 

    def on_click_sort(self, event):
        # print(self.binaryTree.search(self.binaryTree.Node, "H#A"))
        for pos1 in range(len(self.card_list)):
            pos2 = random.randrange(len(self.card_list)) 
            #Place where we can use searching algorithms
            self.real_card_list[pos1], self.real_card_list[pos2] = self.real_card_list[pos2], self.real_card_list[pos1] 
            self.card_list.swap(pos1, pos2)
     
        
        if(self.card_list[-1].position == START_X, BOTTOM_Y):
            self.pull_to_top(self.card_list[-1])
        
        self.play_cards.on_click = self.play_cards_fun
        # print(self.card_list[-1].position)

                
    def on_draw(self):
        arcade.start_render()
        self.pile_mat_list.draw()
        self.card_list.draw()
        self.uimanager.draw()
        self.uimanager2.draw()

    def on_mouse_press(self, x, y, button, key_modifiers):
        cards = arcade.get_sprites_at_point((x, y), self.card_list)

        if(len(cards) > 0):
            primary_card = cards[-1]
            self.held_cards = [primary_card]
            self.held_cards_original_position = [self.held_cards[0].position]
            self.pull_to_top(self.held_cards[0])


    def on_mouse_motion(self, x:float, y:float, dx:float, dy:float):
        for card in self.held_cards:
            card.center_x += dx
            card.center_y += dy

    def on_mouse_release(self, x:float, y:float, button : int, modifiers: int):
        pass
        # if(len(self.held_cards) == 0): 
        #     return
        
        # pile, distance = arcade.get_closest_sprite(self.held_cards[0], self.pile_mat_list)
        # self.reset_position = True 
        
        # if arcade.check_for_collision(self.held_cards[0], pile):

        #     # What pile is it?
        #     pile_index = self.pile_mat_list.index(pile) 
        #     # print(pile_index)
        #     #  Is it the same pile we came from?
        #     if pile_index == self.get_pile_for_card(self.held_cards[0]):
        #         # If so, who cares. We'll just reset our position.
        #         pass
            
        #     elif PLAY_PILE_1 <= pile_index <= PLAY_PILE_7:
        #         # Are there already cards there?
        #         if len(self.piles[pile_index]) > 0:
        #             # Move cards to proper position
                    
        #             top_card = self.piles[pile_index][-1] 
        #             for i, dropped_card in enumerate(self.held_cards):
        #                 dropped_card.position = top_card.center_x, \
        #                                         top_card.center_y - CARD_VERTICAL_OFFSET * (i + 1)
        #         else:
        #             # Are there no cards in the middle play pile?
        #             for i, dropped_card in enumerate(self.held_cards):
        #                 # Move cards to proper position
        #                 dropped_card.position = pile.center_x, \
        #                                         pile.center_y - CARD_VERTICAL_OFFSET * i

        #         for card in self.held_cards:
        #             # Cards are in the right position, but we need to move them to the right list
        #             self.move_card_to_new_pile(card, pile_index)

        #         # Success, don't reset position of cards
        #         self.reset_position = False
        #     elif TOP_PILE_1 <= pile_index <= TOP_PILE_4 and len(self.held_cards) == 1:
        #         # Move position of card to pile
        #         self.held_cards[0].position = pile.position
        #         # Move card to card list
        #         for card in self.held_cards:
        #             self.move_card_to_new_pile(card, pile_index)

        #         self.reset_position = False


        # if self.reset_position:
        #     # Where-ever we were dropped, it wasn't valid. Reset the each card's position
        #     # to its original spot.
        #     for pile_index, card in enumerate(self.held_cards):
        #         card.position = self.held_cards_original_position[pile_index]

        # # We are no longer holding cards
        # self.held_cards = []
        
    def pull_to_top(self, card: arcade.Sprite):
        self.card_list.remove(card)
        self.card_list.append(card)



def main():
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
