import arcade

def field():
    # Picture shown after the fight because arcade is annoying and I don't get it
    arcade.draw_lrtb_rectangle_filled(0, 599, 400, 0, (arcade.csscolor.LIGHT_GREEN))

def main():
    arcade.open_window(600, 600, "Gastly vs Pikachu")

    arcade.set_background_color(arcade.color.DARK_GREEN)

    arcade.start_render()

    arcade.draw_lrtb_rectangle_filled(0, 599, 400, 0, (arcade.csscolor.LIGHT_GREEN))

    arcade.finish_render()

    arcade.run()

main()