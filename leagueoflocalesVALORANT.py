# This program is meant to modify just the audio portion of VALORANT
# Ex. Korean Audio + English Text
# Date: 06/01/2020
# Last edit: 06/02/2020
# Created by Doomlad

from setuptools.command.easy_install import main as install
import os
import time
import urllib.request
from shutil import copyfile

try:
    import psutil
except ModuleNotFoundError:
    pass

english = "english"
deutsch = "dutch"
espanol = "spanish"
francais = "french"
bahasa_indonesia = "indonesian"
italiano = "italian"
japanese = "japanese"
korean = "korean"
polski = "polish"
portugues = "portuguese"
russian = "russian"
malaysian = "malaysian"
turkish = "turkish"
mandarin = "mandarin"


def prerequisites():

    package = 'psutil'

    try:
        return __import__(package)

    except ImportError:
        print("[!] Prerequisites not satisfied [!]\n")
        while True:
            print("You are missing the modules " + package + "\n(Install once and forget about it)")
            user_input = input("\nWould you like to install them? y/n: ")

            if user_input == 'y':
                print("Installing " + package + " via pip...", end="")
                install([package])
                print("Done!\nPlease restart the program.")
                counter = 4
                for count in range(3):
                    counter -= 1
                    print("Exiting in..." + str(counter), end="\r")
                    time.sleep(1)
                exit()

            elif user_input == 'n':
                print("\nThis program cannot function without " + package +
                      ", please consider installing to continue.\n")
                counter = 4
                for count in range(3):
                    counter -= 1
                    print("Exiting in..." + str(counter), end="\r")
                    time.sleep(1)
                exit()

            else:
                continue


folder_struct = r":\Riot Games\VALORANT\live\ShooterGame\Content\Paks"
potential_drives = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                    "U", "V", "W", "X", "Y", "Z"]


def update_check():

    version = open("version.txt", "r")
    __version__ = version.read()
    version.close()

    print("[*] Checking for updates...")
    update_program = urllib.request.urlopen\
        ("https://raw.githubusercontent.com/Doomlad/LeagueOfLocalesVALORANT/master/version.txt")
    read_update = update_program.read().decode('utf-8')

    if float(read_update) > float(__version__):
        print("[!] Update available: " + read_update, end="")
        print("[*] Visit https://github.com/Doomlad/LeagueOfLocalesVALORANT to download.")
    elif float(read_update) == float(__version__):
        print("[*] Currently running the latest version: " + __version__)
    else:
        print("[*] Strange version detected. Latest GitHub release: " + str(read_update))


def banner():
    print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n"
          " League of Locales: VALORANT \n"
          "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n\n"
          "[*] Folder structure: (Drive):\Riot Games\VALORANT\live\ShooterGame\Content\Paks \n\n"
          "[*] Changing folder names will result in program not working correctly. \n"
          "[*] Please do not modify default folder structure.")


def checkIfProcessRunning(process_name):
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if process_name.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


