import arcade

def main():

    # prints the red squares
    arcade.draw_rectangle_filled(10, 10, 10, 10, 255, 0, 0)

arcade.open_window(600, 600, "checkerboard")
arcade.set_background_color((255, 255, 255))

arcade.start_render()
arcade.run()

main()

arcade.finish_render()

arcade.run()