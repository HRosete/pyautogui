import os
import subprocess
import time
import pyautogui
import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
image_path = os.path.join(os.getcwd(), "scopy_images")
screenshots_path = os.path.join(os.getcwd(), "screenshots")


def open_program_windows(dir):
    """open_program_windows: Opens a program in Windows OS from directory.

    parameters:
        dir: type=path
            Absolute/relative path to the application's executable
    """
    try:
        os.startfile(str(dir))
    except Exception as e:
        print(str(e))
        assert False, "Kindly install the latest release of the program/application."
    time.sleep(5)


def open_program_linux(app):
    """open_program_linux: Opens a program in Linux or Mac OS.

    global variable:
        PID: type=string
            The application's process ID
    parameters:
        app: type=string
            The application name that you want to stop
    """
    try:
        global PID
        subprocess.run(f"{app} &", shell=True, check=True)
        a = subprocess.run("echo $!", shell=True, capture_output=True)
        PID = a.stdout.decode()  # Call as common.PID
    except Exception as e:
        print(str(e))
        assert False, f"Kindly install the latest release of {app}."
    time.sleep(5)


def close_program_windows(app):
    """close_program_windows: Closes a program in Windows OS.

    parameters:
        app: type=string
            The application name and its extension that you want to stop
            Example: Scopy.exe
    """
    try:
        os.system(f"TASKKILL /F /IM {app}")
    except Exception as e:
        print(str(e))


def close_program_linux(pid):
    """close_program_linux: Closes a program in Linux and Mac OS on CLI.

    parameters:
        pid: type=string
            The process ID of the application you want to stop
    """
    try:
        subprocess.run(f"kill -15 {pid}", shell=True, check=True)
        time.sleep(1)
        subprocess.run(f"kill -9 {pid}", shell=True, check=True)
    except Exception as e:
        print(str(e))


def screenshot_region_and_save(dir, left, top, width, height, filename="screenshot.png"):
    """screenshot_region_and_save: Saves screenshot from pyautogui and returns the
    path, filename, and extension of the saved screenshot

    parameters:
        dir: type=path
            Path to where you want to save the screenshot
        left: type=int
            Left coordinate of the region to screenshot
        top: type=int
            Top coordinate of the region to screenshot
        width: type=int
            Width in pixels of the region to screenshot
        height: type=int
            Height in pixels of the region to screenshot
        filename: type=string
            Filename and extension for the screenshot
    return:
        file: type=path
            The path, filename,and extension of the saved screenshot
    """
    picture = pyautogui.screenshot(region=(left, top, width, height))
    file = os.path.join(dir, filename)
    picture.save(file)
    return file


def read_text_from_image(path_to_file, threshold=50):
    """read_text_from_image: Reads text from image/screenshot and returns it

    parameter:
        path_to_file: type=path
            The path, filename,and extension of the saved screenshot
        threshold: type=int
            Threshold value in pixel
    """
    pic = cv2.imread(path_to_file)
    gray_pic = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
    x, thresh = cv2.threshold(gray_pic, threshold, 255, cv2.THRESH_BINARY)
    text = pytesseract.image_to_string(thresh)
    # print("Text from file:", text)
    return text


def locate_image_with_str(img):
    """locate_image_with_str: Locates the image with text in the UI, confirms it,
    and returns a tuple of the location

    parameters:
        img: type=path
            Absolute/relative path of the image
    return:
        point: type=tuple
            x and y location coordinates in the UI
    """
    # img = os.path.join(image_path, "connect.png")

    # Reference image from filename
    coord = pyautogui.locateOnScreen(img, confidence=0.8)
    left, top, width, height = coord
    ref_text = read_text_from_image(img, threshold=130)

    # Text, image seen on the UI
    pic = screenshot_region_and_save(
        screenshots_path, left, top, width, height)
    ui_text = read_text_from_image(pic, threshold=130)

    # Compare ref's text and text
    if ui_text == ref_text:
        point = pyautogui.center(coord)
        return point
    elif coord == None:
        assert False, "The image with text can't be found on the screen."


def locate_and_click_image(img):
    """locate_and_click_image: Locates the specified image in the UI and clicks it.

    parameters:
        img: type=path
            Absolute/relative path of the image
    """
    image = pyautogui.locateCenterOnScreen(img, confidence=0.8)
    pyautogui.click(image)
    time.sleep(2)


def popup_dialog_box(cmd="close"):
    """popup_dialog_box: Interacts with the Automatic Update Dialog box in Scopy

    parameter:
        cmd: type=string
            Interaction needed for the dialog box.
            Options: yes, no, close
    """
    update_popup_img = os.path.join(image_path, "auto_update_popup.png")
    locate_and_click_image(update_popup_img)

    if cmd == "yes".lower():
        yes_img = os.path.join(image_path, "yes.png")
        locate_and_click_image(yes_img)
    elif cmd == "no".lower():
        no_img = os.path.join(image_path, "no.png")
        locate_and_click_image(no_img)
    elif cmd == "close".lower():
        close_img = os.path.join(image_path, "close.png")
        locate_and_click_image(close_img)
    time.sleep(3)


