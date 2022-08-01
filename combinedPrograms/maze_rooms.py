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
SCREEN_TITLE = "Maze with Sprite Animation"

COIN_SCALE = 0.5
COIN_COUNT = 50
CHARACTER_SCALING = 1.5

# How fast to move, and how fast to run the animation
MOVEMENT_SPEED = 2
UPDATES_PER_FRAME = 5

# Constants used to track if the player is facing left or right
RIGHT_FACING = 0
LEFT_FACING = 1
UP_FACING = 2
DOWN_FACING = 3


class MazeWall():
    def __init__(self,left,right,top,bottom,color=arcade.color.BLUSH):
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom
        self.color = color
        
    def draw(self):
        arcade.draw_lrtb_rectangle_filled(self.left,self.right,self.top,self.bottom,self.color)
        

class PlayerCharacter(arcade.Sprite):
    def __init__(self):

        # Set up parent class
        super().__init__()

        # Default to face-right
        self.character_face_direction = DOWN_FACING

        # Used for flipping between image sequences
        self.cur_texture = 0

        self.scale = CHARACTER_SCALING
        
        main_path = "Nurse"

        # Load textures for idle standing
        self.idle_texture = f"{main_path}/forward0.png"
        
        # Load textures for walking
        self.walk_textures = []
        for i in range(4):
            texture = f"{main_path}/right{i}.png"
            self.walk_textures.append(texture)
            
        for i in range(4):
            texture = f"{main_path}/left{i}.png"
            self.walk_textures.append(texture)
        
        for i in range(4):
            texture = f"{main_path}/back{i}.png"
            self.walk_textures.append(texture)
            
        for i in range(4):
            texture = f"{main_path}/forward{i}.png"
            self.walk_textures.append(texture)                
            
            

    def update_animation(self, delta_time: float = 1 / 60):

        # Figure out if we need to flip face left or right
        if self.change_x < 0:#and self.character_face_direction == RIGHT_FACING:
            self.character_face_direction = LEFT_FACING
        elif self.change_x > 0:#and self.character_face_direction == LEFT_FACING:
            self.character_face_direction = RIGHT_FACING
          
        elif self.change_y < 0:
            self.character_face_direction = DOWN_FACING
        elif self.change_y > 0:
            self.character_face_direction = UP_FACING           

        # Idle animation
        if self.change_x == 0 and self.change_y == 0:
            self.texture = arcade.load_texture(self.idle_texture)#[self.character_face_direction]
            return

        # Walking animation
        self.cur_texture += 1
        if self.cur_texture > 3 * UPDATES_PER_FRAME:
            self.cur_texture = 0
        frame = self.cur_texture // UPDATES_PER_FRAME
        direction = self.character_face_direction
        self.texture = arcade.load_texture(self.walk_textures[4*direction + frame])


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """ Set up the game and initialize the variables. """
        super().__init__(width, height, title)

        # Sprite lists
        self.player_list = None
        self.coin_list = None

        # Set up the player
        self.score = 0
        self.player = None

    def setup(self):
        self.player_list = arcade.SpriteList()
        '''
        self.coin_list = arcade.SpriteList()
        '''
        
        # Set up the player
        '''
        self.score = 0
        '''
        self.player = PlayerCharacter()

        self.player.center_x = 235
        self.player.center_y = 580
        self.player.scale = CHARACTER_SCALING

        self.player_list.append(self.player)
        '''
        for i in range(COIN_COUNT):
            coin = arcade.Sprite(":resources:images/items/gold_1.png",
                                 scale=0.5)
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            self.coin_list.append(coin)
        '''
        
        
        self.walls = []
        
        self.walls.append(MazeWall(20,35,570,35))
        self.walls.append(MazeWall(570,585,570,35))
        self.walls.append(MazeWall(20,585,45,30))
        
        self.walls.append(MazeWall(20,208,570,555))
        self.walls.append(MazeWall(450,580,570,555))
        
        self.walls.append(MazeWall(262,310,570,500))
        self.walls.append(MazeWall(430,473,570,450))
        self.walls.append(MazeWall(90,340,500,455))
        self.walls.append(MazeWall(35,255,400,355))
        self.walls.append(MazeWall(220,255,360,200))
        self.walls.append(MazeWall(87,120,250,107))
        self.walls.append(MazeWall(306,340,500,107))
        self.walls.append(MazeWall(90,520,145,107))
        self.walls.append(MazeWall(315,515,298,258))
        self.walls.append(MazeWall(395,430,500,355))
        self.walls.append(MazeWall(485,518,260,200))
        self.walls.append(MazeWall(482,580,400,355))
        
        
        # Set the background color
        #arcade.set_background_color(arcade.color.AMAZON)
        self.background = arcade.load_texture("images\simple_maze_background.png")
        
    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        self.clear()
        
        arcade.start_render()
        arcade.draw_texture_rectangle(300,300,600,600,self.background)        

        # Draw all the sprites.
        '''
        self.coin_list.draw()
        '''
        self.player_list.draw()
        for item in self.player_list:
            item.draw_hit_box()
        '''
        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)
        '''
        for wall in self.walls:
            wall.draw()
        
        

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
            
    
    def detect_collision_with_rect(self,player,rect):
        collision = False
        for point in player.get_hit_box():
            print(point[0]+player.center_x, point[1]+player.center_y)
            print(rect.left,rect.right,rect.top,rect.bottom)            
            if point[0]+player.center_x <= rect.left and point[0]+player.center_x >= rect.right: #and point[1] >= rect.bottom and point[1] <= rect.top:
                print("collision")
                collision = True
                
        return collision
                
                
        

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Move the player
        self.player_list.update()

        # Update the players animation
        self.player_list.update_animation()
        
        '''
        # Generate a list of all sprites that collided with the player.
        hit_list = arcade.check_for_collision_with_list(self.player, self.coin_list)
        '''
        '''
        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1
            '''
        '''
        hit_list = arcade.check_for_collision_with_list(self.player,self.walls)
        if len(hit_list) != 0:
            self.player.change_x = 0
            self.player.change_y = 0
            print("hit wall")
        '''
        
        for wall in self.walls:
            if self.detect_collision_with_rect(self.player,wall):
                self.player.change_x = 0
                self.player.change_y = 0
        
        

def main():
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()