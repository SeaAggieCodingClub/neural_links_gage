from Character import *
from Position import *
import copy
import Sound

class Pacman(Character):
    lives = 3
    pause = False # Each dot Pac-Man eats causes him to stop moving for one frame or 1/60th of a second
    
    def __init__(self, speed):
        self.speed = self.base_speed = speed
        self.pos = Position(13.5, 23)
        self.dir = 'a'
    
    def kill(self):
        self.is_dead = True
        self.lives -= 1
        Sound.play_death_sound()
    
    def reset_position(self):
        self.pos = Position(13.5, 23)
    
    def update_pacman(self, grid):
        self.check_warp_tunnels()
        if self.pause:
            self.pause = False
        elif self.check_wall(self.dir, grid): # Check if pos is a wall   
            self.pos = self.pos.tile() # Center the position
        else:
            self.move(self.speed)
            
    # Changes the direction of pacman from the keyboard input, if move is invalid returns the next move 
    def control_pacman(pacman, next_move, grid):
        # Direction controls
        # next_move = next_move_list[0] # Store as tuple for pass by reference
        pos = pacman.pos.tile() # Centered position
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or next_move == 'w':
            if pacman.check_wall('w', grid):
                next_move = 'w' # Set a buffer for the next move
            else:
                pacman.dir = 'w'
                next_move = None
                pacman.pos.x = pos.x # Center x position
        if keys[pygame.K_a] or next_move == 'a':
            if pacman.check_wall('a', grid):
                next_move = 'a' # Set a buffer for the next move
            else:
                pacman.dir = 'a'
                next_move = None
                pacman.pos.y = pos.y # Center y position
        if keys[pygame.K_s] or next_move == 's':
            if pacman.check_wall('s', grid):
                next_move = 's' # Set a buffer for the next move
            else:
                pacman.dir = 's'
                next_move = None
                pacman.pos.x = pos.x # Center x position
        if keys[pygame.K_d] or next_move == 'd':
            if pacman.check_wall('d', grid):
                next_move = 'd' # Set a buffer for the next move
            else:
                pacman.dir = 'd'
                next_move = None
                pacman.pos.y = pos.y # Center y position
        
        return next_move