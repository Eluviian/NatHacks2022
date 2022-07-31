import arcade
from global_vars import *

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
        
        if room == 8:
            if self.center_x < 100 or self.center_x > 285:
                self.change_x = 0
                
        if self.center_y > HALLWAY_TOP:
            
            if room == 1:
                if self.center_x > 479 and self.center_x < 505:
                    room = 0
                    self.center_x = 278
                    self.center_y = HALLWAY_BOTTOM + 1
                    
            elif room == 2:
                if self.center_x > 393 and self.center_x < 419:
                    room = 0
                    self.center_x = 407
                    self.center_y = HALLWAY_BOTTOM + 1
                    
            elif room == 3:
                if self.center_x > 178 and self.center_x < 204:
                    room = 0
                    self.center_x = 536
                    self.center_y = HALLWAY_BOTTOM + 1
                    
            elif room == 8:
                if self.center_x > 176 and self.center_x < 202 :
                    room = 7
                    self.center_x = 277
                    self.center_y = HALLWAY_BOTTOM + 1
            else:
                self.change_y = 0
            
        if self.center_y < HALLWAY_BOTTOM:
            
            if room == 0:
                if (self.center_x > 258 and self.center_x < 298):
                    room = 1
                    self.center_x = 493
                    self.center_y = HALLWAY_TOP - 1
                    
                if (self.center_x > 387 and self.center_x < 427):
                    room = 2
                    self.center_x = 405
                    self.center_y = HALLWAY_TOP - 1
                    
                if (self.center_x > 516 and self.center_x < 556):
                    room = 3
                    self.center_x = 189 
                    self.center_y = HALLWAY_TOP - 1
                else:
                    self.change_y = 0
            if room == 7:
                if  self.center_x > 257 and self.center_x < 297:
                    room = 8
                    self.center_x = 189
                    self.center_y = HALLWAY_TOP - 1
                    
                else:
                    self.change_y = 0
                    
                
            
            
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