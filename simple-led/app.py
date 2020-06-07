import RPi.GPIO as GPIO


def get_pin_number(number):
    return number


gpio_port_number = get_pin_number(18)


def start_app():
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(gpio_port_number, GPIO.OUT)

    GPIO.output(gpio_port_number, True)


try:
    start_app()
except Exception as e:
    GPIO.cleanup()
