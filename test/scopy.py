from test.common import locate_and_click

import os
import pyautogui
import time

image_path = os.path.join(os.getcwd(), "scopy_images")
popup_update_img = os.path.join(image_path, "auto_update_popup.png")
yes_img = os.path.join(image_path, "yes.png")
no_img = os.path.join(image_path, "no.png")
close_img = os.path.join(image_path, "close.png")
home_img = os.path.join(image_path, "home.png")
m2k_img = os.path.join(image_path, "m2k.png")
add_m2k = os.path.join(image_path, "add_m2k.png")
cal_img = os.path.join(image_path, "calibrate.png")
calibrating_img = os.path.join(image_path, "calibrating.png")
connect_img = os.path.join(image_path, "connect.png")
connecting_img = os.path.join(image_path, "connecting.png")
disconnect_img = os.path.join(image_path, "disconnect.png")
disconnect_2_img = os.path.join(image_path, "disconnect_2.png")
add_img = os.path.join(image_path, "add.png")
enable_demo_img = os.path.join(image_path, "enable_demo.png")
disable_demo_img = os.path.join(image_path, "disable_demo.png")
identify_img = os.path.join(image_path, "identify.png")

osc_img = os.path.join(image_path, "oscilloscope.png")
spectrum_analyzer_img = os.path.join(image_path, "spectrum_analyzer.png")
network_analyzer_img = os.path.join(image_path, "network_analyzer.png")
sig_gen_img = os.path.join(image_path, "signal_generator.png")
logic_analyzer_img = os.path.join(image_path, "logic_analyzer.png")
pattern_generator_img = os.path.join(image_path, "pattern_generator.png")
dio_img = os.path.join(image_path, "digital_io.png")
voltmeter_img = os.path.join(image_path, "voltmeter.png")
power_img = os.path.join(image_path, "power_supply.png")


# def locate_and_click(img):
#     """locate_and_click: Locate the specified image in the UI and click it.

#     parameter:
#         img: type=string
#             Filename with extension of the image you want to find
#     """
#     image = pyautogui.locateCenterOnScreen(img, confidence=0.8)
#     pyautogui.click(image)
#     print(f"{img} clicked!")


def main():
    # Edit the path to Scopy in the dir argument
    dir = "C:\\Users\\hrosete\\Downloads\\Analog Devices\\Scopy\\Scopy.exe"
    pyautogui.FAILSAFE = False

    # Open Scopy
    try:
        os.startfile(str(dir))
    except Exception as e:
        print(str(e))
        assert False, "Kindly install the latest release of Scopy here: https://github.com/analogdevicesinc/scopy/releases"

    # Wait for the program to open
    time.sleep(5)

    # Automatic Update Dialog Box
    popup = pyautogui.locateCenterOnScreen(popup_update_img, confidence=0.8)
    if popup:
        locate_and_click(popup_update_img)
        time.sleep(2)
        # locate_and_click(yes_img)
        # locate_and_click(no_img)
        locate_and_click(close_img)
        time.sleep(2)

    # Connect to M2K
    locate_and_click(m2k_img)
    time.sleep(5)
    locate_and_click(connect_img)
    time.sleep(2)
    pyautogui.moveRel(0, 100, duration=0.5)

    # To debug
    # connecting = pyautogui.locateCenterOnScreen(connect_img, confidence=0.8)
    # while connecting or cal:
    #     pyautogui.PAUSE
    #     connecting = pyautogui.locateCenterOnScreen(
    #         connect_img, confidence=0.8)
    #     cal = pyautogui.locateCenterOnScreen(calibrating_img, confidence=0.8)
    #     if (connecting and cal) == False:
    #         break
    # print("M2K successfully connected!")
    time.sleep(20)

    # Oscilloscope
    locate_and_click(osc_img)
    time.sleep(5)
    import scopy_instruments.oscilloscope as osc
    osc.main()

    # Add M2K through IP
    locate_and_click(home_img)
    time.sleep(5)
    ip = "192.168.2.1"
    locate_and_click(add_m2k)
    time.sleep(2)
    pyautogui.moveRel(0, 155, duration=0.5)
    pyautogui.click()
    pyautogui.PAUSE
    pyautogui.write(ip, interval=0.1)
    pyautogui.PAUSE
    locate_and_click(connect_img)
    time.sleep(2)
    locate_and_click(add_img)
    time.sleep(2)
    locate_and_click(connect_img)
    time.sleep(2)

    # Enable Demo Mode
    locate_and_click(home_img)
    time.sleep(5)
    locate_and_click(add_m2k)
    time.sleep(2)
    locate_and_click(enable_demo_img)
    time.sleep(2)

    # Disable Demo Mode
    locate_and_click(home_img)
    time.sleep(5)
    locate_and_click(disable_demo_img)
    time.sleep(2)

    # Identify M2K
    locate_and_click(home_img)
    time.sleep(5)
    locate_and_click(identify_img)
    time.sleep(15)

    # Calibrate M2k
    locate_and_click(home_img)
    time.sleep(5)
    locate_and_click(cal_img)
    time.sleep(15)

    # Disconnect M2k
    locate_and_click(home_img)
    time.sleep(5)
    locate_and_click(disconnect_img)
    time.sleep(3)
    print("Done!")

    # try:
    #     os.system("TASKKILL /F /IM Scopy.exe")
    # except Exception as e:
    #     print(str(e))


if __name__ == "__main__":
    main()
