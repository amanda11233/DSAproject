
import arcade 

class Star(arcade.Sprite):
    def __init__(self, scale=1): 
        self.image_file_name = f":resources:images/items/star.png" 
        super().__init__(None, scale, hit_box_algorithm = "None") 
        self.show = False
  
    def dont_show(self):
        """ Don't show the star"""
        self.texture = arcade.load_texture(None)
        self.show = False

    def do_show(self):
        """ show the card """
        self.texture =  arcade.load_texture(self.image_file_name)
        self.show = False

    @property
    def is_not_show(self):  
        return not self.show


