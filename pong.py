from pygame import *


window = display.set_mode((800, 600))

background = transform.scale(image.load("background.jpg"), (800, 600))


class GameSprite(sprite.Sprite):

    def __init__(self, player_image, player_x, player_y, player_speed, x, y):
 
        sprite.Sprite.__init__(self)
  
        self.image = transform.scale(image.load(player_image),(x, y))
   
        self.speed = player_speed
   
        self.rect = self.image.get_rect()
    
        self.rect.x = player_x
    
        self.rect.y = player_y
    
    
    def reset(self):
        
        window.blit(self.image, (self.rect.x, self.rect.y))
    

    def update_1(self):
       
        keys = key.get_pressed()

        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
    

    def update_2(self):
        keys = key.get_pressed()

        if keys[K_s] and self.rect.y > 5:
            self.rect.y -= self.speed


class Player(GameSprite):

    def update(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_LEFT]:
            self.rect.y -= self.speed

        if keys_pressed[K_RIGHT]:
            self.rect.y += self.speed

#sprites

a = Player("ball.png", 250, 250, 5, 45, 45)

b = Player("r1.png", 40, 250, 10, 30, 170)

c = Player("r2.png", 400, 250, 10, 30, 170)

#sprites




FPS = 75
running = True
clock = time.Clock()


while running:

    for r in event.get():

        if r.type == QUIT:
            running = False
 
    window.blit(background, (0, 0))
    a.reset()
    b.reset()
    c.reset()
    clock.tick(FPS)
 
    display.update()
