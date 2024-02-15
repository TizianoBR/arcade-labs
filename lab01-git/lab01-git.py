import math
import random
import arcade

def draw_minecart(x, y, size):
    arcade.draw_circle_filled(size * 617.5 + x, size * 145 + y, size * 12, arcade.color.YELLOW)
    arcade.draw_lrtb_rectangle_filled(size * 450 + x, size * 600 + x, size * 180 + y, size * 100 + y,arcade.color.BROWN_NOSE)
    arcade.draw_triangle_filled(size * 450 + x, size * 181 + y, size * 450 + x, size * 100 + y, size * 420 + x,size * 181 + y, arcade.color.BROWN_NOSE)
    arcade.draw_triangle_filled(size * 600 + x, size * 181 + y, size * 600 + x, size * 100 + y, size * 630 + x,size * 181 + y, arcade.color.BROWN_NOSE)
    arcade.draw_lrtb_rectangle_filled(size * 410 + x, size * 640 + x, size * 190 + y, size * 170 + y, (110, 110, 110))
    arcade.draw_circle_filled(size * 475 + x, size * 100 + y, size * 30, (110, 110, 110))
    arcade.draw_circle_outline(size * 475 + x, size * 100 + y, size * 22.5, arcade.color.BROWN_NOSE, size * 15)
    arcade.draw_circle_filled(size * 575 + x, size * 100 + y, size * 30, (110, 110, 110))
    arcade.draw_circle_outline(size * 575 + x, size * 100 + y, size * 22.5, arcade.color.BROWN_NOSE, size * 15)

    arcade.draw_lrtb_rectangle_filled(size * 225 + x, size * 325 + x, size * 550 + y, size * 125 + y, (75, 75, 75))

    arcade.draw_triangle_filled(size * 435 + x, size * 0 + y, size * 295 + x, size * 0 + y, size * 365 + x,
                                size * 275 + y, (70, 70, 70))
    arcade.draw_triangle_filled(size * 335 + x, size * 0 + y, size * 215 + x, size * 0 + y, size * 275 + x,
                                size * 210 + y, (70, 70, 70))

def draw_slime(x,y,w,h,verde,oscuro,espada):

    arcade.draw_ellipse_filled(w*270+x, h*270+y, 20*w, 70*h, arcade.color.BLACK, 40)
    arcade.draw_rectangle_filled(w*300+x, h*245+y, 20*w, 70*h, arcade.color.BLACK, -50)

    arcade.draw_rectangle_filled(w*230+x, h*300+y, 30*w, 100*h, espada, 310)
    arcade.draw_triangle_filled(w*205+x, h*341+y, w*186+x, h*316+y, w*165+x, h*355+y, espada)

    arcade.draw_rectangle_filled(w*230+x, h*300+y, 1*w, 100*h, arcade.color.SPANISH_GRAY, -50)

    arcade.draw_rectangle_filled(w*400+x, h*240+y, 190*w, 80*h, verde)
    arcade.draw_rectangle_filled(w*440+x, h*240+y, 105*w, 80*h, oscuro)

    arcade.draw_ellipse_filled(w*312+x, h*262+y, 40*w, 129*h, verde)
    arcade.draw_ellipse_filled(w*488+x, h*262+y, 40*w, 129*h, oscuro)
    arcade.draw_rectangle_filled(w*400+x, h*200+y, 190*w, 10*h, oscuro)

    arcade.draw_ellipse_filled(w*400+x, h*300+y, 200*w, 189*h, verde)  # circulo principal
    arcade.draw_ellipse_filled(w*340+x, h*300+y, 20*w, 70*h, arcade.color.BLACK)  # ojos
    arcade.draw_ellipse_filled(w*420+x, h*300+y, 20*w, 70*h, arcade.color.BLACK)



