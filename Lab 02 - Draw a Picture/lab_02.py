import arcade

arcade.open_window(600, 600, "Drawing Example")

# base sky color
arcade.set_background_color((0, 0, 156))

arcade.start_render()

# sky layers
arcade.draw_lrtb_rectangle_filled(0, 599, 400, 200, (224, 33, 212))
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 200, (255, 64, 64))

# sun
arcade.draw_circle_filled(299, 200, 110, (255, 207, 16))
arcade.draw_circle_filled(299, 200, 100, arcade.csscolor.YELLOW)

# starry sky
arcade.draw_circle_filled(340, 450, 2, arcade.csscolor.WHITE)
arcade.draw_circle_filled(310, 500, 1, arcade.csscolor.WHITE)
arcade.draw_circle_filled(550, 530, 2, arcade.csscolor.WHITE)
arcade.draw_circle_filled(234, 420, 3, arcade.csscolor.WHITE)
arcade.draw_circle_filled(356, 590, 1, arcade.csscolor.WHITE)
arcade.draw_circle_filled(567, 464, 2, arcade.csscolor.WHITE)
arcade.draw_circle_filled(346, 500, 3, arcade.csscolor.WHITE)
arcade.draw_circle_filled(20, 430, 1, arcade.csscolor.WHITE)

# saturn
arcade.draw_circle_filled(450, 550, 6, arcade.csscolor.LIGHT_BLUE)
arcade.draw_ellipse_outline(450, 550, 25, 10, arcade.csscolor.LIGHT_BLUE)

# big dipper
arcade.draw_circle_filled(50, 550, 3, arcade.csscolor.WHITE)
arcade.draw_circle_filled(100, 555, 3, arcade.csscolor.WHITE)
arcade.draw_circle_filled(125, 530, 3, arcade.csscolor.WHITE)
arcade.draw_circle_filled(160, 510, 3, arcade.csscolor.WHITE)
arcade.draw_circle_filled(155, 470, 3, arcade.csscolor.WHITE)
arcade.draw_circle_filled(200, 450, 3, arcade.csscolor.WHITE)
arcade.draw_circle_filled(230, 490, 3, arcade.csscolor.WHITE)
arcade.draw_polygon_outline(((50, 550),
                             (100, 555),
                             (125, 530),
                             (160, 510),
                             (155, 470),
                             (200, 450),
                             (230, 490),
                             (160, 510),
                             (125, 530),
                             (100, 555),
                             (50, 550)
                             ),
                            arcade.csscolor.WHITE)

# cloud right
arcade.draw_ellipse_filled(500, 230, 100, 50, arcade.csscolor.WHITE)
arcade.draw_ellipse_filled(575, 240, 90, 40, arcade.csscolor.WHITE)
arcade.draw_ellipse_filled(545, 220, 80, 30, arcade.csscolor.WHITE)

# cloud left
arcade.draw_ellipse_filled(2, 200, 60, 50, arcade.csscolor.WHITE)
arcade.draw_ellipse_filled(40, 190, 80, 43, arcade.csscolor.WHITE)
arcade.draw_ellipse_filled(70, 210, 50, 20, arcade.csscolor.WHITE)

# ground
arcade.draw_lrtb_rectangle_filled(0, 599, 200, 0, (72, 60, 50))
arcade.draw_lrtb_rectangle_filled(0, 599, 190, 0, (59, 49, 43))
arcade.draw_lrtb_rectangle_filled(0, 599, 180, 0, (51, 43, 40))
arcade.draw_lrtb_rectangle_filled(0, 599, 170, 0, (35, 30, 29))
arcade.draw_lrtb_rectangle_filled(0, 599, 160, 0, (24, 22, 22))
arcade.draw_lrtb_rectangle_filled(0, 599, 150, 0, (0, 0, 0))

# person sitting down
arcade.draw_circle_filled(299, 350, 40, (0, 0, 0))
arcade.draw_rectangle_filled(299, 300, 40, 50, (0, 0, 0))
arcade.draw_rectangle_filled(299, 250, 60, 120, (0, 0, 0))

# arms
arcade.draw_line(319, 310, 370, 190, (0, 0, 0), 22)
arcade.draw_line(279, 310, 230, 190, (0, 0, 0), 22)

# legs
arcade.draw_line(319, 195, 325, 210, (0, 0, 0), 22)
arcade.draw_line(279, 195, 275, 210, (0, 0, 0), 22)

# title of masterpiece
arcade.draw_text("Head Empty",
                 259, 10,
                 arcade.color.DARK_BLUE)

arcade.finish_render()

arcade.run()