def choose_device(device, connection="usb"):
    """choose_device: Chooses a device to connect to.

    parameters:
        device: type=string
            The device that you want to connect to
            Options are: m2k
        connection: type=string
            Connection of the device with regards to your machine.
            Options are: usb, ip, demo
    """
    if device.lower() == "m2k":
        img = os.path.join(image_path, "m2k.png")
    # elif device.lower() == "pluto":
    #     img = os.path.join(image_path, "pluto.png")

    x, y = 0, 0
    coords = pyautogui.locateAllOnScreen(img, confidence=0.95)
    for c in coords:
        l, t, w, h = c
        s1 = screenshot_region_and_save(
            screenshots_path, l, (t + h), w, h-105, filename="s1.png")
        ui_text = read_text_from_image(s1, threshold=90)
        if connection.lower() == "demo":
            if "ip:127.0.0.1" in ui_text:
                x, y = pyautogui.center(c)
                break
            else:
                continue
        elif connection.lower() == "ip":
            if "ip:192" in ui_text:
                x, y = pyautogui.center(c)
                break
            else:
                continue
        elif connection.lower() == "usb":
            if connection in ui_text:
                x, y = pyautogui.center(c)
                break
            else:
                continue
    pyautogui.moveTo(x, y, 1, pyautogui.easeOutQuad)
    pyautogui.click()
    time.sleep(2)


def connect():
    """connect: Connect UI to the chosen device"""
    connect_img = os.path.join(image_path, "connect.png")
    x, y = locate_image_with_str(connect_img)
    pyautogui.moveTo(x, y, 1, pyautogui.easeOutQuad)
    pyautogui.click()
    print("Connecting...")
    time.sleep(25)


def disconnect():
    """disconnect: Donnect the chosen device to the UI"""
    disconnect_img = os.path.join(image_path, "disconnect.png")
    x, y = locate_image_with_str(disconnect_img)
    pyautogui.moveTo(x, y, 1, pyautogui.easeOutQuad)
    pyautogui.click()
    print("Disconnecting...")
    time.sleep(3)


def identify():
    """identify: Identify the chosen device"""
    identify_img = os.path.join(image_path, "identify.png")
    x, y = locate_image_with_str(identify_img)
    pyautogui.moveTo(x, y, 1, pyautogui.easeOutQuad)
    pyautogui.click()
    time.sleep(5)


def forget_device():
    """forget_device: Forget the chosen device"""
    forget_device_img = os.path.join(image_path, "forget_device.png")
    x, y = locate_image_with_str(forget_device_img)
    pyautogui.moveTo(x, y, 1, pyautogui.easeOutQuad)
    pyautogui.click()
    time.sleep(5)


def calibrate():
    """calibrate: Forget the chosen device"""
    calibrate_img = os.path.join(image_path, "calibrate.png")
    x, y = locate_image_with_str(calibrate_img)
    pyautogui.moveTo(x, y, 1, pyautogui.easeOutQuad)
    pyautogui.click()
    print("Calibrating...")
    time.sleep(10)


def enable_demo():
    """enable_demo: Enable M2K demo mode"""
    enable_demo_img = os.path.join(image_path, "enable_demo.png")
    x, y = locate_image_with_str(enable_demo_img)
    pyautogui.moveTo(x, y, 1, pyautogui.easeOutQuad)
    pyautogui.click()
    time.sleep(2)


def disable_demo():
    """disable_demo: Disable M2K demo mode"""
    disable_demo_img = os.path.join(image_path, "disable_demo.png")
    x, y = locate_image_with_str(disable_demo_img)
    pyautogui.moveTo(x, y, 1, pyautogui.easeOutQuad)
    pyautogui.click()
    time.sleep(2)


def add_device():
    """add_device: Add device through IP"""
    add_device_img = os.path.join(image_path, "add_device.png")
    x, y = locate_image_with_str(add_device_img)
    pyautogui.moveTo(x, y, 1, pyautogui.easeOutQuad)
    pyautogui.click()
    time.sleep(2)


def add():
    """add: Add device that is connected via IP"""
    add_img = os.path.join(image_path, "add.png")
    x, y = locate_image_with_str(add_img)
    pyautogui.moveTo(x, y, 1, pyautogui.easeOutQuad)
    pyautogui.click()
    time.sleep(2)


def register():
    """register: Register device's licence on myAnalog"""
    register_img = os.path.join(image_path, "register.png")
    x, y = locate_image_with_str(register_img)
    pyautogui.moveTo(x, y, 1, pyautogui.easeOutQuad)
    pyautogui.click()
    time.sleep(2)
    # Add steps for registering the device online


def screenshot_ui():
    pass
