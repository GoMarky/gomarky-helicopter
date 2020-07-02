import RPi.GPIO as GPIO
import time


def check_gpio_is_enabled(port_number):
    channel_is_on = GPIO.input(port_number)

    return channel_is_on


led_pin = 25


def start_app():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led_pin, GPIO.OUT)

    if check_gpio_is_enabled(led_pin):
        print('Gpio pin was enabled')
        GPIO.output(led_pin, led_pin)

    while True:
        GPIO.output(led_pin, True)
        time.sleep(1)

        GPIO.output(led_pin, False)
        time.sleep(1)


try:
    start_app()
except Exception as e:
    print(e)
    GPIO.cleanup()

finally:
    GPIO.cleanup()
