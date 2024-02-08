import arcade

arcade.open_window(800, 600, "My drawing")
arcade.set_background_color(arcade.color.BATTLESHIP_GREY)
arcade.start_render()

arcade.draw_lrtb_rectangle_filled(0, 800, 150, 0, arcade.color.DAVY_GREY)
arcade.draw_triangle_filled(70, 130,150, 130, 110, 270, (80, 80, 80))
arcade.draw_triangle_filled(775, 115,695, 115, 735, 350, (80, 80, 80))

arcade.draw_lrtb_rectangle_filled(0, 800, 600, 525, (100, 100, 100))
arcade.draw_triangle_filled(500, 550, 540, 550, 520, 425, (95, 95, 95))
arcade.draw_triangle_filled(450, 570, 510, 570, 480, 390, (95, 95, 95))
arcade.draw_triangle_filled(15, 565, 55, 565, 35, 415, (95, 95, 95))

arcade.draw_point(100, 570, arcade.color.GOLD, 15)
arcade.draw_point(130, 575, arcade.color.GOLD, 15)
arcade.draw_point(122.5, 550, arcade.color.GOLD, 20)
arcade.draw_point(92.5, 550, arcade.color.GOLD, 10)
arcade.draw_point(150, 565, arcade.color.GOLD, 10)

arcade.draw_point(650, 75, arcade.color.DIAMOND, 20)
arcade.draw_point(685, 60, arcade.color.DIAMOND, 25)
arcade.draw_point(640, 40, arcade.color.DIAMOND, 30)
arcade.draw_point(677.5, 30, arcade.color.DIAMOND, 20)

arcade.draw_point(400, 560, arcade.color.EMERALD, 20)
arcade.draw_point(430, 550, arcade.color.EMERALD, 15)
arcade.draw_point(425, 575, arcade.color.EMERALD, 15)

arcade.draw_point(745, 555, arcade.color.LAPIS_LAZULI, 15)
arcade.draw_point(705, 575, arcade.color.LAPIS_LAZULI, 15)
arcade.draw_point(715, 550, arcade.color.LAPIS_LAZULI, 20)
arcade.draw_point(740, 580, arcade.color.LAPIS_LAZULI, 25)
arcade.draw_point(740, 535, arcade.color.LAPIS_LAZULI, 10)

arcade.draw_point(80, 50, arcade.color.DARK_PASTEL_PURPLE, 20)
arcade.draw_point(107.5, 30, arcade.color.DARK_PASTEL_PURPLE, 20)
arcade.draw_point(110, 65, arcade.color.DARK_PASTEL_PURPLE, 30)
arcade.draw_point(75, 20, arcade.color.DARK_PASTEL_PURPLE, 25)
arcade.draw_point(135, 15, arcade.color.DARK_PASTEL_PURPLE, 15)
arcade.draw_point(140, 50, arcade.color.DARK_PASTEL_PURPLE, 20)

for i in range(0, 770, 50):
    arcade.draw_line(i+20, 70, i+20, 110, arcade.color.WOOD_BROWN, 5)
arcade.draw_line(0, 70, 800, 70, (100, 100, 100), 7.5)
arcade.draw_line(0, 110, 800, 110, (100, 100, 100), 7.5)

arcade.draw_circle_filled(617.5, 145, 12, arcade.color.YELLOW)
arcade.draw_lrtb_rectangle_filled(450, 600, 180, 100, arcade.color.BROWN_NOSE)
arcade.draw_triangle_filled(450, 181, 450, 100, 420, 181, arcade.color.BROWN_NOSE)
arcade.draw_triangle_filled(600, 181, 600, 100, 630, 181, arcade.color.BROWN_NOSE)
arcade.draw_lrtb_rectangle_filled(410, 640, 190, 170, (110, 110, 110))
arcade.draw_circle_filled(475, 100, 30, (110, 110, 110))
arcade.draw_circle_outline(475, 100, 22.5, arcade.color.BROWN_NOSE, 15)
arcade.draw_circle_filled(575, 100, 30, (110, 110, 110))
arcade.draw_circle_outline(575, 100, 22.5, arcade.color.BROWN_NOSE, 15)

arcade.draw_lrtb_rectangle_filled(225, 325, 550, 125, (75, 75, 75))

arcade.draw_triangle_filled(435, 0,295, 0, 365, 275, (70, 70, 70))
arcade.draw_triangle_filled(335, 0,215, 0, 275, 210, (70, 70, 70))

arcade.finish_render()
arcade.run()