def main():
    prerequisites()
    update_check()
    print("[*] Prerequisites satisfied.")
    banner()
    while True:
        user_input = input("\nEnter your VALORANT install drive (Default is C): ")
        if user_input == "":
            drive_letter = "C"

        elif user_input.upper() in potential_drives:
            drive_letter = user_input

        elif user_input.lower() == "exit":
            counter = 4
            for count in range(4):
                time.sleep(1)
                counter -= 1
                print("Exiting in...", end='')
                print(str(counter))
            exit()

        else:
            print("Your input was not a valid drive letter. Please try again.")
            continue

        print("\n[+] Drive letter '" + drive_letter.upper() + "' selected.")

        try:
            path = drive_letter.upper() + folder_struct
            os.chdir(path)

            try:
                os.mkdir(os.path.expanduser("~\\Desktop") + "\\en_US_TextFiles", 0o755)
                print("[+] en_US_TextFiles directory created.")
                for file in os.listdir(path):
                    if file.startswith("en_US_Text"):
                        print("[*] File found: [" + file + "]")
                        print("[!] Copying " + file + " to en_US_TextFiles folder on your Desktop.")
                        src = path + "\\" + file
                        dst = os.path.expanduser("~\\Desktop") + "\\en_US_TextFiles\\" + file
                        copyfile(src, dst)
                        print("[*] File copied.")

            except FileExistsError:
                print("[*] en_US_TextFiles directory exists.")
                pass

            print("\n[*] All preliminary preparations complete!\n"
                  "[?] Note: Up till this point if you are logged into your account on the client,\n"
                  "[?] you will need to log out otherwise the game will just automatically start.\n"
                  "[?] To circumvent this, simply add the following to VALORANT's launch args: --disable-auto-launch\n")

            # user_input = input("Would you like to automatically scan for VALORANT and start it (y/n)?: ")
            user_input = 'y'
            if user_input.lower() == 'y':

                print("\n[!] Scanning your Desktop for VALORANT executable...")
                for root, dirs, files in os.walk(os.path.expanduser("~\\Desktop")):
                    for file in files:
                        if file.startswith("VALORANT"):
                            valorant = root + "\\" + file
                            print("\n[*] Found your VALORANT shortcut! [" + valorant + "]" +
                                  "\n[*] Launching VALORANT...")
                            os.startfile(valorant)
            else:
                print("\n[!] Manual mode selected. Please launch client manually and change to desired locale.")

            print("\n[*] Possible Locales [*]")

            locales_list = [english, deutsch, espanol, francais, bahasa_indonesia, italiano, japanese, korean, polski,
                            portugues, russian, malaysian, turkish, mandarin]
            counter = 0
            for loc in locales_list:
                counter += 1
                print("[" + str(counter) + "] " + loc.upper())

            while True:
                user_input = input("Enter your desired locale (number or word): ")

                if user_input.lower() == english or user_input == "1":
                    print("[!] " + english.upper() + " selected [!]")
                    locale_code = "en_US"
                    break

                elif user_input.lower() == deutsch or user_input == "2":
                    print("[!] " + deutsch.upper() + " selected [!]")
                    locale_code = "de_DE"
                    break

                elif user_input.lower() == espanol or user_input == "3":
                    print("[!] " + espanol.upper() + " selected [!]")
                    locale_code = "es_MX"
                    break

                elif user_input.lower() == francais or user_input == "4":
                    print("[!] " + francais.upper() + " selected [!]")
                    locale_code = "fr_FR"
                    break

                elif user_input.lower() == bahasa_indonesia or user_input == "5":
                    print("[!] " + bahasa_indonesia.upper() + " selected [!]")
                    locale_code = "id_ID"
                    break

                elif user_input.lower() == italiano or user_input == "6":
                    print("[!] " + italiano.upper() + " selected [!]")
                    locale_code = "it_IT"
                    break

                elif user_input.lower() == japanese or user_input == "7":
                    print("[!] " + japanese.upper() + " selected [!]")
                    locale_code = "ja_JP"
                    break

                elif user_input.lower() == korean or user_input == "8":
                    print("[!] " + korean.upper() + " selected [!]")
                    locale_code = "ko_KR"
                    break

                elif user_input.lower() == polski or user_input == "9":
                    print("[!] " + polski.upper() + " selected [!]")
                    locale_code = "pl_PL"
                    break

                elif user_input.lower() == portugues or user_input == "10":
                    print("[!] " + portugues.upper() + " selected [!]")
                    locale_code = "pt_BR"
                    break

                elif user_input.lower() == russian or user_input == "11":
                    print("[!] " + russian.upper() + " selected [!]")
                    locale_code = "ru_RU"
                    break

                elif user_input.lower() == malaysian or user_input == "12":
                    print("[!] " + malaysian.upper() + " selected [!]")
                    locale_code = "th_TH"
                    break

                elif user_input.lower() == turkish or user_input == "13":
                    print("[!] " + turkish.upper() + " selected [!]")
                    locale_code = "tr_TR"
                    break

                elif user_input.lower() == mandarin or user_input == "14":
                    print("[!] " + mandarin.upper() + " selected [!]")
                    locale_code = "zh_TW"
                    break

                else:
                    print("[!] Input out of bounds... Select an appropriate locale.")

            search_desired_text = locale_code + "_Text"

            print("[!] Killing VALORANT client processes...\n")
            os.system("taskkill /im RiotClientUx.exe /f")

            print("\n[*] Waiting 4 seconds to relaunch client...")
            time.sleep(4)

            for root, dirs, files in os.walk(os.path.expanduser("~\\Desktop")):
                for file in files:
                    if file.startswith("VALORANT"):
                        valorant = root + "\\" + file
                        print("\n[*] Found your VALORANT shortcut! [" + valorant + "]" +
                              "\n[*] Launching VALORANT...")
                        os.startfile(valorant)

            input("\n[!] Press ENTER when your client is finished patching...")

            # search_desired_text
            for file in os.listdir(path):
                if file.startswith(search_desired_text):
                    print("[*] File found: [" + file + "]")
                    print("[!] Deleting " + file + ".")
                    # locales_base_text = path + "\\" + file
                    os.chdir(path)
                    # os.system("rm " + file)
                    os.remove(file)
                    print("[*] File Deleted.")

            text_folder = os.path.expanduser("~\\Desktop") + "\\en_US_TextFiles\\"

            for file in os.listdir(text_folder):
                if file.startswith("en_US_Text"):
                    print("[*] File found: [" + file + "]")
                    print("[!] Copying " + file + " to en_US_TextFiles folder.")
                    src = os.path.expanduser("~\\Desktop") + "\\en_US_TextFiles\\" + file
                    dst = path + "\\" + file
                    # print(src + "\n" + dst)
                    copyfile(src, dst)
                    print("[*] File copied.")

            # en_US_Text-WindowsClient.pak
            # en_US_Text-WindowsClient.sig
            pak_file = path + "\\" + search_desired_text + "-WindowsClient.pak"
            sig_file = path + "\\" + search_desired_text + "-WindowsClient.sig"

            eng_pak = path + "\\en_US_Text-WindowsClient.pak"
            eng_sig = path + "\\en_US_Text-WindowsClient.sig"

            print("[!] Renaming english text file to desired locale...")
            os.rename(eng_pak, pak_file)
            os.rename(eng_sig, sig_file)
            print("[*] Done!")
            print("\n[!] All steps completed! Text should now be in english, just start VALORANT and Enjoy!")

            input("\nPress [ENTER] to exit program.")
            exit()

        except FileNotFoundError:
            print(f"\n[!] The path '{path}' does not exist. \n[!] Verify your VALORANT install location and try again.")


if __name__ == '__main__':
    main()
