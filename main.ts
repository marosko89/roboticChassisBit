input.onButtonPressed(Button.A, function () {
    wuKong.setServoAngel(wuKong.ServoList.S1, 50)
    wuKong.setServoAngel(wuKong.ServoList.S0, 70)
})
input.onButtonPressed(Button.AB, function () {
    wuKong.setServoAngel(wuKong.ServoList.S0, 90)
})
input.onButtonPressed(Button.B, function () {
    wuKong.setServoAngel(wuKong.ServoList.S1, 30)
    wuKong.setServoAngel(wuKong.ServoList.S0, 110)
})
basic.showIcon(IconNames.Heart)
wuKong.setLightMode(wuKong.LightMode.BREATH)
wuKong.setServoAngel(wuKong.ServoList.S0, 90)
wuKong.setServoAngel(wuKong.ServoList.S1, 90)
