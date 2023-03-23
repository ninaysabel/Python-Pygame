# Nina Ysabel Alinsonorin // Computing ID: nca9ku
"""
Game Description: This game is similar to crossy road. The goal is for the pig to cross the as many streets as possible without hitting a car.
The player will have 3 lives and once out of lives the game is over. Each time the player crosses a street their score will go up.
Basic:
    User Input: Using arrows to control the movement of the pig
    Game Over: If the player runs out of lives the game will end. They will have the option to restart the game.
    Graphics/Images: The pig and cars
Additional:
    Restart from Game Over: Player can restart the game by pressing the "s" key
    Enemies: Cars
    Health Bar: Players will start with 3 lives and lose a life if hit by a car
    Score: Score goes up everytime the player crosses a road. The score is displayed at the end of the game.
"""
import uvage
camera = uvage.Camera(800,800)
game_on = False
game_over = False
pig = uvage.from_image(100, 750,"https://creazilla-store.fra1.digitaloceanspaces.com/cliparts/11261/pig-animal-clipart-md.png")
pig.scale_by(.05)
cars_left = [uvage.from_image(100,700, "https://creazilla-store.fra1.digitaloceanspaces.com/cliparts/29102/car-red-clipart-md.png"),
        uvage.from_image(300,700, "https://creazilla-store.fra1.digitaloceanspaces.com/cliparts/29102/car-red-clipart-md.png"),
        uvage.from_image(600,700, "https://creazilla-store.fra1.digitaloceanspaces.com/cliparts/29102/car-red-clipart-md.png"),
        uvage.from_image(200,500, "https://creazilla-store.fra1.digitaloceanspaces.com/cliparts/29102/car-red-clipart-md.png"),
        uvage.from_image(700,500, "https://creazilla-store.fra1.digitaloceanspaces.com/cliparts/29102/car-red-clipart-md.png"),
        uvage.from_image(150,300, "https://creazilla-store.fra1.digitaloceanspaces.com/cliparts/29102/car-red-clipart-md.png"),
        uvage.from_image(473,300, "https://creazilla-store.fra1.digitaloceanspaces.com/cliparts/29102/car-red-clipart-md.png"),
        uvage.from_image(679,300, "https://creazilla-store.fra1.digitaloceanspaces.com/cliparts/29102/car-red-clipart-md.png"),
        uvage.from_image(386,100, "https://creazilla-store.fra1.digitaloceanspaces.com/cliparts/29102/car-red-clipart-md.png"),
        uvage.from_image(724,100, "https://creazilla-store.fra1.digitaloceanspaces.com/cliparts/29102/car-red-clipart-md.png")]
for car in cars_left:
    car.scale_by(.08)
cars_right = [uvage.from_image(100,600, "https://creazilla-store.fra1.digitaloceanspaces.com/cliparts/29102/car-red-clipart-md.png"),
        uvage.from_image(300,600, "https://creazilla-store.fra1.digitaloceanspaces.com/cliparts/29102/car-red-clipart-md.png"),
        uvage.from_image(600,600, "https://creazilla-store.fra1.digitaloceanspaces.com/cliparts/29102/car-red-clipart-md.png"),
        uvage.from_image(200,400, "https://creazilla-store.fra1.digitaloceanspaces.com/cliparts/29102/car-red-clipart-md.png"),
        uvage.from_image(700,400, "https://creazilla-store.fra1.digitaloceanspaces.com/cliparts/29102/car-red-clipart-md.png"),
        uvage.from_image(150,200, "https://creazilla-store.fra1.digitaloceanspaces.com/cliparts/29102/car-red-clipart-md.png"),
        uvage.from_image(473,200, "https://creazilla-store.fra1.digitaloceanspaces.com/cliparts/29102/car-red-clipart-md.png"),
        uvage.from_image(679,200, "https://creazilla-store.fra1.digitaloceanspaces.com/cliparts/29102/car-red-clipart-md.png"),
]
for car in cars_right:
    car.scale_by(.08)
    car.flip()
score = 0
ticks = 0
lives = 3
grass = [
    uvage.from_color(400, 800, "black", 800, 50),
    uvage.from_color(400, 700, "black", 800, 50),
    uvage.from_color(400, 600, "black", 800, 50),
    uvage.from_color(400, 500, "black", 800, 50),
    uvage.from_color(400, 400, "black", 800, 50),
    uvage.from_color(400, 300, "black", 800, 50),
    uvage.from_color(400, 200, "black", 800, 50),
    uvage.from_color(400, 100, "black", 800, 50)]
ceiling = uvage.from_color(400, 10, "black", 800, 20)
walls = [
    uvage.from_color(0, 400, "white", 20, 800),
    uvage.from_color(800, 400, "white", 20, 800)]




def tick():
    camera.clear("light green")
    #Global Variables
    global game_on
    global game_over
    global score, ticks
    global grass
    global pig
    global ceiling
    global walls
    global cars
    global lives

    # game_over
    if lives == 0:
        game_over = True
        game_on = False

    if game_over:
        camera.draw(uvage.from_text(400, 400, "Game over! Press s to restart!", 60, "red", bold=False))
        camera.draw(uvage.from_text(400, 500, "Your final score is " + str(score), 50, "white", bold=False))
        if uvage.is_pressing("s"):
            lives = 3
            score = 0
            game_over = False
            game_on = False

    # Turning game on
    if (game_on == False) and (game_over == False):
        camera.draw(uvage.from_text(400, 400, "Press space to start!", 100, "Red", bold=False))
        camera.draw(uvage.from_text(400, 500, "The white number is your score. The red number is your lives remaining.", 30, "White", bold=False))
        camera.draw(uvage.from_text(400, 550, "Use the up, right, and left arrows to move the pig forward!", 30, "White", bold=False))
    if uvage.is_pressing("space"):
        game_on = True

    #game on
    if game_on:
        if pig.y == 100:
            score += 1
        if pig.y == 200:
            score += 1
        if pig.y == 300:
            score += 1
        if pig.y == 400:
            score += 1
        if pig.y == 500:
            score += 1
        if pig.y == 600:
            score += 1
        if pig.y == 700:
            score += 1

        #drawing lines
        for g in grass:
            camera.draw(g)

        #drawing ceiling
        camera.draw(ceiling)

        #drawing wall
        for wall in walls:
            camera.draw(wall)
            if pig.touches(wall):
                pig.move_to_stop_overlapping(wall)

        #drawing/moving cars
            for car in cars_left:
                camera.draw(car)
                car.speedx = -2
                car.move_speed()
                if car.touches(wall):
                    car.x = 730
                if pig.touches(car):
                    pig.y = 750
                    lives -= 1
            for car in cars_right:
                camera.draw(car)
                car.speedx = 2
                car.move_speed()
                if car.touches(wall):
                    car.x = 70
                if pig.touches(car):
                    pig.y = 750
                    lives -= 1

        #drawing/moving pig
        camera.draw(pig)
        if uvage.is_pressing("right arrow"):
            pig.move(4, 0)
        if uvage.is_pressing("left arrow"):
            pig.move(-4, 0)
        if uvage.is_pressing("up arrow"):
            pig.move(0, -5)

        if pig.touches(ceiling):
            pig.y = 750


        #score
        camera.draw(uvage.from_text(30, 50, str(score), 50, "white", bold=True))

        #lives
        camera.draw(uvage.from_text(750, 50, str(lives), 50, "red", bold=True))

    camera.display()


ticks_per_second = 30
uvage.timer_loop(ticks_per_second, tick)
