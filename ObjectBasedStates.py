import pygame
pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("State Machine Demo")

# Colors
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Player variables (shared across states)
px, py = 50, 50
pw, ph = 20, 20
speed = 5

# Collision function
def is_colliding(x1, y1, w1, h1, x2, y2, w2, h2):
    return (
        x1 < x2 + w2 and x1 + w1 > x2 and
        y1 < y2 + h2 and y1 + h1 > y2
    )

#variable to keep track of states
current_state = None


# === Main Map State ===
class MainState:
    def __init__(self):
        self.bg_color = (200, 200, 255)
        self.door_x = 550
        self.door_y = 180
        self.door_w = 30
        self.door_h = 30

    def update(self):
        global px, py, current_state
        
        #input section------------------------
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:  px -= speed
        if keys[pygame.K_RIGHT]: px += speed
        if keys[pygame.K_UP]:    py -= speed
        if keys[pygame.K_DOWN]:  py += speed

        #physics/update section-------------------------
        
        #check collision with door to house
        if is_colliding(px, py, pw, ph, self.door_x, self.door_y, self.door_w, self.door_h) == True:
            px = house.door_x + house.door_w + 5 # Appear just outside the house door
            py = house.door_y
            current_state = house #change state to house

    def draw(self):
        screen.fill(self.bg_color)
        pygame.draw.rect(screen, BLACK, (self.door_x, self.door_y, self.door_w, self.door_h))

# === House Map State ===
class HouseState:
    def __init__(self):
        self.bg_color = (200, 255, 200)
        self.door_x = 10
        self.door_y = 180
        self.door_w = 30
        self.door_h = 30

    def update(self):
        global px, py, current_state
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:  px -= speed
        if keys[pygame.K_RIGHT]: px += speed
        if keys[pygame.K_UP]:    py -= speed
        if keys[pygame.K_DOWN]:  py += speed

        if is_colliding(px, py, pw, ph,
                        self.door_x, self.door_y,
                        self.door_w, self.door_h):
            # Appear just outside the main map door
            px = main.door_x - pw - 5
            py = main.door_y
            current_state = main

    def draw(self):
        screen.fill(self.bg_color)
        pygame.draw.rect(screen, BLACK, (self.door_x, self.door_y, self.door_w, self.door_h))

# === Create states ===
main = MainState()
house = HouseState()
current_state = main

#game loop variables
clock = pygame.time.Clock()
running = True


while running: #GAME LOOP#########################################
    
    #input section---------------------------
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #update section---------------------------
    current_state.update()

    #render section---------------------------
    screen.fill((0, 0, 0))  # just in case
    current_state.draw()
    pygame.draw.rect(screen, RED, (px, py, pw, ph))  # draw player

    pygame.display.flip()
    

pygame.quit()

