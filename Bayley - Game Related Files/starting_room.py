"""
Move with a Sprite Animation

Simple program to show basic sprite usage.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_move_animation
"""
import arcade
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Rooms with Sprite Animation"

COIN_SCALE = 0.5
COIN_COUNT = 50
CHARACTER_SCALING = 1.5

# How fast to move, and how fast to run the animation
MOVEMENT_SPEED = 2
UPDATES_PER_FRAME = 10

HALLWAY_TOP = 270
HALLWAY_BOTTOM = 190

# Constants used to track if the player is facing left or right
DOWN_FACING = 0
LEFT_FACING = 1
RIGHT_FACING = 2
UP_FACING = 3

class PlayerCharacter(arcade.Sprite):
    def __init__(self):

        # Set up parent class
        super().__init__()

        # Default to face-right
        self.character_face_direction = DOWN_FACING

        # Used for flipping between image sequences
        self.cur_texture = 0

        self.scale = CHARACTER_SCALING
        
        main_path = "Player"

        # Load textures for idle standing
        self.idle_textures = []
        for i in ["01","04","07","10"]:
            self.idle_textures.append(f"{main_path}/tile0{i}.png")
        
        # Load textures for walking
        self.walk_textures = []
        for i in range(10):
            texture = f"{main_path}/tile00{i}.png"
            self.walk_textures.append(texture)
            
        for i in [10,11]:
            texture = f"{main_path}/tile0{i}.png"
            self.walk_textures.append(texture)
            
        #forward, left, right, back             
            
            

    def update_animation1(self, room, delta_time: float = 1 / 60):
        # Figure out if we need to flip face left or right
        if self.change_x < 0:#and self.character_face_direction == RIGHT_FACING:
            self.character_face_direction = LEFT_FACING
        elif self.change_x > 0:#and self.character_face_direction == LEFT_FACING:
            self.character_face_direction = RIGHT_FACING
          
        elif self.change_y < 0:
            self.character_face_direction = DOWN_FACING
        elif self.change_y > 0:
            self.character_face_direction = UP_FACING           
          
        if self.center_y > HALLWAY_TOP:
            self.center_y = HALLWAY_BOTTOM + 1
            if room == 1:
                if self.center_x > 479 and self.center_x < 505:
                    room = 0
                    self.center_x = 278
                    
            elif room == 2:
                if self.center_x > 393 and self.center_x < 419:
                    room = 0
                    self.center_x = 407
                    
            elif room == 3:
                if self.center_x > 178 and self.center_x < 204:
                    room = 0
                    self.center_x = 536
                    
            elif room == 8:
                if self.center_x > 176 and self.center_x < 202 :
                    room = 7
                    self.center_x = 277
            else:
                self.change_y = 0
            
        if self.center_y < HALLWAY_BOTTOM:
            self.center_y = HALLWAY_TOP - 1
            if room == 0:
                if (self.center_x > 258 and self.center_x < 298):
                    room = 1
                    self.center_x = 493
                    
                if (self.center_x > 387 and self.center_x < 427):
                    room = 2
                    self.center_x = 405
                    
                if (self.center_x > 516 and self.center_x < 556):
                    room = 3
                    self.center_x = 189  
                else:
                    self.change_y = 0
            if room == 7:
                if  self.center_x > 257 and self.center_x < 297:
                    room = 8
                    self.center_x = 189
                    
                
            
            
        if self.center_x > SCREEN_WIDTH:
            self.center_x = 1
            if room == 1:
                room = 2
            elif room == 2:
                room = 3
            elif room == 3:
                room = 7
            elif room == 7:
                room = 1
            else:
                self.change_x = 0
        
        elif self.center_x < 0:
            self.center_x = SCREEN_WIDTH-1
            if room == 1:
                room = 7
            elif room == 2:
                room = 1
            elif room == 3:
                room = 2
            elif room == 7:
                room = 3
            else:
                self.change_x = 0
            
        # Idle animation
        if self.change_x == 0 and self.change_y == 0:
            self.texture = arcade.load_texture(self.idle_textures[self.character_face_direction])
            return room

        # Walking animation
        self.cur_texture += 1
        if self.cur_texture > 2 * UPDATES_PER_FRAME:
            self.cur_texture = 0
        frame = self.cur_texture // UPDATES_PER_FRAME
        direction = self.character_face_direction
        self.texture = arcade.load_texture(self.walk_textures[3*direction + frame])
        
        return room


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """ Set up the game and initialize the variables. """
        super().__init__(width, height, title)
        '''
        # Sprite lists
        self.player_list = None
        self.coin_list = None '''

        # Set up the player
        self.score = 0
        self.player = None

    def setup(self):
        #self.player_list = arcade.SpriteList()
        '''
        self.coin_list = arcade.SpriteList()
        '''
        
        # Set up the player
        '''
        self.score = 0
        '''
        self.player = PlayerCharacter()

        self.player.center_x = 250
        self.player.center_y = 250
        self.player.scale = CHARACTER_SCALING

        #self.player_list.append(self.player)
        '''
        for i in range(COIN_COUNT):
            coin = arcade.Sprite(":resources:images/items/gold_1.png",
                                 scale=0.5)
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            self.coin_list.append(coin)
        '''
        
        
        # Set the background color
        #arcade.set_background_color(arcade.color.AMAZON)
        self.background = arcade.load_texture("Maps\exit_room.png")
        self.room = 7
        
        
    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        self.clear()
        
        arcade.start_render()
        arcade.draw_texture_rectangle(300,300,600,600,self.background)  
        
        #arcade.draw_lrtb_rectangle_filled(5,595,260,255,arcade.color.BLUSH)
        #arcade.draw_lrtb_rectangle_filled(5,595,150,145,arcade.color.BLUSH)

        # Draw all the sprites.
        #self.player_list.draw()
        self.player.draw()
        
        #arcade.draw_lrtb_rectangle_filled(178,204,272,260,arcade.color.BLUSH)
        #arcade.draw_lrtb_rectangle_filled(387,427,140,100,arcade.color.BLUSH)
        #arcade.draw_lrtb_rectangle_filled(176,202,272,260,arcade.color.BLUSH)
        
        '''
        for item in self.player_list:
            item.draw_hit_box()'''
        
        

    def on_key_press(self, key, modifiers):
        """
        Called whenever a key is pressed.
        """
        if key == arcade.key.UP:
            self.player.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """
        Called when the user releases a key.
        """
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0
            
                
                
        

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Move the player
        self.player.update()

        # Update the players animation
        self.room = self.player.update_animation1(self.room)
        
        '''
        # Generate a list of all sprites that collided with the player.
        hit_list = arcade.check_for_collision_with_list(self.player, self.coin_list)
        '''

        
        if self.room == 0:
            map_string = "Maps/exit_room.png"

        else:
            map_string = f"Maps/room{self.room}.png"
           
           
        self.background = arcade.load_texture(map_string)


def main():
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()