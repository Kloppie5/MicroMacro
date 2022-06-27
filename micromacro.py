import keyboard
import pyautogui
import time

points = []

def main ( ):
    while True:
        if keyboard.is_pressed('m'):
            print("Starting...")
            time.sleep(1)
            keep_clicking()
        if keyboard.is_pressed('a'):
            point = pyautogui.position()
            print(f"Adding point {point}")
            points.append(point)
            time.sleep(1)
        if keyboard.is_pressed('c'):
            print(f"Current position: {pyautogui.position()}")
            print(f"Current points: {points}")
            time.sleep(1)

def keep_clicking ( ):
    while True:
        for point in points:
            print(f"Clicking on {point}")
            pyautogui.click(point)
            time.sleep(0.1)
        if keyboard.is_pressed('q'):
            print("Stopping...")
            break

# main
if __name__ == '__main__':
    main()
