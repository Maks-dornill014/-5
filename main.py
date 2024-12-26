import colorama
from colorama import init, Fore, Back, Style
import inspect


init(autoreset=True)


print(Fore.RED + "Цей текст червоного кольору")
print(Back.GREEN + "Цей текст із зеленим фоном")
print(Style.BRIGHT + "Цей текст яскравий")
print(Style.RESET_ALL + "Цей текст зі скинутими стилями")


print("\nДоступні кольори в Fore:")
print(dir(Fore))

print("\nДоступні кольори в Back:")
print(dir(Back))

print("\nДоступні стилі в Style:")
print(dir(Style))


from colorama.ansitowin32 import AnsiToWin32

print("\nМетоди та атрибути класу AnsiToWin32:")
print(inspect.getmembers(AnsiToWin32, predicate=inspect.isfunction))


print("\nДокументація для функції init:")
print(inspect.getdoc(init))


import sys
ansi_converter = AnsiToWin32(sys.stdout)
ansi_converter.write(Fore.BLUE + "Текст синього кольору через AnsiToWin32\n")
