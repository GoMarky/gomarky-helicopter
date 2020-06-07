import RPi.GPIO as GPIO
import time


def get_pin_number(number):
    return number


gpio_port_number = get_pin_number(18)


def check_gpio_is_enabled():
    channel_is_on = GPIO.input(gpio_port_number)

    return channel_is_on


def start_app():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(gpio_port_number, GPIO.OUT)

    if check_gpio_is_enabled():
        print('Gpio pin was enabled')
        GPIO.output(gpio_port_number, gpio_port_number)

    while True:
        GPIO.output(gpio_port_number, True)
        time.sleep(1)

        GPIO.output(gpio_port_number, False)
        time.sleep(1)


try:
    start_app()
except Exception as e:
    print(e)
    GPIO.cleanup()

finally:
    GPIO.cleanup
