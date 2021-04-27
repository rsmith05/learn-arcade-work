import arcade


def white_tile(xw, yw):
    # prints white tile 50 by 50
    arcade.draw_rectangle_filled(50 * xw, 50 * yw, 50, 50, (255, 255, 255))


def black_tile(xb, yb):
    # prints black tile 50 by 50
    arcade.draw_rectangle_filled(50 * xb, 50 * yb, 50, 50, (0, 0, 0))


def tile_rows_white_black(y):
    # top row if white if the first on the left, first number being the x cord times 50,
    # second number being the y cord times 50
    white_tile(1, 11 - y)
    black_tile(2, 11 - y)
    white_tile(3, 11 - y)
    black_tile(4, 11 - y)
    white_tile(5, 11 - y)
    black_tile(6, 11 - y)
    white_tile(7, 11 - y)
    black_tile(8, 11 - y)
    white_tile(9, 11 - y)
    black_tile(10, 11 - y)
    white_tile(11, 11 - y)


def tile_rows_black_white(y):
    # top row if black is the first on the left
    black_tile(1, 11 - y)
    white_tile(2, 11 - y)
    black_tile(3, 11 - y)
    white_tile(4, 11 - y)
    black_tile(5, 11 - y)
    white_tile(6, 11 - y)
    black_tile(7, 11 - y)
    white_tile(8, 11 - y)
    black_tile(9, 11 - y)
    white_tile(10, 11 - y)
    black_tile(11, 11 - y)


def main():
    arcade.open_window(600, 600, "checkerboard")
    arcade.set_background_color(arcade.color.BARBIE_PINK)
    arcade.start_render()

    # runs white first 5 times every other line, number in the parameters makes it go down 50 starting at 1
    tile_rows_white_black(1)
    tile_rows_white_black(3)
    tile_rows_white_black(5)
    tile_rows_white_black(7)
    tile_rows_white_black(9)

    # runs the same thing up top but every even line
    tile_rows_black_white(0)
    tile_rows_black_white(2)
    tile_rows_black_white(4)
    tile_rows_black_white(6)
    tile_rows_black_white(8)

    arcade.finish_render()
    arcade.run()


# runs the entire program
main()
