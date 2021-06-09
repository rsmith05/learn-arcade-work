import arcade


def field():
    # Picture shown after the fight because arcade is annoying and I don't get it
    arcade.draw_lrtb_rectangle_filled(0, 599, 400, 0, arcade.csscolor.LIGHT_GREEN)
    arcade.draw_ellipse_filled(400, 300, 250, 100, arcade.csscolor.BLANCHED_ALMOND)
    arcade.draw_ellipse_outline(400, 300, 250, 100, arcade.csscolor.BROWN, 5)
    arcade.draw_ellipse_filled(150, 100, 300, 125, arcade.csscolor.BLANCHED_ALMOND)
    arcade.draw_ellipse_outline(150, 100, 300, 125, arcade.csscolor.BROWN, 5)


def gastly_circles(x, y):
    arcade.draw_circle_filled(x, y, 10, arcade.csscolor.PURPLE)


def gastly():
    arcade.draw_circle_filled(150, 200, 100, arcade.csscolor.PURPLE)
    arcade.draw_circle_filled(150, 200, 90, arcade.csscolor.BLACK)
    gastly_circles(150, 85)
    gastly_circles(175, 300)
    gastly_circles(100, 310)
    gastly_circles(200, 100)
    gastly_circles(50, 150)
    gastly_circles(150, 85)
    gastly_circles(250, 180)
    gastly_circles(45, 175)
    gastly_circles(50, 250)
    gastly_circles(250, 240)


