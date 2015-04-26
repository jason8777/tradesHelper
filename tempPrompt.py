

from colorama import init, Fore
import tempConv

#============================================================================#
#                       TEMP CONVERSION PROGRAM:                             #
#============================================================================#

#-----------------------------------------------------------------------------

def opt(number, symbol, name):
    """ Prints menu options to screen """
    print("{0:>3s} {1:<3s}{2:^5s}{3:<15s}"
          .format(number, symbol, "-->", name))

#-----------------------------------------------------------------------------

def primary_message(where):
    """ A message for the main switch """
    print(Fore.CYAN + "\n Select the unit you want to convert", where + "\n" +
          Fore.RESET)
    menu("Exit")

#-----------------------------------------------------------------------------

def secondary_message(t, unit):
    """ A message for the secondary switch """
    print(Fore.CYAN + "\n What would you like to convert " + str(t) + "\u00b0" + unit + " into?\n" + Fore.RESET)
    menu("Back")

#-----------------------------------------------------------------------------

def result_message(t, t2, unit, unit2):
    """ Prints the result to the screen """
    print(Fore.GREEN + "\n " + str(round(t, 2)) + "\u00b0" + unit +
          Fore.YELLOW +" --> " +
          Fore.GREEN + str(round(t2, 2)) + "\u00b0" + unit2 +
          Fore.RESET)

#-----------------------------------------------------------------------------

def menu(exit):
    """ This is the main menu for temp conversions """
    opt("1)", "\u00b0C", "Celsius")
    opt("2)", "\u00b0F", "Fahrenheit")
    opt("3)", "\u00b0K", "Kelvin")
    opt("4)", "\u00b0R", "Rankine")
    opt("5)", "\u00b0De", "Delisle")
    opt("6)", "\u00b0N", "Newton")
    opt("7)", "\u00b0R\u00e9", "R\u00e9aumur")
    opt("8)", "\u00b0R\u00f8", "R\u00f8mer")
    opt("9)", '', Fore.YELLOW + exit + "\n" + Fore.RESET)

#-----------------------------------------------------------------------------

def choice(x, y = 0):
    """ Checks user input """
    while True:
        try:
            choice = int(input(">>>"))   # <=== Check if it's an int
            if choice <= x and choice > 0 and choice != y: # <=== If choice in
                return choice        # range and not the same; return choice
                break
            elif choice == y:
                print(Fore.RED + "\n Can't convert to the same unit!" +
                      Fore.RESET)
            else:
                print(Fore.RED + "\n Invalid choice!\n" + Fore.RESET)
        except ValueError:          # <=== If choice is invalid prompt message
            print(Fore.RED + "\n Invalid input!\n" + Fore.RESET)

#-----------------------------------------------------------------------------

def value_input(unit):
    """ Asks user for temp. value, then checks it. """
    print(Fore.CYAN + "\n Enter the temperature in \u00b0" + unit + ":\n" +
          Fore.RESET)
    while True:
        try:
            value = float(input(">>>")) # <=== Make sure input is a float
            return value
            break
        except ValueError:
            print(Fore.RED + "\n Input must be an integer!\n" + Fore.RESET)

#-----------------------------------------------------------------------------

def value_check(unit, value):
    """ Check for value below absolute zero """
    while True:
        try:                        # <=== Checks that value isn't below abs 0
            t = value_input(unit)        # Returns value if okay
            if value(t) != None:
                return t
                break
        except ValueError:
            tempConv(t)

#-----------------------------------------------------------------------------

