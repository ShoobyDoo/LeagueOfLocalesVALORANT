import urllib.request


class Update:
    def __init__(self, local, filename=None, from_file=False):
        self.local = local
        self.from_file = from_file
        self.filename = filename

    def set_file(self, new_filename):
        


def update_check():
    try:
        version = open("version.txt", "r")
        __version__ = version.read()
        version.close()
    except Exception:
        __version__ = "1.1"
        print("[!] Error reading version from file... FALLING BACK TO LOCAL {}".format(
            __version__))

    print("[*] Checking for updates...")
    update_program = urllib.request.urlopen(
        "https://raw.githubusercontent.com/Doomlad/LeagueOfLocalesVALORANT/master/version.txt")
    read_update = update_program.read().decode('utf-8')

    if float(read_update) > float(__version__):
        print("[!] Update available: " + read_update)
        print(
            "[*] Visit https://github.com/Doomlad/LeagueOfLocalesVALORANT to download.")
    elif float(read_update) == float(__version__):
        print("[*] Currently running the latest version: " + __version__)
    else:
        print("[*] Strange version detected. Latest GitHub release: " +
              str(read_update))
