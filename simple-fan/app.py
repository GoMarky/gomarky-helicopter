import RPi.GPIO as GPIO


def get_pin_number(port_number):
    return port_number


def check_gpio_is_enabled(port_number):
    channel_is_on = GPIO.input(port_number)

    return channel_is_on


input_a = get_pin_number(15)
input_b = get_pin_number(18)


def start_app():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(input_a, GPIO.OUT)
    GPIO.setup(input_b, GPIO.OUT)

    power_b = GPIO.PWM(input_b, 500)

    power_b.start(15)

    while True:
        duty_s = input('Enter speed from 0 to 100')
        duty = int(duty_s)
        power_b.ChangeDutyCycle(duty)


try:
    start_app()
except Exception as e:
    print(e)
    GPIO.cleanup()

finally:
    GPIO.cleanup
