import time
import pyautogui 


run_status = "nComplete"
run_count = 0

while run_status == "nComplete":
    #Click Start 
    pyautogui.click(824, 962)


    #Expert Map Button
    time.sleep(0.5)
    pyautogui.click(1340, 962)

    #Infernal Map Button
    time.sleep(0.5)
    pyautogui.click(1307, 661)

    #Easy Mode
    time.sleep(0.5)
    pyautogui.click(659, 414)

    #Deflation Mode
    time.sleep(0.5)
    pyautogui.click(1286, 450)

    #Ok Button Upon Loading
    time.sleep(3.5)
    pyautogui.click(948, 771)

    #Sniper Monkey
    time.sleep(0.5)
    pyautogui.click(1812, 643)

    #Place Sniper Monkey
    pyautogui.dragTo(1544, 600, duration=0.5)

    #Click On Sniper Monkey
    time.sleep(0.6)
    pyautogui.click(1544, 600)


    #Upgrade Sniper Monkey Faster Firing to Tier 4
    time.sleep(1.1)
    pyautogui.click(334, 794)
    time.sleep(0.1)
    pyautogui.click(334, 794)
    time.sleep(0.1)
    pyautogui.click(334, 794)
    time.sleep(0.1)
    pyautogui.click(334, 794)
    time.sleep(0.1)

    #Upgrade Sniper Monkey Night Vision Goggles to Tier 2
    time.sleep(1)
    pyautogui.click(324, 648)
    time.sleep(0.1)
    pyautogui.click(324, 648)
    #Sniper Monkey Completed




    #Click Quincy 
    time.sleep(0.2)
    pyautogui.click(1703, 222)
    pyautogui.dragTo(837, 324, duration=1.2)

    #Scroll Down To Alchemist
    time.sleep(0.5)
    pyautogui.moveTo(1703, 222, duration=0.3)
    time.sleep(0.8)
    pyautogui.scroll(-50)
    time.sleep(0.1)
    pyautogui.scroll(-50)
    time.sleep(0.1)
    pyautogui.scroll(-50)
    time.sleep(0.1)
    pyautogui.scroll(-50)
    time.sleep(0.1)
    pyautogui.scroll(-50)
    time.sleep(0.1)
    pyautogui.scroll(-50)
    time.sleep(0.1)
    pyautogui.scroll(-50)

    #Pick The Alchemist
    pyautogui.click(1803, 817)
    time.sleep(0.1)

    #Placing The Alchemist
    pyautogui.dragTo(1608, 513)

    #Upgrading The Alchemist
    time.sleep(0.1)
    pyautogui.click(1608, 513)
    time.sleep(0.1)

    #Upgrade Alchemist Larger Potions Tier 4
    pyautogui.click(316, 492)
    time.sleep(0.1)
    pyautogui.click(316, 492)
    time.sleep(0.1)
    pyautogui.click(316, 492)
    time.sleep(0.1)
    pyautogui.click(316, 492)
    time.sleep(0.1)

    #Upgrade Alchemist Stronger Acid Tier 2
    time.sleep(0.1)
    pyautogui.click(319, 635)
    time.sleep(0.1)
    pyautogui.click(319, 635)
    time.sleep(0.1)



    #Scroll Down To Second Alchemist
    time.sleep(0.1)
    pyautogui.moveTo(1703, 222, duration=0.3)
    time.sleep(0.2)
    pyautogui.scroll(-50)
    time.sleep(0.2)
    pyautogui.scroll(-50)
    time.sleep(0.2)
    pyautogui.scroll(-50)
    time.sleep(0.2)
    pyautogui.scroll(-50)
    time.sleep(0.2)
    pyautogui.scroll(-50)
    time.sleep(0.2)
    pyautogui.scroll(-50)
    time.sleep(0.2)
    pyautogui.scroll(-50)
    time.sleep(1)



    #Second Alchemist
    pyautogui.click(1825, 486)
    time.sleep(0.1)

    #Placing The Second Alchemist 
    pyautogui.dragTo(1594, 671, duration=0.1)
    time.sleep(0.5)
    pyautogui.click(1593, 654)
    time.sleep(0.5)

    #Upgrade Alchemist Larger Potions Tier 4 (SECOND ALC)
    pyautogui.click(322, 511)
    time.sleep(0.1)
    pyautogui.click(322, 511)
    time.sleep(0.1)
    pyautogui.click(322, 511)
    time.sleep(0.1)
    pyautogui.click(322, 511)
    time.sleep(0.1)

    #Upgrade Alchemist Faster Throwing Tier 2 (SECOND ALC)
    pyautogui.click(323, 822)
    time.sleep(0.1)
    pyautogui.click(323, 822)
    time.sleep(0.1)



    #Click Play and Speed Up
    time.sleep(0.3)
    pyautogui.click(1815, 998)
    time.sleep(0.1)
    pyautogui.click(1815, 998)

    game_State = "playing"
    level_check = 0

    #Checking for fail and Level Up 
    while game_State == "playing":
        pyautogui.click(741, 794)
        time.sleep(2)
        pyautogui.click(999, 0)
        run_status = "inGame"
        #Counts Game Time 
        time.sleep(19)
        level_check +=1
        print(level_check)

        if level_check == 16:
            game_State = "complete"
            pyautogui.click(943, 896)
            time.sleep(5)
            pyautogui.click(720, 853)

        else:
            game_State = "playing"
    #Reset Countdown
    while run_status == "inGame":
        print("Your run is over, you have 10 seconds to close the script if you wish, if not please ignore this message./n")
        run_count +=1 
        print("You have currently completed "+ str(run_count) + " runs.")
        time.sleep(10)
        run_status = "nComplete"

        


#16 count is end of run with no level up 
#18 should be safe to end run on
  