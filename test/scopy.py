from test.common import locate_and_click

import os
import pyautogui
import time

image_path = os.path.join(os.getcwd(), "scopy_images")
popup_update_img = os.path.join(image_path, "auto_update_popup.png")
# calibrating_img = os.path.join(image_path, "calibrating.png")
# connecting_img = os.path.join(image_path, "connecting.png")
# disconnect_2_img = os.path.join(image_path, "disconnect_2.png")


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
        locate_and_click(image_path, "auto_update_popup.png")
        time.sleep(2)
        # locate_and_click(image_path, "yes.png")
        # locate_and_click(image_path, "no.png")
        locate_and_click(image_path, "close.png")
        time.sleep(2)

    # Connect to M2K
    locate_and_click(image_path, "m2k.png")
    time.sleep(5)
    locate_and_click(image_path, "connect.png")
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
    locate_and_click(image_path, "oscilloscope.png")
    time.sleep(5)
    import scopy_instruments.oscilloscope as osc
    osc.main()

    # Spectrum Analyzer
    locate_and_click(image_path, "spectrum_analyzer.png")
    time.sleep(5)
    import scopy_instruments.spectrum_analyzer as spec
    spec.main()

    # Network Analyzer
    locate_and_click(image_path, "network_analyzer.png")
    time.sleep(5)
    import scopy_instruments.network_analyzer as network
    network.main()

    # Signal Generator
    locate_and_click(image_path, "signal_generator.png")
    time.sleep(5)
    import scopy_instruments.signal_generator as sig_gen
    sig_gen.main()

    # Logic Analyzer
    locate_and_click(image_path, "logic_analyzer.png")
    time.sleep(5)
    import scopy_instruments.logic_analyzer as logic
    logic.main()

    # Pattern Generator
    locate_and_click(image_path, "pattern_generator.png")
    time.sleep(5)
    import scopy_instruments.pattern_generator as pattern
    pattern.main()

    # Digital IO
    locate_and_click(image_path, "digital_io.png")
    time.sleep(5)
    import scopy_instruments.digital_io as dio
    dio.main()

    # Voltmeter
    locate_and_click(image_path, "voltmeter.png")
    time.sleep(5)
    import scopy_instruments.voltmeter as volt
    volt.main()

    # Power Supply
    locate_and_click(image_path, "power_supply.png")
    time.sleep(5)
    import scopy_instruments.power_supply as power
    power.main()

    # Add M2K through IP
    locate_and_click(image_path, "home.png")
    time.sleep(5)
    ip = "192.168.2.1"
    locate_and_click(image_path, "add_m2k.png")
    time.sleep(2)
    pyautogui.moveRel(0, 155, duration=0.5)
    pyautogui.click()
    pyautogui.PAUSE
    pyautogui.write(ip, interval=0.1)
    pyautogui.PAUSE
    locate_and_click(image_path, "connect.png")
    time.sleep(2)
    locate_and_click(image_path, "add.png")
    time.sleep(2)
    locate_and_click(image_path, "connect.png")
    time.sleep(2)

    # Enable Demo Mode
    locate_and_click(image_path, "home.png")
    time.sleep(5)
    locate_and_click(image_path, "add_m2k.png")
    time.sleep(2)
    locate_and_click(image_path, "enable_demo.png")
    time.sleep(2)

    # Disable Demo Mode
    locate_and_click(image_path, "home.png")
    time.sleep(5)
    locate_and_click(image_path, "disable_demo.png")
    time.sleep(2)

    # Identify M2K
    locate_and_click(image_path, "home.png")
    time.sleep(5)
    locate_and_click(image_path, "identify.png")
    time.sleep(15)

    # Calibrate M2k
    locate_and_click(image_path, "home.png")
    time.sleep(5)
    locate_and_click(image_path, "calibrate.png")
    time.sleep(15)

    # Disconnect M2k
    locate_and_click(image_path, "home.png")
    time.sleep(5)
    locate_and_click(image_path, "disconnect.png")
    time.sleep(3)
    print("Done!")

    # try:
    #     os.system("TASKKILL /F /IM Scopy.exe")
    # except Exception as e:
    #     print(str(e))


if __name__ == "__main__":
    main()
