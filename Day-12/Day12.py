################### Scope ####################
enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope 

def drink_potion():
  potion_strength = 2
  print(potion_strength)

drink_potion()

# Global Scope
player_health = 10

def game():
  def drink_potion():
    potion_strength = 2
    print(potion_strength)

  drink_potion()
print(player_health)
  
# If there is no Block Scope

game_level = 3
def create_enemy():
  enemies = ["Skeleton", "Zombie", "Alien"]
  if game_level < 5:
    new_enemy = enemies[0]

  print(new_enemy)

# Modifying Global varaible

enemies = 1

def increase_enemies():
  # global enemies
  # enemies += 1
  print(f"enemies inside function: {enemies}")
  return enemies + 1
enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

# Global Constants

PI = 3.14159
URL = "https://www.keelen.com"

def calc():
  URL
