from colorama import init, Fore
init()

#============================================================================#
#                    TEMPERATURE CONVERSION FUNCTIONS:                       #
#============================================================================#

#------------------------------ Warning Functions ----------------------------

def below_abs(temp):
    print(Fore.RED + "\n Value too low!!!\n" + Fore.RESET,
          Fore.YELLOW + temp,"is absolute zero..." + Fore.RESET)

#------------------------------- From Celsius --------------------------------

def cel_fah(c):
    """ Takes Celsius argument and returns Fahrenheit """
    if c < -273.15:        # <=== Check to see it c is below absolute zero
        below_abs("-273.15\u00b0C")
    else:
        f = c * (9/5) + 32
        return f

def cel_kel(c):
    """ Takes Celsius argument and returns Kelvin """
    if c < -273.15:        # <=== Check to see it c is below absolute zero
        below_abs("-273.15\u00b0C")
    else:
        k = c + 273.15
        return k

def cel_ran(c):
    """ Takes Celsius argument and returns Rankine """
    if c < -273.15:        # <=== Check to see it c is below absolute zero
        below_abs("-273.15\u00b0C")
    else:
        r = (c + 273.15) * (9/5)
        return r

def cel_del(c):
    """ Takes Celsius argument and returns Delisle """
    if c < -273.15:        # <=== Check to see it c is below absolute zero
        below_abs("-273.15\u00b0C")
    else:
        de = (100 - c) * (3/2)
        return de

def cel_new(c):
    """ Takes Celsius argument and returns Newton """
    if c < -273.15:        # <=== Check to see it c is below absolute zero
        below_abs("-273.15\u00b0C")
    else:
        n = c * (33/100)
        return n

def cel_rea(c):
    """ Takes Celsius argument and returns Reaumur """
    if c < -273.15:        # <=== Check to see it c is below absolute zero
        below_abs("-273.15\u00b0C")
    else:
        re = c * (4/5)
        return re

def cel_rom(c):
    """ Takes Celsius argument and returns Romer """
    if c < -273.15:        # <=== Check to see it c is below absolute zero
        below_abs("-273.15\u00b0C")
    else:
        ro = c * (21/40) + 7.5
        return ro

#------------------------------ From Fahrenheit ------------------------------

def fah_cel(f):
    """ Takes Fahrenheit argument and returns Celsius """
    if f < -459.67:        # <=== Check to see if f is below absolute zero
        below_abs("-459.67\u00b0F")
    else:
        c = (f - 32) * (5/9)
        return c

def fah_kel(f):
    """ Takes Fahrenheit argument and returns Kelvin """
    if f < -459.67:        # <=== Check to see if f is below absolute zero
        below_abs("-459.67\u00b0F")
    else:
        k = (f + 459.67) * (5/9)
        return k

def fah_ran(f):
    """ Takes Fahrenheit argument and returns Rankine """
    if f < -459.67:        # <=== Check to see if f is below absolute zero
        below_abs("-459.67\u00b0F")
    else:
        r = f + 459.67
        return r

def fah_del(f):
    """ Takes Fahrenheit argument and returns Delisle """
    if f < -459.67:        # <=== Check to see if f is below absolute zero
        below_abs("-459.67\u00b0F")
    else:
        de = (212 - f) * (5/6)
        return de

def fah_new(f):
    """ Takes Fahrenheit argument and returns Newton """
    if f < -459.67:        # <=== Check to see if f is below absolute zero
        below_abs("-459.67\u00b0F")
    else:
        n = (f - 32) * (11/60)
        return n

def fah_rea(f):
    """ Takes Fahrenheit argument and returns Reaumur """
    if f < -459.67:        # <=== Check to see if f is below absolute zero
        below_abs("-459.67\u00b0F")
    else:
        re = (f - 32) * (4/9)
        return re

def fah_rom(f):
    """ Takes Fahrenheit argument and returns Romer """
    if f < -459.67:        # <=== Check to see if f is below absolute zero
        below_abs("-459.67\u00b0F")
    else:
        ro = (f -32) * (7/24) + 7.5
        return ro

#----------------------------- From Kelvin -----------------------------------

