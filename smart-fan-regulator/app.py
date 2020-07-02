import RPi.GPIO as GPIO
import time


def check_gpio_is_enabled(port_number):
    channel_is_on = GPIO.input(port_number)

    return channel_is_on


max_speed = 100
min_speed = 0


def start_app():
    GPIO.setmode(GPIO.BCM)

    # setup sound sensor

    gpio_trigger = 18
    gpio_echo = 24

    GPIO.setup(gpio_trigger, GPIO.OUT)
    GPIO.setup(gpio_echo, GPIO.IN)

    # setup fan

    fan_input_a = 27
    fan_input_b = 22

    GPIO.setup(fan_input_a, GPIO.OUT)
    GPIO.setup(fan_input_b, GPIO.OUT)

    # setup led

    led_pin = 25

    GPIO.setup(led_pin, GPIO.OUT)

    if check_gpio_is_enabled(led_pin):
        print('LED pin was enabled')
        GPIO.output(led_pin, led_pin)

    # run fun motor by default

    power_b = GPIO.PWM(fan_input_b, 500)
    power_b.start(70)

    def convert_distance_to_speed(distance):
        speed = 0

        integer = int(distance)

        if integer >= max_speed:
            speed = max_speed
        elif integer <= min_speed:
            speed = 20
        else:
            speed = integer + 20

        if speed >= max_speed:
            speed = 100

        print('Current speed is' + str(speed))

        power_b.ChangeDutyCycle(speed)

    def get_distance():
        GPIO.output(gpio_trigger, True)

        time.sleep(0.00001)
        GPIO.output(gpio_trigger, False)

        start_time = time.time()
        stop_time = time.time()

        # save StartTime
        while GPIO.input(gpio_echo) == 0:
            start_time = time.time()

        # save time of arrival
        while GPIO.input(gpio_echo) == 1:
            stop_time = time.time()

        # time difference between start and arrival
        time_elapsed = stop_time - start_time

        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        return (time_elapsed * 34300) / 2

    while True:
        distance = get_distance()

        convert_distance_to_speed(distance)

        time.sleep(0.5)


try:
    start_app()
except Exception as e:
    print(e)
    GPIO.cleanup()

finally:
    GPIO.cleanup()
