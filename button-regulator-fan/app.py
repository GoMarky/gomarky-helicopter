import RPi.GPIO as GPIO


def get_pin_number(port_number):
    return port_number


def check_gpio_is_enabled(port_number):
    channel_is_on = GPIO.input(port_number)

    return channel_is_on


input_a = get_pin_number(15)
input_b = get_pin_number(18)


def start_app():
    print(1)


try:
    start_app()
except Exception as e:
    print(e)
    GPIO.cleanup()

finally:
    GPIO.cleanup
