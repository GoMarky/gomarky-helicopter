import time
import RPi.GPIO as GPIO


def get_pin_number(port_number):
    return port_number


def check_gpio_is_enabled(port_number):
    channel_is_on = GPIO.input(port_number)

    return channel_is_on


smoke_detector_pin = get_pin_number(7)


def start_app():
    times = 0

    def action():
        print('Sensor detected action!')

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(smoke_detector_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    GPIO.add_event_detect(smoke_detector_pin, GPIO.RISING)
    GPIO.add_event_callback(smoke_detector_pin, action)

    while True:
        times += 1

        print('alive ', str(times))
        time.sleep(0.5)


try:
    start_app()
except Exception as e:
    print(e)
    GPIO.cleanup()
finally:
    GPIO.cleanup()