def pikachu():
    # tail
    arcade.draw_rectangle_filled(430, 360, 100, 33, arcade.csscolor.GOLD, -45)
    arcade.draw_rectangle_outline(430, 360, 100, 33, arcade.csscolor.BLACK, 1, 45)
    # ears
    arcade.draw_ellipse_filled(375, 430, 60, 20, arcade.csscolor.GOLD, 50)
    arcade.draw_ellipse_outline(375, 430, 60, 20, arcade.csscolor.BLACK, 1, 50)
    arcade.draw_ellipse_filled(360, 445, 30, 20, arcade.csscolor.BLACK, 50)
    arcade.draw_ellipse_filled(425, 430, 60, 20, arcade.csscolor.GOLD, -50)
    arcade.draw_ellipse_outline(425, 430, 60, 20, arcade.csscolor.BLACK, 1, -50)
    arcade.draw_ellipse_filled(440, 445, 30, 20, arcade.csscolor.BLACK, -50)
    # feet
    arcade.draw_ellipse_filled(370, 305, 40, 20, arcade.csscolor.GOLD)
    arcade.draw_ellipse_filled(430, 305, 40, 20, arcade.csscolor.GOLD)
    arcade.draw_ellipse_outline(370, 305, 40, 20, arcade.csscolor.BLACK)
    arcade.draw_ellipse_outline(430, 305, 40, 20, arcade.csscolor.BLACK)
    # arms
    arcade.draw_ellipse_filled(360, 350, 20, 60, arcade.csscolor.GOLD, 25)
    arcade.draw_ellipse_filled(440, 350, 20, 60, arcade.csscolor.GOLD, -25)
    arcade.draw_ellipse_outline(360, 350, 20, 60, arcade.csscolor.BLACK, 1, 25)
    arcade.draw_ellipse_outline(440, 350, 20, 60, arcade.csscolor.BLACK, 1, -25)
    # torso and head
    arcade.draw_ellipse_filled(400, 350, 85, 100, arcade.csscolor.GOLD)
    arcade.draw_ellipse_outline(400, 350, 85, 100, arcade.csscolor.BLACK)
    arcade.draw_circle_filled(400, 400, 35, arcade.csscolor.GOLD)
    arcade.draw_circle_outline(400, 400, 35, arcade.csscolor.BLACK)
    # eyes
    arcade.draw_circle_filled(385, 410, 8, arcade.csscolor.BLACK)
    arcade.draw_circle_filled(388, 413, 3, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(415, 410, 8, arcade.csscolor.BLACK)
    arcade.draw_circle_filled(412, 413, 3, arcade.csscolor.WHITE)
    # cheeks
    arcade.draw_circle_filled(422, 390, 10, arcade.csscolor.RED)
    arcade.draw_circle_filled(378, 390, 10, arcade.csscolor.RED)


def battle():
    # Entire fight with pikachu vs gastly
    pikachu_hp = 49
    gastly_hp = 45
    confuse_ray = 0
    pikachu_status = 0
    pikachu_cannot_run = False
    pikachu_run_away = False
    gastly_run_away = False

    # Initiates the battle and tells the trainer the hp of both pokemon
    print(" A wild Pikachu appeared!\n")
    print("Pikachu has " + str(pikachu_hp) + " hp!")
    print("Gastly has " + str(gastly_hp) + " hp!\n")

    # Loop for when gastly and pikachu either drop to 0 hp or run away.
    while gastly_hp > 0 and pikachu_hp > 0 and not gastly_run_away and not pikachu_run_away:

        print("A. Lick\nB. Confuse Ray\nC. Giga Drain\nD. Mean Look\nE. Run away")
        move = input("What move will gastly use? ")
        print("")

        # PIKACHU ATTACKS
        if pikachu_status > 0:
            print("Pikachu hit himself and lost 2 hp!")
            pikachu_hp -= 2
            print("")

        elif pikachu_status == 0 and pikachu_hp >= 35:
            print("Pikachu Used Quick Attack! Pikachu deals 6 damage!")
            gastly_hp -= 6
            print("")

        elif pikachu_status == 0 and pikachu_hp >= 25:
            print("Pikachu used Thunder Shock! Pikachu deals 8 damage!")
            gastly_hp -= 8
            print("")

        elif pikachu_status == 0 and pikachu_hp < 25 and pikachu_cannot_run == True:
            print("Pikachu used Spark! Pikachu deals 10 damage!")
            gastly_hp -= 10
            print("")

        elif pikachu_status == 0 and pikachu_hp < 25 and pikachu_cannot_run == False:
            print("Pikachu ran away!")
            pikachu_run_away = True
            print("")

        else:
            print("THIS IS NOT SUPPOSED TO TRIGGER!!!")
            print("")

        # States whether or not pikachu is still confused after his turn
        if pikachu_status > 0:
            pikachu_status -= 1
            if pikachu_status == 0:
                print("pikachu snapped out of confusion!")
                print("")

        if gastly_hp > 0 and pikachu_run_away == False:
            # GASTLY ATTACKS
            if move.upper() == "A":
                print("Gastly used Lick! Gastly deals 7 damage!")
                pikachu_hp -= 7
                print("")

            # Confuse Ray if its off cooldown
            elif move.upper() == "B" and confuse_ray == 0:
                print("Gastly used Confuse Ray! Pikachu is confused!")
                pikachu_status = 2
                confuse_ray = 4
                print("")

            # Confuse Ray if its on cooldown
            elif move.upper() == "B" and confuse_ray > 0:
                print("This move has no effect!")
                print("")

            elif move.upper() == "C":
                print("Gastly used Giga Drain! Gastly deals 4 damage and heals 2 hp!")
                gastly_hp += 2
                pikachu_hp -= 4
                print("")

            elif move.upper() == "D":
                print("Gastly used Mean Look! Pikachu can't run away!")
                pikachu_cannot_run = True
                print("")

            elif move.upper() == "E":
                print("You ran away successfully!")
                gastly_run_away = True

            else:
                print("You were looking at flowers...")
                print("")

            # States whether or not gastly can use Confuse Ray again
            if confuse_ray > 0:
                confuse_ray -= 1
                if confuse_ray == 0:
                    print("Gastly can use Confuse Ray again!")
                    print("")

        print("Pikachu has " + str(pikachu_hp) + " hp!")
        print("Gastly has " + str(gastly_hp) + " hp!\n")

    if gastly_hp <= 0:
        print("As gastly fainted, you rushed towards the nearest pokecenter.")
    elif pikachu_hp <= 0:
        print("Pikachu was defeated! Your party gains +54 xp.")
    elif pikachu_run_away == True:
        print("Better luck next time.")
    elif gastly_run_away == True:
        print("You got away safely")


def main():

    battle()

    arcade.open_window(600, 600, "Gastly vs Pikachu")

    arcade.set_background_color(arcade.color.DARK_GREEN)

    arcade.start_render()

    field()

    gastly()

    pikachu()

    arcade.finish_render()

    arcade.run()


main()