def kel_cel(k):
    """ Takes Kelvin argument and returns Celsius """
    if k < 0:      # <=== Check to see if k is below absolute zero
        below_abs("0\u00b0K")
    else:
        c = k - 273.15
        return c

def kel_fah(k):
    """ Takes Kelvin argument and returns Fahrenheit """
    if k < 0:      # <=== Check to see if k is below absolute zero
        below_abs("0\u00b0K")
    else:
        f = k * (9/5) - 459.67
        return f

def kel_ran(k):
    """ Takes Kelvin argument and returns Rankine """
    if k < 0:      # <=== Check to see if k is below absolute zero
        below_abs("0\u00b0K")
    else:
        r = k * (9/5)
        return r

def kel_del(k):
    """ Takes Kelvin argument and returns Delisle """
    if k < 0:      # <=== Check to see if k is below absolute zero
        below_abs("0\u00b0K")
    else:
        de = (373.15 - k) * (3/2)
        return de

def kel_new(k):
    """ Takes Kelvin argument and returns Newton """
    if k < 0:      # <=== Check to see if k is below absolute zero
        below_abs("0\u00b0K")
    else:
        n = (k - 273.15) * (33/100)
        return n

def kel_rea(k):
    """ Takes Kelvin argument and returns Reaumur """
    if k < 0:      # <=== Check to see if k is below absolute zero
        below_abs("0\u00b0K")
    else:
        re = (k - 273.15) * (4/5)
        return re

def kel_rom(k):
    """ Takes Kelvin argument and returns Romer """
    if k < 0:      # <=== Check to see if k is below absolute zero
        below_abs("0\u00b0K")
    else:
        ro = (k - 273.15) * (21/40) + 7.5
        return ro

#---------------------------- From Rankine -----------------------------------

def ran_cel(r):
    """ Takes Rankine argument and returns Celsius """
    if r < 0:      # <=== Check to see if r is below absolute zero
        below_abs("0\u00b0R")
    else:
        c = (r - 491.67) * (5/9)
        return c

def ran_fah(r):
    """ Takes Rankine argument and returns Fahrenheit """
    if r < 0:      # <=== Check to see if r is below absolute zero
        below_abs("0\u00b0R")
    else:
        f = r - 459.67
        return f

def ran_kel(r):
    """ Takes Rankine argument and returns Kelvin """
    if r < 0:      # <=== Check to see if r is below absolute zero
        below_abs("0\u00b0R")
    else:
        k = r * (5/9)
        return k

def ran_del(r):
    """ Takes Rankine argument and returns Delisle """
    if r < 0:      # <=== Check to see if r is below absolute zero
        below_abs("0\u00b0R")
    else:
        de = (671.67 - r) * (5/6)
        return de

def ran_new(r):
    """ Takes Rankine argument and returns Newton """
    if r < 0:      # <=== Check to see if r is below absolute zero
        below_abs("0\u00b0R")
    else:
        n = (r - 491.76) * (11/60)
        return n

def ran_rea(r):
    """ Takes Rankine argument and returns Reaumur """
    if r < 0:      # <=== Check to see if r is below absolute zero
        below_abs("0\u00b0R")
    else:
        re = (r - 491.67) * (4/9)
        return re

def ran_rom(r):
    """ Takes Rankine argument and returns Romer """
    if r < 0:      # <=== Check to see if r is below absolute zero
        below_abs("0\u00b0R")
    else:
        ro = (r - 491.67) * (7/24) + 7.5
        return ro

#-------------------------- From Delisle -------------------------------------


def del_cel(de):
    """ Takes Delisle argument and returns Celsius """
    if de > 559.73:        # <=== Check to see if de is below absolute zero
        below_abs("559.73\u00b0De")
        print(Fore.YELLOW +
              " Note: \u00b0De, works the in the opposite direction of the",
               " others." + Fore.RESET)
    if de < -559.73:        # <=== Check to see if de is below absolute zero
        below_abs("-559.73\u00b0De")
    else:
        c = 100 - de * (2/3)
        return c

def del_fah(de):
    """ Takes Delisle argument and returns Fahrenheit """
    if de > 559.73:        # <=== Check to see if de is below absolute zero
        below_abs("559.73\u00b0De")
        print(Fore.YELLOW +
              " Note: \u00b0De, works the in the opposite direction of the",
               " others." + Fore.RESET)
    if de < -559.73:        # <=== Check to see if de is below absolute zero
        below_abs("-559.73\u00b0De")
    else:
        f = 212 - de * (6/5)
        return f

