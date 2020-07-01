import RPi.GPIO as GPIO
import time


def get_pin_number(port_number):
    return port_number


def check_gpio_is_enabled(port_number):
    channel_is_on = GPIO.input(port_number)

    return channel_is_on


switch_pin = get_pin_number(24)
led_pin = get_pin_number(23)

fan_input_a = get_pin_number(15)
fan_input_b = get_pin_number(18)


def start_app():
    GPIO.setmode(GPIO.BCM)

    pressed_times = 0

    GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(led_pin, GPIO.OUT)

    GPIO.setup(fan_input_a, GPIO.OUT)
    GPIO.setup(fan_input_b, GPIO.OUT)

    power_b = GPIO.PWM(fan_input_b, 500)
    power_b.start(50)

    led_state = False
    old_input_state = True

    while True:
        new_input_state = check_gpio_is_enabled(switch_pin)

        if new_input_state == False and old_input_state == True:
            time.sleep(0.2)

            led_state = not led_state

            if led_state == True:
                power_b.ChangeDutyCycle(100)
            else:
                power_b.ChangeDutyCycle(0)

            pressed_times += 1
            print('Button pressed ' + str(pressed_times) + 'times')

        old_input_state = new_input_state
        GPIO.output(led_pin, led_state)


try:
    start_app()
except Exception as e:
    print(e)
    GPIO.cleanup()

finally:
    GPIO.cleanup()