def main_switch():
    """" This is the main function """
    init()

    while True:
        primary_message("from:")        # <=== Display menu and take input
        x = choice(9)
        z = tempConv

        if x == 1:
            # This is the From Celsius options
            t = value_check("C", tempConv.cel_ran)
            secondary_message(t, "C")
            y = choice(9, 1)

            while True:
                if y == 2:
                    t2 = z.cel_fah(t)               # <=== Fahrenheit
                    result_message(t, t2, "C", "F")
                    break
                elif y == 3:
                    t2 = z.cel_kel(t)               # <=== Kelvin
                    result_message(t, t2, "C", "K")
                    break
                elif y == 4:
                    t2 = z.cel_ran(t)               # <=== Rankin
                    result_message(t, t2, "C", "R")
                    break
                elif y == 5:
                    t2 = z.cel_del(t)               # <=== Delisle
                    result_message(t, t2, "C", "De")
                    break
                elif y == 6:
                    t2 = z.cel_new(t)               # <=== Newton
                    result_message(t, t2, "C", "N")
                    break
                elif y == 7:
                    t2 = z.cel_rea(t)               # <=== Reaumur
                    result_message(t, t2, "C", "R\u00e9")
                    break
                elif y == 8:
                    t2 = z.cel_rom(t)               # <=== Romer
                    result_message(t, t2, "C", "R\u00f8")
                    break
                elif y == 9:
                    break

        elif x == 2:
            t = value_check("F", tempConv.fah_ran)
            secondary_message(t, "F")
            y = choice(9, 2)

            while True:
                if y == 1:
                    t2 = z.fah_cel(t)
                    result_message(t, t2, "F", "C")
                    break
                elif y == 3:
                    t2 = z.fah_kel(t)
                    result_message(t, t2, "F", "K")
                    break
                elif y == 4:
                    t2 = z.fah_ran(t)
                    result_message(t, t2, "F", "R")
                    break
                elif y == 5:
                    t2 = z.fah_del(t)
                    result_message(t, t2, "F", "De")
                    break
                elif y == 6:
                    t2 = z.fah_new(t)
                    result_message(t, t2, "F", "N")
                    break
                elif y == 7:
                    t2 = z.fah_rea(t)
                    result_message(t, t2, "F", "R\u00e9")
                    break
                elif y == 8:
                    t2 = z.fah_rom(t)
                    result_message(t, t2, "F", "R\u00f8")
                    break
                elif y == 9:
                    break

        elif x == 3:
            t = value_check("K", tempConv.kel_ran)
            secondary_message(t, "K")
            y = choice(9, 3)

            while True:
                if y == 1:
                    t2 = z.kel_cel(t)
                    result_message(t, t2, "K", "C")
                    break
                elif y == 2:
                    t2 = z.kel_fah(t)
                    result_message(t, t2, "K", "F")
                    break
                elif y == 4:
                    t2 = z.kel_ran(t)
                    result_message(t, t2, "K", "R")
                    break
                elif y == 5:
                    t2 = z.kel_del(t)
                    result_message(t, t2, "K", "De")
                    break
                elif y == 6:
                    t2 = z.kel_new(t)
                    result_message(t, t2, "K", "N")
                    break
                elif y == 7:
                    t2 = z.kel_rea(t)
                    result_message(t, t2, "K", "R\u00e9")
                    break
                elif y == 8:
                    t2 = z.kel_rom(t)
                    result_message(t, t2, "K", "R\u00f8")
                    break
                elif y == 9:
                    break

        elif x == 4:
            t = value_check("R", tempConv.ran_rea)
            secondary_message(t, "R")
            y = choice(9, 4)

            while True:
                if y == 1:
                    t2 = z.ran_cel(t)
                    result_message(t, t2, "R", "C")
                    break
                elif y == 2:
                    t2 = z.ran_fah(t)
                    result_message(t, t2, "R", "F")
                    break
                elif y == 3:
                    t2 = z.ran_kel(t)
                    result_message(t, t2, "R", "K")
                    break
                elif y == 5:
                    t2 = z.ran_del(t)
                    result_message(t, t2, "R", "De")
                    break
                elif y == 6:
                    t2 = z.ran_new(t)
                    result_message(t, t2, "R", "N")
                    break
                elif y == 7:
                    t2 = z.ran_rea(t)
                    result_message(t, t2, "R", "R\u00e9")
                    break
                elif y == 8:
                    t2 = z.ran_rom(t)
                    result_message(t, t2, "R", "R\u00f8")
                    break
                elif y == 9:
                    break

        elif x == 5:
            t = value_check("De", tempConv.del_ran)
            secondary_message(t, "De")
            y = choice(9, 5)

            while True:

                if y == 1:
                    t2 = z.del_cel(t)
                    result_message(t, t2, "De", "C")
                    break
                elif y == 2:
                    t2 = z.del_fah(t)
                    result_message(t, t2, "De", "F")
                    break
                elif y == 3:
                    t2 = z.del_kel(t)
                    result_message(t, t2, "De", "K")
                    break
                elif y == 4:
                    t2 = z.del_ran(t)
                    result_message(t, t2, "De", "R")
                    break
                elif y == 6:
                    t2 = z.del_new(t)
                    result_message(t, t2, "De", "N")
                    break
                elif y == 7:
                    t2 = z.del_rea(t)
                    result_message(t, t2, "De", "R\u00e9")
                    break
                elif y == 8:
                    t2 = z.del_rom(t)
                    result_message(t, t2, "De", "R\u00f8")
                    break
                elif y == 9:
                    break

        elif x == 6:
            t = value_check("N", tempConv.new_ran)
            secondary_message(t, "N")
            y = choice(9, 6)

            while True:

                if y == 1:
                    t2 = z.new_cel(t)
                    result_message(t, t2, "N", "C")
                    break
                elif y == 2:
                    t2 = z.new_fah(t)
                    result_message(t, t2, "N", "F")
                    break
                elif y == 3:
                    t2 = z.new_kel(t)
                    result_message(t, t2, "N", "K")
                    break
                elif y == 4:
                    t2 = z.new_ran(t)
                    result_message(t, t2, "N", "R")
                    break
                elif y == 5:
                    t2 = z.new_del(t)
                    result_message(t, t2, "N", "N")
                    break
                elif y == 7:
                    t2 = z.new_rea(t)
                    result_message(t, t2, "N", "R\u00e9")
                    break
                elif y == 8:
                    t2 = z.new_rom(t)
                    result_message(t, t2, "N", "R\u00f8")
                    break
                elif y == 9:
                    break

        elif x == 7:
            t = value_check("R\u00e9", tempConv.rea_ran)
            secondary_message(t, "R\u00e9")
            y = choice(9, 7)

            while True:

                if y == 1:
                    t2 = z.rea_cel(t)
                    result_message(t, t2, "R\u00e9", "C")
                    break
                elif y == 2:
                    t2 = z.rea_fah(t)
                    result_message(t, t2, "R\u00e9", "F")
                    break
                elif y == 3:
                    t2 = z.rea_kel(t)
                    result_message(t, t2, "R\u00e9", "K")
                    break
                elif y == 4:
                    t2 = z.rea_ran(t)
                    result_message(t, t2, "R\u00e9", "R")
                    break
                elif y == 5:
                    t2 = z.rea_del(t)
                    result_message(t, t2, "R\u00e9", "De")
                    break
                elif y == 6:
                    t2 = z.rea_new(t)
                    result_message(t, t2, "R\u00e9", "N")
                    break
                elif y == 8:
                    t2 = z.rea_rom(t)
                    result_message(t, t2, "R\u00e9", "R\u00f8")
                    break
                elif y == 9:
                    break

        elif x == 8:
            t = value_check("R\u00f8", tempConv.rom_ran)
            secondary_message(t, "R\u00f8")
            y = choice(9, 8)

            while True:

                if y == 1:
                    t2 = z.rom_cel(t)
                    result_message(t, t2, "R\u00f8", "C")
                    break
                elif y == 2:
                    t2 = z.rom_fah(t)
                    result_message(t, t2, "R\u00f8", "F")
                    break
                elif y == 3:
                    t2 = z.rom_kel(t)
                    result_message(t, t2, "R\u00f8", "K")
                    break
                elif y == 4:
                    t2 = z.rom_ran(t)
                    result_message(t, t2, "R\u00f8", "R")
                    break
                elif y == 5:
                    t2 = z.rom_del(t)
                    result_message(t, t2, "R\u00f8", "De")
                    break
                elif y == 6:
                    t2 = z.rom_new(t)
                    result_message(t, t2, "R\u00f8", "N")
                    break
                elif y == 7:
                    t2 = z.rom_rea(t)
                    result_message(t, t2, "R\u00f8", "R\u00e9")
                    break
                elif y == 9:
                    break

        elif x == 9:
            print(Fore.CYAN + "\n Goodbye!" + Fore.RESET)
            i = 0
            break

#-----------------------------------------------------------------------------

main_switch()