def del_kel(de):
    """ Takes Delisle argument and returns Kelvin """
    if de > 559.73:        # <=== Check to see if de is below absolute zero
        below_abs("559.73\u00b0De")
        print(Fore.YELLOW +
              " Note: \u00b0De, works the in the opposite direction of the",
               " others." + Fore.RESET)
    if de < -559.73:        # <=== Check to see if de is below absolute zero
        below_abs("-559.73\u00b0De")

    else:
        k = 373.15 - de * (2/3)
        return k

def del_ran(de):
    """ Takes Delisle argument and returns Rankine """
    if de > 559.73:        # <=== Check to see if de is below absolute zero
        below_abs("559.73\u00b0De")
        print(Fore.YELLOW +
              " Note: \u00b0De, works the in the opposite direction of the",
               " others." + Fore.RESET)
    if de < -559.73:        # <=== Check to see if de is below absolute zero
        below_abs("-559.73\u00b0De")
    else:
        r = 671.67 - de * (6/5)
        return r

def del_new(de):
    """ Takes Delisle argument and returns Newton """
    if de > 559.73:        # <=== Check to see if de is below absolute zero
        below_abs("559.73\u00b0De")
        print(Fore.YELLOW +
              " Note: \u00b0De, works the in the opposite direction of the",
               " others." + Fore.RESET)
    if de < -559.73:        # <=== Check to see if de is below absolute
        below_abs("-559.73\u00b0De")
    else:
        n = 33 - de * (11/50)
        return n

def del_rea(de):
    """ Takes Delisle argument and returns Reaumur """
    if de > 559.73:        # <=== Check to see if de is below absolute zero
        below_abs("559.73\u00b0De")
        print(Fore.YELLOW +
              " Note: \u00b0De, works the in the opposite direction of the",
               " others." + Fore.RESET)
    if de < -559.73:        # <=== Check to see if de is below absolute zero
        below_abs("-559.73\u00b0De")
    else:
        re = 80 - de * (11/50)
        return re

def del_rom(de):
    """ Takes Delisle argument and returns Romer """
    if de > 559.73:        # <=== Check to see if de is below absolute zero
        below_abs("559.73\u00b0De")
        print(Fore.YELLOW +
              " Note: \u00b0De, works the in the opposite direction of the",
               " others." + Fore.RESET)
    if de < -559.73:        # <=== Check to see if de is below absolute zero
        below_abs("-559.73\u00b0De")
    else:
        ro = 60 - de * (7/20)
        return ro

#-------------------------- From Newton --------------------------------------

def new_cel(n):
    """ Takes Newton argument and returns Celsius """
    if n < -90.14:     # <=== Check to see if n is below absolute zero
        below_abs("-90.14\u00b0N")
    else:
        c = n * (100/33)
        return c

def new_fah(n):
    """ Takes Newton argument and returns Fahrenheit """
    if n < -90.14:     # <=== Check to see if n is below absolute zero
        below_abs("-90.14\u00b0N")
    else:
        f = n * (60/11) + 32
        return f

def new_kel(n):
    """ Takes Newton argument and returns Kelvin """
    if n < -90.14:     # <=== Check to see if n is below absolute zero
        below_abs("-90.14\u00b0N")
    else:
        k = n * (100/33) + 273.15
        return k

def new_ran(n):
    """ Takes Newton argument and returns Rankine """
    if n < -90.14:     # <=== Check to see if n is below absolute zero
        below_abs("-90.14\u00b0N")
    else:
        r = n * (60/11) + 491.67
        return r

def new_del(n):
    """ Takes Newton argument and returns Delisle """
    if n < -90.14:     # <=== Check to see if n is below absolute zero
        below_abs("-90.14\u00b0N")
    else:
        de = (33 - n) * (50/11)
        return de

def new_rea(n):
    """ Takes Newton argument and returns Reaumur """
    if n < -90.14:     # <=== Check to see if n is below absolute zero
        below_abs("-90.14\u00b0N")
    else:
        re = n * (80/33)
        return re

