import os
import pyautogui


def locate_and_click(dir, filename):
    """locate_and_click: Locate the specified image in the UI and click it.

    parameters:
        dir: type=path
            Absolute/relative path to the images folder
        filename: type=string
            Filename with extension of the image you want to find
    """
    location = os.path.join(dir, filename)
    image = pyautogui.locateCenterOnScreen(location, confidence=0.8)
    pyautogui.click(image)
    print(f"{filename} clicked!")
