import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class Game(arcade.Window):
    def __init__(self):
        
        super().__init__(SCREEN_WIDTH,SCREEN_HEIGHT,title="Haunted House Maze")
        self.background = arcade.load_texture("images\simple_maze_background.png")
        
        self.player_list = arcade.SpriteList()
        self.player_sprite = Player(":resources:images/animated_characters/female_person/femalePerson_idle.png",0.5)
        self.player_sprite.center_x = 235
        self.player_sprite.center_y = 580
        self.player_list.append(self.player_sprite)
        
        
    #def setup():
        self.camera_sprites = arcade.Camera(self.width, self.height)
        self.camera_gui = arcade.Camera(self.width, self.height)
        
        '''
        self.player_sprite = arcade.Sprite("images\player_1.png",1.0)
        self.player_sprite.cener_x = 100
        self.player_sprite.center_y = 100
        self.scene.add_sprite("Player",self.player_sprite)
        '''
        
    def on_draw(self):
        self.clear()
        
        arcade.start_render()
        arcade.draw_texture_rectangle(300,300,600,600,self.background)
        self.camera_sprites.use()   
        self.camera_gui.use()        
        self.player_list.draw()
        
    def on_update(self, delta_time):
        self.player_list.update()
        
    def on_key_press(self, key, modifiers):

        # If the player presses a key, update the speed
        if key == arcade.key.UP:
            self.player_sprite.change_y = 2
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -2
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -2
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = 2

    def on_key_release(self, key, modifiers):

        # If a player releases a key, zero out the speed.
        # This doesn't work well if multiple keys are pressed.
        # Use 'better move by keyboard' example if you need to
        # handle this.
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0 
        
        

class Player(arcade.Sprite):
    
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        
        
        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1        
        
    

window = Game()
#window.setup()
arcade.run()