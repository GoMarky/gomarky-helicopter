import RPi.GPIO as GPIO


def get_pin_number(port_number):
    return port_number


def check_gpio_is_enabled(port_number):
    channel_is_on = GPIO.input(port_number)

    return channel_is_on
