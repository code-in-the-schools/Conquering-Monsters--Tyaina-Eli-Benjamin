import pygame
import os
import random
 
img_path = os.path.join('Grey.png')
img_path = os.path.join('Pink.png')
img_path = os.path.join('Potion.png')

class Potion(object):
 def __init__(self):
   pygame.sprite.Sprite.__init__(self)

   Potion.image = pygame.image.load('Potion.png')

   #self.image = pygame.transform.scale(self.image, (50, 50))

   self.y = 20
   self.x = 50

 def draw(self, surface):
   surface.blit(self.image, (self.x, self.y)) 

class Monster(object):
  def __init__(self):
   pygame.sprite.Sprite.__init__(self)

   Monster.image = pygame.image.load('Grey.png')

   #self.image = pygame.transform.scale(self.image, (50, 50))

   self.y = 100
   self.x = 100
   
  def draw(self, surface):
    surface.blit(self.image, (self.x, self.y))
       
  def Attack():
    PlayerHealth = 100
    MonsterHealth = 100
    MonsterAttack = random.randint(5,10)
    if MonsterHealth == 80:
        print("Monster's turn")
    PlayerHealth = MonsterAttack - PlayerHealth
    print(PlayerHealth)

class Player(object):
  def __init__(self):
   pygame.sprite.Sprite.__init__(self)

   Player.image = pygame.image.load('Pink.png')

   #self.image = pygame.transform.scale(self.image, (50, 50))

   
   self.x = 50
   self.y = 50

  def draw(self, surface):
    surface.blit(self.image, (self.x, self.y))
 
  def Inventory(self,screen):
    self.x = 50
    self.y = 50
    Inventory = []
    if self.x and Potion.x == self.y and Potion.y:
     Potion.append(Inventory)
     print(Inventory)
  
  def HealthBar(self,screen):
    Attacks = ['Punch', 'Block']
    MonsterAttack = random.randrange(10)
    MonsterHealth = 100
    PlayerHealth = 100
    Fighting = True
    while Fighting:
      b = input('Attack? YES or NO. ')
      print(b)
      if b == 'YES':
        print(Attacks)
        c = input('Choose your attack: ')
        print(c)
      if c == 'Punch':
        MonsterHealth = MonsterHealth - 20
        print("Monster's Health:", MonsterHealth ,'\n' ,">> Monster's turn <<")
        PlayerHealth = MonsterAttack - PlayerHealth
        print("Player's Health:" , abs(PlayerHealth))
      if c == 'Block':
          print("Monster's turn")
          MonsterAttack = MonsterAttack // 2
          PlayerHealth = MonsterAttack - PlayerHealth
          print("Player's Health:" , abs(PlayerHealth))
    
      if MonsterHealth == 0:
        print('CONGRADULATIONS!!! >> You Have Defated The Monster << You Advaced to next level')
        Fighting = False  
    if PlayerHealth == 0:
        print('You Lose')
        Fighting = False


  #def movement(self):
    #key = pygame.key.get_pressed()

    #if key[pygame.K_DOWN]:
      #self.y += 1

    #if key[pygame.K_UP]:
      #self.y -= 1
  


          
pygame.init()
screen_width = 700
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))


running = True
Players = Player()
Monsters = Monster()
Potions = Potion()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False 
                  
                  
    screen.fill((255, 255, 255))
    Players.draw(screen)
    Players.HealthBar(screen)
    Players.Inventory(screen)
    Monsters.attack(screen)
    Monsters.draw(screen)
    Players.attack(screen)
    Potions.draw(screen)
    pygame.display.update()