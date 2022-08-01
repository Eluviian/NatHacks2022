"""
Move with a Sprite Animation

Simple program to show basic sprite usage.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_move_animation
"""
import arcade
import random
import time
from PlayerCharacter import PlayerCharacter
from EnemyCharacter import EnemyCharacter
from global_vars import *




class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """ Set up the game and initialize the variables. """
        super().__init__(width, height, title)

        # Set up the player
        self.player = None
        self.enemy = None

    def setup(self):
        
        # Set up the player
        self.enemy_timer = 0
        self.enemy_spawned = False
        
        self.player = PlayerCharacter()
        self.player.center_x = 250
        self.player.center_y = 250
        self.player.scale = CHARACTER_SCALING
        
        self.enemy = EnemyCharacter()
        self.enemy.center_x = 300
        self.enemy.center_y = 200
        self.enemy.scale = ENEMY_SCALING
        
        self.total_chase_timer = 0
        self.continue_game = True
        
        self.broken_mirror = False
        
        

        self.background = arcade.load_texture("Maps\exit_room.png")
        self.room = 7
        
        self.music = None
        self.song = "audio\Closing-In_Looping.mp3"
        self.play_song()
        
        
    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        self.clear()
        
        arcade.start_render()
        arcade.draw_texture_rectangle(300,300,600,600,self.background)  
        
        
        
        if self.room == 8:
            if self.broken_mirror == False: 
                unbroken_mirror_sprite = arcade.Sprite("images/before_mirror.png", scale=1.2, center_x = 535, center_y= 305)
                unbroken_mirror_sprite.draw()
            else:
                broken_mirror_sprite = arcade.Sprite("images/after_mirror.png", scale = 1.2, center_x = 535, center_y = 305)
                broken_mirror_sprite.draw()
        
        #arcade.draw_lrtb_rectangle_filled(5,595,260,255,arcade.color.BLUSH)
        #arcade.draw_lrtb_rectangle_filled(5,595,150,145,arcade.color.BLUSH)
        if self.continue_game:
            # Draw all the sprites.
            self.player.draw()
            if self.enemy.room == self.room:
                self.enemy.draw()
            
            #arcade.draw_lrtb_rectangle_filled(178,204,272,260,arcade.color.BLUSH)
            #arcade.draw_lrtb_rectangle_filled(387,427,140,100,arcade.color.BLUSH)
            #arcade.draw_lrtb_rectangle_filled(176,202,272,260,arcade.color.BLUSH)
        
        
        

    def on_key_press(self, key, modifiers):
        """
        Called whenever a key is pressed.
        """
        if key == arcade.key.UP:
            self.player.change_y = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player.change_y = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player.change_x = PLAYER_MOVEMENT_SPEED

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
       
        #reading from the file
        with open('ratios.txt', 'r') as f:
            ratioString = (f.readline().split('\n'))
      
        if ratioString[0] != '':
            #print this one
            '''print("ratio string 0",ratioString[0])
            '''
            if float(ratioString[0]) > 0.1:
                pass
                #print("true")
                #self.room = 0

        
        #check of player is caught
        if arcade.check_for_collision(self.enemy,self.player) and self.room == self.enemy.room:
            #end_game(False)
            self.continue_game = False
            self.broken_mirror = False
            self.background = arcade.load_texture("images\game_over.png")
            self.song = "audio\Closing-In_Looping.mp3"
            self.play_song()            
            
            

        # Move the player
        self.player.update()
        self.enemy.update()
        
        self.prev_room = self.room

        # Update the players animation
        self.room = self.player.update_animation1(self.room)
        self.enemy.update_animation1()
        
        ##########broken mirror when unfocused
        if self.enemy_timer >= 300 and self.room == 8 and self.player.center_y < HALLWAY_TOP - 25 and self.broken_mirror == False and self.continue_game:
            self.broken_mirror = True
            #play audio/glass_shatter.mp3
            glass_shatter_sound = arcade.load_sound("audio/glass_shatter.mp3")
            arcade.play_sound(glass_shatter_sound)
            #print statement showing ratio
        
        ##########monster shows up when focused
        #deactivate monster spawning automatically
        #boolean to spawn moneter into next room player enters
        #print statement showing ratio
        #prevent this from happening again for a time limit
        '''
        if self.enemy_timer >= 200 and self.room != self.prev_room and self.enemy.chasing_player == False:
            self.enemy.room = self.room '''
            
        
        
        
        if self.enemy_timer == 200:
            
            if self.room == 0 or self.room == 1 or self.room == 2:
                self.enemy.room = 8
                #print("enemy is in room",self.enemy.room)
            if self.room == 3 or self.room == 7 or self.room == 8:
                self.enemy.room = 1
                #print("enemy is in room "+str(self.enemy.room))
          
          
        if self.enemy.room == self.room:
            if self.song != "audio\Horror-NeverLookBack.mp3":
                self.song = "audio\Horror-NeverLookBack.mp3"
                self.play_song()
            self.chase_timer = self.enemy_timer
            self.enemy.chasing_player = True
            self.chase_distance = abs(self.enemy.center_x - self.player.center_x)
            
        if self.enemy.chasing_player == True:
            self.total_chase_timer += 1
            
            #print(self.enemy_timer,self.chase_timer)
            if self.enemy.room == self.room:
                self.enemy_pursue()
            
            #player can lose the enemy after a while
            elif self.total_chase_timer  >= 500 and self.chase_distance > 230:
                self.enemy.chasing_player = False
                print("chase over")
                self.total_chase_timer = 0
                self.enemy_timer = 0
            
            elif self.enemy_timer == self.chase_timer + 50 and self.chase_distance < 100:
                #print("a")
                chase_distance = abs(self.enemy.center_x - self.player.center_x)
                self.enemy.transfer_room(self.enemy.room,self.room)
                
            elif self.enemy_timer == self.chase_timer + 200:
                #print("a")
                chase_distance = abs(self.enemy.center_x - self.player.center_x)
                self.enemy.transfer_room(self.enemy.room,self.room)            
            
        
        
        if self.room == 0:
            map_string = "Maps/exit_room.png"

        else:
            map_string = f"Maps/room{self.room}.png"
           
        
        self.enemy_timer += 1
        if self.continue_game:
            self.background = arcade.load_texture(map_string)
            
        self.prev_room = self.room
        

    def enemy_pursue(self):
        if self.player.center_x < self.enemy.center_x:
            self.enemy.change_x = -ENEMY_MOVEMENT_SPEED
        else:
            self.enemy.change_x = ENEMY_MOVEMENT_SPEED
            
        if self.player.center_y < self.enemy.center_y:
            self.enemy.change_y = -ENEMY_MOVEMENT_SPEED
        
        else:
            self.enemy.change_y = ENEMY_MOVEMENT_SPEED       
            
        
        
    def play_song(self):
        if self.music:
            self.music.stop(self.current_player)
        
        self.music = arcade.Sound(self.song, streaming = True)
        self.current_player = self.music.play(MUSIC_VOLUME)
        time.sleep(0.03)
   
       

def main():
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()
    window.music.stop(window.current_player)


if __name__ == "__main__":
    main()