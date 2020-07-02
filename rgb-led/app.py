import RPi.GPIO as GPIO


def get_pin_number(port_number):
    return port_number


pin_red = get_pin_number(18)
pin_green = get_pin_number(23)
pin_blue = get_pin_number(24)

try:
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(pin_red, GPIO.OUT)
    GPIO.setup(pin_green, GPIO.OUT)
    GPIO.setup(pin_blue, GPIO.OUT)

    pwmRed = GPIO.PWM(pin_red, 500)
    pwmRed.start(100)

    pwmGreen = GPIO.PWM(pin_green, 500)
    pwmGreen.start(100)

    pwmBlue = GPIO.PWM(pin_blue, 500)
    pwmBlue.start(100)
except Exception as e:
    print(e)
    GPIO.cleanup()

finally:
    GPIO.cleanup()
