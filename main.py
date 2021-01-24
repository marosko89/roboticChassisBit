def on_button_pressed_a():
    wuKong.set_servo_angel(wuKong.ServoList.S1, 50)
    wuKong.set_servo_angel(wuKong.ServoList.S0, 70)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    wuKong.set_servo_angel(wuKong.ServoList.S0, 90)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    wuKong.set_servo_angel(wuKong.ServoList.S1, 30)
    wuKong.set_servo_angel(wuKong.ServoList.S0, 110)
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_icon(IconNames.HEART)
wuKong.set_light_mode(wuKong.LightMode.BREATH)
wuKong.set_servo_angel(wuKong.ServoList.S0, 90)
wuKong.set_servo_angel(wuKong.ServoList.S1, 90)