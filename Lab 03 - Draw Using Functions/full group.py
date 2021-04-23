import arcade

def draw_tree_1():
   arcade.draw_rectangle_filled(500, 120, 20, 60, arcade.csscolor.SIENNA)
   arcade.draw_triangle_filled(500, 200, 470, 120, 530, 120, arcade.csscolor.DARK_GREEN)

def draw_tree_2():
   arcade.draw_rectangle_filled(100, 120, 20, 60, arcade.csscolor.SIENNA)
   arcade.draw_triangle_filled(100, 200, 70, 120, 130, 120, arcade.csscolor.DARK_GREEN)

def draw_car_2():
   arcade.draw_rectangle_filled(140, 24, 40, 17, (156, 191, 247))
   arcade.draw_rectangle_filled(140, 14, 70, 15, (51, 204, 97))
   arcade.draw_rectangle_filled(140, 14, 70, 15, (51, 204, 97))
   arcade.draw_circle_filled(120, 9, 8, arcade.csscolor.DARK_GREY)
   arcade.draw_circle_filled(160, 9, 8, arcade.csscolor.DARK_GREY)

def draw_road():
   arcade.draw_rectangle_filled(300, 40, 600, 80, (55, 59, 64))
   arcade.draw_rectangle_filled(300, 90, 600, 20, (116, 121, 130))
   arcade.draw_rectangle_filled(300, 40, 600, 80, (55, 59, 64))
   arcade.draw_rectangle_filled(300, 90, 600, 20, (116, 121, 130))
   arcade.draw_rectangle_filled(300, 40, 40, 10, (214, 170, 11))
   arcade.draw_rectangle_filled(150, 40, 40, 10, (214, 170, 11))
   arcade.draw_rectangle_filled(450, 40, 40, 10, (214, 170, 11))
   arcade.draw_rectangle_filled(0, 40, 40, 10, (214, 170, 11))
   arcade.draw_rectangle_filled(600, 40, 40, 10, (214, 170, 11))

def draw_car_1():
   arcade.draw_rectangle_filled(340, 60, 70, 15, (189, 31, 31))
   arcade.draw_rectangle_filled(340, 70, 40, 17, (156, 191, 247))
   arcade.draw_rectangle_filled(340, 60, 70, 15, (189, 31, 31))
   arcade.draw_circle_filled(320, 55, 8, arcade.csscolor.DARK_GREY)
   arcade.draw_circle_filled(360, 55, 8, arcade.csscolor.DARK_GREY)


def draw_building():
   # building
   arcade.draw_lrtb_rectangle_filled(200, 400, 500, 100, arcade.csscolor.GREY)

   #door
   arcade.draw_lrtb_rectangle_filled(287, 313, 140, 100, ((135, 62, 35)))
   arcade.draw_circle_filled(307, 115, 2, arcade.csscolor.BLACK)

   # windows
   arcade.draw_rectangle_filled(225, 460, 35, 60, arcade.csscolor.LIGHT_BLUE)
   arcade.draw_rectangle_filled(225, 380, 35, 60, arcade.csscolor.LIGHT_BLUE)
   arcade.draw_rectangle_filled(225, 300, 35, 60, arcade.csscolor.LIGHT_BLUE)
   arcade.draw_rectangle_filled(225, 220, 35, 60, arcade.csscolor.LIGHT_BLUE)
   arcade.draw_rectangle_filled(275, 460, 35, 60, arcade.csscolor.LIGHT_BLUE)
   arcade.draw_rectangle_filled(275, 380, 35, 60, arcade.csscolor.LIGHT_BLUE)
   arcade.draw_rectangle_filled(275, 300, 35, 60, arcade.csscolor.LIGHT_BLUE)
   arcade.draw_rectangle_filled(275, 220, 35, 60, arcade.csscolor.LIGHT_BLUE)
   arcade.draw_rectangle_filled(325, 460, 35, 60, arcade.csscolor.LIGHT_BLUE)
   arcade.draw_rectangle_filled(325, 380, 35, 60, arcade.csscolor.LIGHT_BLUE)
   arcade.draw_rectangle_filled(325, 300, 35, 60, arcade.csscolor.LIGHT_BLUE)
   arcade.draw_rectangle_filled(325, 220, 35, 60, arcade.csscolor.LIGHT_BLUE)
   arcade.draw_rectangle_filled(375, 460, 35, 60, arcade.csscolor.LIGHT_BLUE)
   arcade.draw_rectangle_filled(375, 380, 35, 60, arcade.csscolor.LIGHT_BLUE)
   arcade.draw_rectangle_filled(375, 300, 35, 60, arcade.csscolor.LIGHT_BLUE)
   arcade.draw_rectangle_filled(375, 220, 35, 60, arcade.csscolor.LIGHT_BLUE)

def draw_sun_sunset():
   '''background colors and sun'''
   # sunset

   arcade.draw_lrtb_rectangle_filled(0, 599, 250, 0, ((255, 214, 51)))
   arcade.draw_lrtb_rectangle_filled(0, 599, 400, 250, arcade.csscolor.YELLOW)
   arcade.draw_lrtb_rectangle_filled(0, 599, 500, 400, ((255, 255, 230)))

   # sun

   arcade.draw_circle_filled(300, 275, 150, ((255, 255, 102)))

def draw_cloud_1():
   '''big cloud'''
   arcade.draw_ellipse_filled(60, 525, 50, 30, arcade.csscolor.LIGHT_GREY)
   arcade.draw_ellipse_filled(90, 540, 60, 40, arcade.csscolor.LIGHT_GREY)
   arcade.draw_ellipse_filled(130, 555, 80, 20, arcade.csscolor.LIGHT_GREY)
   arcade.draw_ellipse_filled(135, 545, 43, 30, arcade.csscolor.LIGHT_GREY)
   arcade.draw_ellipse_filled(125, 525, 45, 25, arcade.csscolor.LIGHT_GREY)


def draw_cloud_2():
   '''smaller cloud'''
   arcade.draw_ellipse_filled(500, 330, 100, 50, arcade.csscolor.LIGHT_GREY)
   arcade.draw_ellipse_filled(575, 340, 90, 40, arcade.csscolor.LIGHT_GREY)
   arcade.draw_ellipse_filled(545, 320, 80, 30, arcade.csscolor.LIGHT_GREY)


def draw_cloud_3():
   '''other small cloud'''
   arcade.draw_ellipse_filled(102, 400, 60, 50, arcade.csscolor.LIGHT_GREY)
   arcade.draw_ellipse_filled(140, 390, 80, 43, arcade.csscolor.LIGHT_GREY)
   arcade.draw_ellipse_filled(170, 410, 50, 20, arcade.csscolor.LIGHT_GREY)

arcade.open_window(600, 600, "building")

arcade.set_background_color(arcade.csscolor.WHITE)

arcade.start_render ()

draw_sun_sunset()

draw_cloud_1()

draw_cloud_2()

draw_cloud_3()

draw_building()

draw_road()

draw_car_1()

draw_car_2()

draw_tree_1()

draw_tree_2()

arcade.finish_render()

arcade.run()




