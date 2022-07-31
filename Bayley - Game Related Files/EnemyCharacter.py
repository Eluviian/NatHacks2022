import arcade
from global_vars import *

class EnemyCharacter(arcade.Sprite):
    def __init__(self):

        # Set up parent class
        super().__init__()

        # Default to face-right
        self.character_face_direction = DOWN_FACING
        self.room = 99
        self.chasing_player = False

        # Used for flipping between image sequences
        self.cur_texture = 0

        self.scale = CHARACTER_SCALING
        
        main_path = "Nurse"

        # Load textures for idle standing
        self.idle_textures = []
        for direction in ["forward","left","right","back"]:
            self.idle_textures.append(f"{main_path}/{direction}0.png")
        
        #forward, left, right, back
        
        # Load textures for walking
        self.walk_textures = []
        for direction in ["forward","left","right","back"]:
            for i in range(4):
                texture = f"{main_path}/{direction}{i}.png"
                self.walk_textures.append(texture)

                   
            
            

    def update_animation1(self, delta_time: float = 1 / 60):
        # Figure out if we need to flip face left or right
        if self.change_x < 0: #and self.character_face_direction == RIGHT_FACING:
            self.character_face_direction = LEFT_FACING
        elif self.change_x > 0: #and self.character_face_direction == LEFT_FACING:
            self.character_face_direction = RIGHT_FACING
          
        elif self.change_y < 0:
            self.character_face_direction = DOWN_FACING
        elif self.change_y > 0:
            self.character_face_direction = UP_FACING           

                
        
            
        # Idle animation
        if self.change_x == 0 and self.change_y == 0:
            self.texture = arcade.load_texture(self.idle_textures[self.character_face_direction])
            

        # Walking animation
        self.cur_texture += 1
        if self.cur_texture > 3 * UPDATES_PER_FRAME:
            self.cur_texture = 0
        frame = self.cur_texture // UPDATES_PER_FRAME
        direction = self.character_face_direction
        self.texture = arcade.load_texture(self.walk_textures[4*direction + frame])
        
        
    def transfer_room(self, starting_room, goal_room):
        print(self.room, goal_room)
        self.room = goal_room
        if starting_room == 0:
            if goal_room == 1:
                self.center_x = 493
                self.center_y = HALLWAY_TOP - 1
            if goal_room == 2:
                self.center_x = 405
                self.center_y = HALLWAY_TOP - 1
            if goal_room == 3:
                self.center_x = 189
                self.center_y = HALLWAY_TOP - 1
        if starting_room == 1:
            if goal_room == 0:
                self.center_x = 278
                self.center_y = HALLWAY_BOTTOM + 1
            if goal_room == 2:
                self.center_x = 1
        if starting_room == 2:
            if goal_room == 0:
                self.center_x = 393
                self.center_y = HALLWAY_BOTTOM + 1
            if goal_room == 1:
                self.center_x = 1
            if goal_room == 3:
                self.center_x = 1
        if starting_room == 3:
            if goal_room == 0:
                self.center_x = 178
                self.center_y = HALLWAY_BOTTOM + 1
            if goal_room == 2:
                self.center_x = SCREEN_WIDTH - 1
            if goal_room == 7:
                self.center_x = 1
        if starting_room == 7:
            if goal_room == 3:
                self.center_x = SCREEN_WIDTH - 1
            if goal_room == 8:
                self.center_x = 189
                self.center_y = HALLWAY_TOP - 1
        if starting_room == 8:
            if goal_room == 7:
                self.center_x = 277
                self.center_y = HALLWAY_BOTTOM + 1
        
        