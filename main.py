# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
from math import hypot
oposto = float(input('informe o comprimento do cateto oposto: '))
adjacente = float(input('informe o comprimento do cateto adjacente:' ))
hipotenusa = hypot(oposto, adjacente)
print('de acordo com o comprimento do cateto oposto {} e do adjacente {},')
'o comprimento da hipotenusa e  {:.2f}'.format(oposto, adjacente, hipotenusa)

'''oposto = float(input('comprimento do cateto oposto '))
adjacente = float(input('comprimento do cateto adjacente'))
hipotenusa = (oposto ** 2 + adjacente ** 2) ** (1/2)
print('a hipotenusa vai medir {:.2f}'.format (hipotenusa))'''
