# Day 12

## Namespaces: Local vs. Global Scope

### Scope

- Important in programming. The concept is very similar to global variable and local variables. When you pass the variables through in and out of the functions. The main difference is the ***Namespace***.

### Local Scope

- Exists within the function

- Example:

            def drink_potion():
              potion_strength = 2
              print(potion_strength)

            drink_potion()

### Global Scope

- Outside of the function

- Example:
              player_health = 10

              def drink_potion():
                potion_strength = 2
                print(potion_strength)

              drink_potion()
              print(player_health)

### How to modify a Global Variable

              enemies = 1

              def increase_enemies():
                # global enemies
                # enemies += 1
                print(f"enemies inside function: {enemies}")
                return enemies + 1
              enemies = increase_enemies()
              print(f"enemies outside function: {enemies}")

### Global Constants
