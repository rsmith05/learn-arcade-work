"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.
"""

# Import the "arcade" library
import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the dimensions (width and height)
arcade.open_window(600, 600, "Drawing Example")

# Set the background color

arcade.set_background_color(arcade.csscolor.SKY_BLUE)


# Get ready to draw

arcade.start_render()

# Draw a rectangle
arcade.draw_lrtb_rectangle_filled(0, 500, 250, 100, arcade.csscolor.GREEN)

# Tree trunk
arcade.draw_rectangle_filled(200, 320, 20, 60, arcade.csscolor.SIENNA)

# circle drawing
# Tree top
arcade.draw_circle_filled(200, 350, 30, arcade.csscolor.DARK_GREEN)

# Draw an ellipse and rect with
# a center of (300, 300)
# width of 350
# height of 200
arcade.draw_rectangle_outline(300, 20, 350, 100, arcade.csscolor.BLACK, 3)
arcade.draw_ellipse_outline(300, 450, 350, 200, arcade.csscolor.RED, 3)

# Another tree, with a trunk and ellipse for top
arcade.draw_rectangle_filled(300, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(300, 370, 60, 80, arcade.csscolor.DARK_GREEN)

# Another tree, with a trunk and triangle for top
# Triangle is made of these three points:
# (400, 400), (370, 320), (430, 320)
arcade.draw_rectangle_filled(400, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(400, 400, 370, 320, 430, 320, arcade.csscolor.DARK_GREEN)

# Another tree, with a trunk and arc for top
# Arc is centered at (500, 340) with a width of 60 and height of 100.
# The starting angle is 0, and ending angle is 180.
arcade.draw_rectangle_filled(500, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_arc_filled(500, 340, 60, 100, arcade.csscolor.DARK_GREEN, 0, 180)

# Draw a tree using a polygon with a list of points
arcade.draw_rectangle_filled(550, 220, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_polygon_filled(((550, 300),
                            (530, 260),
                            (520, 220),
                            (580, 220),
                            (570, 260)
                            ),
                           arcade.csscolor.DARK_GREEN)

# Draw a sun
arcade.draw_circle_filled(500, 550, 40, arcade.color.YELLOW)

# Rays to the left, right, up, and down
arcade.draw_line(500, 550, 400, 550, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 600, 550, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 500, 450, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 500, 650, arcade.color.YELLOW, 3)

# Diagonal rays
arcade.draw_line(500, 550, 550, 600, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 550, 500, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 450, 600, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 450, 500, arcade.color.YELLOW, 3)

# (The drawing code will go here.)

# Draw text at (0, 150) with a font size of 48 pts.
arcade.draw_text("I call this piece, Nature",
                 0, 150,
                 arcade.color.PINK, 48)

# Finish drawing

arcade.finish_render()


# Keep the window up until someone closes it.
arcade.run()
