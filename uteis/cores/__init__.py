import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


''' ### COLORAMA - FORE, BACK, STYLE ### '''

# === FOREGROUND ===
frgW = Fore.WHITE
frgR = Fore.RED
frgG = Fore.GREEN
frgY = Fore.YELLOW
frgB = Fore.BLUE
frgM = Fore.MAGENTA
frgC = Fore.CYAN
frgP = Fore.BLACK
frg0 = Fore.RESET

# === BACKGROUND ===
bkgW = Back.WHITE
bkgR = Back.RED
bkgG = Back.GREEN
bkgY = Back.YELLOW
bkgB = Back.BLUE
bkgM = Back.MAGENTA
bkgC = Back.CYAN
bkgP = Back.BLACK
bkg0 = Back.RESET

# ======= STYLE =======
styD = Style.DIM
styN = Style.NORMAL
styB = Style.BRIGHT
styR = Style.RESET_ALL

#======================================================================================
if __name__ == '__main__':
    nome = 'Vladimir'
    print(f'{frgC+bkgR+styD}{nome}')
# =====================================================================================