def draw_image(x, y, size):
    arcade.draw_lrtb_rectangle_filled(size*0+x, size*800+x, size*150+y, size*0+y, arcade.color.DAVY_GREY)
    arcade.draw_triangle_filled(size*70+x, size*130+y, size*150+x, size*130+y, size*110+x, size*270+y, (80, 80, 80))
    arcade.draw_triangle_filled(size*775+x, size*115+y, size*695+x, size*115+y, size*735+x, size*350+y, (80, 80, 80))

    arcade.draw_lrtb_rectangle_filled(size*0+x, size*800+x, size*600+y, size*525+y, (100, 100, 100))
    arcade.draw_triangle_filled(size*500+x, size*550+y, size*540+x, size*550+y, size*520+x, size*425+y, (95, 95, 95))
    arcade.draw_triangle_filled(size*450+x, size*570+y, size*510+x, size*570+y, size*480+x, size*390+y, (95, 95, 95))
    arcade.draw_triangle_filled(size*15+x, size*565+y, size*55+x, size*565+y, size*35+x, size*415+y, (95, 95, 95))

    #color = arcade.color.GOLD
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    arcade.draw_point(size*100+x, size*570+y, color, size*15)
    arcade.draw_point(size*130+x, size*575+y, color, size*15)
    arcade.draw_point(size*122.5+x, size*550+y, color, size*20)
    arcade.draw_point(size*92.5+x, size*550+y, color, size*10)
    arcade.draw_point(size*150+x, size*565+y, color, size*10)

    #color = arcade.color.DIAMOND
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    arcade.draw_point(size*650+x, size*75+y, color, size*20)
    arcade.draw_point(size*685+x, size*60+y, color, size*25)
    arcade.draw_point(size*640+x, size*40+y, color, size*30)
    arcade.draw_point(size*677.5+x, size*30+y, color, size*20)

    #color = arcade.color.EMERALD
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    arcade.draw_point(size*400+x, size*560+y, color, size*20)
    arcade.draw_point(size*430+x, size*550+y, color, size*15)
    arcade.draw_point(size*425+x, size*575+y, color, size*15)

    #color = arcade.color.LAPIS_LAZULI
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    arcade.draw_point(size*745+x, size*555+y, color, size*15)
    arcade.draw_point(size*705+x, size*575+y, color, size*15)
    arcade.draw_point(size*715+x, size*550+y, color, size*20)
    arcade.draw_point(size*740+x, size*580+y, color, size*25)
    arcade.draw_point(size*740+x, size*535+y, color, size*10)

    #color = arcade.color.DARK_PASTEL_PURPLE
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    arcade.draw_point(size*80+x, size*50+y, color, size*20)
    arcade.draw_point(size*107.5+x, size*30+y, color, size*20)
    arcade.draw_point(size*110+x, size*65+y, color, size*30)
    arcade.draw_point(size*75+x, size*20+y, color, size*25)
    arcade.draw_point(size*135+x, size*15+y, color, size*15)
    arcade.draw_point(size*140+x, size*50+y, color, size*20)

    for i in range(0, 770, 50):
        arcade.draw_line(size*(i+20)+x, size*70+y, size*(i+20)+x, size*110+y, arcade.color.WOOD_BROWN, size*5)
    arcade.draw_line(size*0+x, size*70+y, size*800+x, size*70+y, (100, 100, 100), size*7.5)
    arcade.draw_line(size*0+x, size*110+y, size*800+x, size*110+y, (100, 100, 100), size*7.5)

arcade.open_window(1500, 700, "My drawing")
arcade.set_background_color(arcade.color.BATTLESHIP_GREY)
arcade.start_render()

random.seed()

#for i in range(3):
#    r = random.random()*0.5 + 0.5
#    draw_image(random.randint(0, 1500-round(800*r)), random.randint(0, 700-round(600*r)), r)
draw_image(-100, 0, 1.166)
draw_image(800*1.166-100, 0, 1.166)

r = random.randint(50, 255)
g = random.randint(50, 255)
b = random.randint(50, 255)
color = (r, g, b)
colorShadow = (r - 80, g - 80, b - 60)
draw_slime(310, 110, 0.5, 0.5, color, colorShadow, (75, 75, 75))

r = random.randint(50, 255)
g = random.randint(50, 255)
b = random.randint(50, 255)
color = (r, g, b)
colorShadow = (r - 80, g - 80, b - 60)
draw_slime(310 + 800*1.166, 110, 0.5, 0.5, color, colorShadow, (75, 75, 75))

draw_minecart(-100, 0, 1.166)
draw_minecart(800*1.166-100, 0, 1.166)

r = random.randint(50, 255)
g = random.randint(50, 255)
b = random.randint(50, 255)
color = (r, g, b)
colorShadow = (r - 80, g - 80, b - 60)
draw_slime(700, 20, 0.5, 0.5, color, colorShadow, (75, 75, 75))

arcade.finish_render()
arcade.run()
