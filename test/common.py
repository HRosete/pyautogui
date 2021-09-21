import pyautogui


def locate_and_click(img):
    """locate_and_click: Locate the specified image in the UI and click it.

    parameter:
        img: type=string
            Filename with extension of the image you want to find
    """
    image = pyautogui.locateCenterOnScreen(img, confidence=0.8)
    pyautogui.click(image)
    print(f"{img} clicked!")