def new_rom(n):
    """ Takes Newton argument and returns Romer """
    if n < -90.14:     # <=== Check to see if n is below absolute zero
        below_abs("-90.14\u00b0N")
    else:
        ro = n * (35/22) + 7.5
        return ro

#---------------------------- From Reaumur -----------------------------------

def rea_cel(re):
    """ Takes Reaumur argument and returns Celsius """
    if re < -218.52:       # <=== Check to see is re is below absolute zero
        below_abs("-218\u00b0R\u00e9")
    else:
        c = re * (5/4)
        return c

def rea_fah(re):
    """ Takes Reaumur argument and returns Fahrenheit """
    if re < -218.52:       # <=== Check to see is re is below absolute zero
        below_abs("-218\u00b0R\u00e9")
    else:
        f = re * (9/4) + 32
        return f

def rea_kel(re):
    """ Takes Reaumur argument and returns Kelvin """
    if re < -218.52:       # <=== Check to see is re is below absolute zero
        below_abs("-218\u00b0R\u00e9")
    else:
        k = re * (5/4) + 273.15
        return k

def rea_ran(re):
    """ Takes Reaumur argument and returns Rankine """
    if re < -218.52:       # <=== Check to see is re is below absolute zero
        below_abs("-218\u00b0R\u00e9")
    else:
        r = re * (9/4) + 491.67
        return r

def rea_del(re):
    """ Takes Reaumur argument and returns Delisle """
    if re < -218.52:       # <=== Check to see is re is below absolute zero
        below_abs("-218\u00b0R\u00e9")
    else:
        de = (80 - re) * (15/8)
        return de

def rea_new(re):
    """ Takes Reaumur argument and returns Newton """
    if re < -218.52:       # <=== Check to see is re is below absolute zero
        below_abs("-218\u00b0R\u00e9")
    else:
        n = re * (33/80)
        return n

def rea_rom(re):
    """ Takes Reaumur argument and returns Romer """
    if re < -218.52:       # <=== Check to see is re is below absolute zero
        below_abs("-218\u00b0R\u00e9")
    else:
        ro = re * (21/32) + 7.5
        return ro

#--------------------------- From Romer --------------------------------------

def rom_cel(ro):
    """ Takes Romer argument and returns Celsius """
    if ro < -135.90:       # <=== Check to see if ro is below absolute zero
        below_abs("-135.90\u00b0R\u00f8")
    else:
        c = (ro - 7.5) * (40/21)
        return c

def rom_fah(ro):
    """ Takes Romer argument and returns Fahrenheit """
    if ro < -135.90:       # <=== Check to see if ro is below absolute zero
        below_abs("-135.90\u00b0R\u00f8")
    else:
        f = (ro - 7.5) * (24/7) + 32
        return f

def rom_kel(ro):
    """ Takes Romer argument and returns Kelvin """
    if ro < -135.90:       # <=== Check to see if ro is below absolute zero
        below_abs("-135.90\u00b0R\u00f8")
    else:
        k = (ro - 7.5) * (40/21) + 273.15
        return k

def rom_ran(ro):
    """ Takes Romer argument and returns Rankine """
    if ro < -135.90:       # <=== Check to see if ro is below absolute zero
        below_abs("-135.90\u00b0R\u00f8")
    else:
        r = (ro - 7.5) * (24/7) + 491.67
        return r

def rom_del(ro):
    """ Takes Romer argument and returns Delisle """
    if ro < -135.90:       # <=== Check to see if ro is below absolute zero
        below_abs("-135.90\u00b0R\u00f8")
    else:
        de = (60 - ro) * (20/7)
        return de

def rom_new(ro):
    """ Takes Romer argument and returns Newton """
    if ro < -135.90:       # <=== Check to see if ro is below absolute zero
        below_abs("-135.90\u00b0R\u00f8")
    else:
        n = (ro - 7.5) * (22/35)
        return n

def rom_rea(ro):
    """ Takes Romer argument and returns Reaumur """
    if ro < -135.90:       # <=== Check to see if ro is below absolute zero
        below_abs("-135.90\u00b0R\u00f8")
    else:
        re = (ro - 7.5) * (32/21)
        return re
