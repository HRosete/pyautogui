from os.path import dirname, join, realpath

import os
import pyautogui as pag
import time

# image_path = dirname(realpath(__file__)) + "/scopy_images/"
# m2k_image = image_path + "m2k.png"
connect_image = image_path + "connect.png"
identify_image = image_path + "identify.png"
cal_image = image_path + "calibrate.png"
osc_image = image_path + "oscilloscope.png"
spectrum_analyzer_image = image_path + "spectrum_analyzer.png"
network_analyzer_image = image_path + "network_analyzer.png"
sig_gen_image = image_path + "signal_generator.png"
logic_analyzer_image = image_path + "logic_analyzer.png"
pattern_generator_image = image_path + "pattern_generator.png"
dio_image = image_path + "digital_io.png"
voltmeter_image = image_path + "voltmeter.png"
power_image = image_path + "power_supply.png"


def locate_and_click(img):
    """locate_and_click: Locate the specified image in the UI and click it.

    parameter:
        img: type=string
            Filename with extension of the image you want to find
    """
    image = pag.locateCenterOnScreen(img)
    pag.click(image)


def main():
    dir = "C:\\Users\\hrosete\\Downloads\\Analog Devices\\Scopy\\Scopy.exe"

    # Open Scopy
    try:
        os.startfile(str(dir))
    except Exception as e:
        print(str(e))
        assert False, "Kindly install the latest release of Scopy here: https://github.com/analogdevicesinc/scopy/releases"

    # Wait for the program to open
    time.sleep(3)

    # Connect to M2K
    locate_and_click(m2k_image)
    time.sleep(2)
    locate_and_click(connect_image)
    # while pyautogui.locateCenterOnScreen("calibrating.png"):
    #     pyautogui.PAUSE
    time.sleep(2)

    calibrating = pyautogui.locateCenterOnScreen(
        calibrating_image, confidence=0.7)
    connecting = pyautogui.locateCenterOnScreen(
        connecting_image, confidence=0.7)
    if calibrating or connecting:
        time.sleep(2)
    else:
        print("Connected!")

    # Identify M2K
    locate_and_click(identify_image)
    time.sleep(3)

    # Calibrate M2K
    locate_and_click(cal_image)
    time.sleep(3)

    # Oscilloscope
    locate_and_click(osc_image)
    '''should call on the osc module after'''

    # Spectrum Analyzer
    locate_and_click(spectrum_analyzer_image)
    '''should call on the spec module after'''

    # # Network Analyzer
    # locate_and_click(network_analyzer_image)
    # '''should call on the network module after'''

    # # Signal Generator
    # locate_and_click(sig_gen_image)
    # '''should call on the siggen module after'''

    # # Logic Analyzer
    # locate_and_click(logic_analyzer_image)
    # '''should call on the logic module after'''

    # # Pattern Generator
    # locate_and_click(pattern_generator_image)
    # '''should call on the pattern module after'''

    # # Digital IO
    # locate_and_click(dio_image)
    # '''should call on the digital io module after'''

    # # Voltmeter
    # locate_and_click(voltmeter_image)
    # '''should call on the voltmeter module after'''

    # # Power Supply
    # locate_and_click(power_image)
    # '''should call on the power supply module after'''

    # # About


if __name__ == "__main__":
    main()
