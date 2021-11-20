
import arcade
from constants import FACE_DOWN_IMAGE

class Card(arcade.Sprite):
    def __init__(self, suit, value, scale=1):
        self.suit = suit
        self.value = value
        self.image_file_name = f":resources:images/cards/card{self.suit}{self.value}.png"
        super().__init__(FACE_DOWN_IMAGE, scale, hit_box_algorithm = "None") 
        self.is_face_up = False 

    def face_down(self):
        """ Turn card face-down """
        self.texture = arcade.load_texture(FACE_DOWN_IMAGE)
        self.is_face_up = False

    def face_up(self):
        """ Turn card face-up """
        self.texture = arcade.load_texture(self.image_file_name)
        self.is_face_up = True

    @property
    def is_face_down(self):
        """ Is this card face down? """
        return not self.is_face_up


