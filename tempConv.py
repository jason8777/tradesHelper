from colorama import init, Fore

init()

#============================================================================#
#                    TEMPERATURE CONVERSION FUNCTIONS:                       #
#============================================================================#

#------------------------------ Warning Functions ----------------------------

def below_abs(temp):
    print(Fore.RED + " Value too low!!!\n" + Fore.RESET,
          Fore.CYAN + temp,"is absolute zero..." + Fore.RESET)

#------------------------------- From Celsius --------------------------------

def cel_fah(c):
    """ Takes Celsius argument and returns Fahrenheit """
    if c >= -273.15:        # <=== Check to see it c is below absolute zero
        f = c * (9/5) + 32
        return f
    else:
        below_abs("-273.15\u00b0C")

def cel_kel(c):
    """ Takes Celsius argument and returns Kelvin """
    if c >= -273.15:        # <=== Check to see it c is below absolute zero
        k = c + 273.15
        return k
    else:
        below_abs("-273.15\u00b0C")

def cel_ran(c):
    """ Takes Celsius argument and returns Rankine """
    if c >= -273.15:        # <=== Check to see it c is below absolute zero
        r = (c + 273.15) * (9/5)
        return r
    else:
        below_abs("-273.15\u00b0C")

def cel_del(c):
    """ Takes Celsius argument and returns Delisle """
    if c >= -273.15:        # <=== Check to see it c is below absolute zero
        de = (100 - c) * (3/2)
        return de
    else:
        below_abs("-273.15\u00b0C")

def cel_new(c):
    """ Takes Celsius argument and returns Newton """
    if c >= -273.15:        # <=== Check to see it c is below absolute zero
        n = c * (33/100)
        return n
    else:
        below_abs("-273.15\u00b0C")

def cel_rea(c):
    """ Takes Celsius argument and returns Reaumur """
    if c >= -273.15:        # <=== Check to see it c is below absolute zero
        re = c * (4/5)
        return re
    else:
        below_abs("-273.15\u00b0C")

def cel_rom(c):
    """ Takes Celsius argument and returns Romer """
    if c >= -273.15:        # <=== Check to see it c is below absolute zero
        ro = c * (21/40) + 7.5
        return ro
    else:
        below_abs("-273.15\u00b0C")

#------------------------------ From Fahrenheit ------------------------------

def fah_cel(f):
    """ Takes Fahrenheit argument and returns Celsius """
    if f >= -459.67:        # <=== Check to see if f is below absolute zero
        c = (f - 32) * (5/9)
        return c
    else:
        below_abs("-459.67\u00b0F")

def fah_kel(f):
    """ Takes Fahrenheit argument and returns Kelvin """
    if f >= -459.67:        # <=== Check to see if f is below absolute zero
        k = (f + 459.67) * (5/9)
        return k
    else:
        below_abs("-459.67\u00b0F")

def fah_ran(f):
    """ Takes Fahrenheit argument and returns Rankine """
    if f >= -459.67:        # <=== Check to see if f is below absolute zero
        r = f + 459.67
        return r
    else:
        below_abs("-459.67\u00b0F")

def fah_del(f):
    """ Takes Fahrenheit argument and returns Delisle """
    if f >= -459.67:        # <=== Check to see if f is below absolute zero
        de = (212 - f) * (5/6)
        return de
    else:
        below_abs("-459.67\u00b0F")

def fah_new(f):
    """ Takes Fahrenheit argument and returns Newton """
    if f >= -459.67:        # <=== Check to see if f is below absolute zero
        n = (f - 32) * (11/60)
        return n
    else:
        below_abs("-459.67\u00b0F")

def fah_rea(f):
    """ Takes Fahrenheit argument and returns Reaumur """
    if f >= -459.67:        # <=== Check to see if f is below absolute zero
        re = (f - 32) * (4/9)
        return re
    else:
        below_abs("-459.67\u00b0F")

def fah_rom(f):
    """ Takes Fahrenheit argument and returns Romer """
    if f >= -459.67:        # <=== Check to see if f is below absolute zero
        ro = (f -32) * (7/24) + 7.5
        return ro
    else:
        below_abs("-459.67\u00b0F")

#----------------------------- From Kelvin -----------------------------------

def kel_cel(k):
    """ Takes Kelvin argument and returns Celsius """
    if k >= 0:      # <=== Check to see if k is below absolute zero
        c = k - 273.15
        return c
    else:
        below_abs("0\u00b0K")

def kel_fah(k):
    """ Takes Kelvin argument and returns Fahrenheit """
    if k >= 0:      # <=== Check to see if k is below absolute zero
        f = k * (9/5) - 459.67
        return f
    else:
        below_abs("0\u00b0K")

def kel_ran(k):
    """ Takes Kelvin argument and returns Rankine """
    if k >= 0:      # <=== Check to see if k is below absolute zero
        r = k * (9/5)
        return r
    else:
        below_abs("0\u00b0K")

def kel_del(k):
    """ Takes Kelvin argument and returns Delisle """
    if k >= 0:      # <=== Check to see if k is below absolute zero
        de = (373.15 - k) * (3/2)
        return de
    else:
        below_abs("0\u00b0K")

def kel_new(k):
    """ Takes Kelvin argument and returns Newton """
    if k >= 0:      # <=== Check to see if k is below absolute zero
        n = (k - 273.15) * (33/100)
        return n
    else:
        below_abs("0\u00b0K")

def kel_rea(k):
    """ Takes Kelvin argument and returns Reaumur """
    if k >= 0:      # <=== Check to see if k is below absolute zero
        re = (k - 273.15) * (4/5)
        return re
    else:
        below_abs("0\u00b0K")

def kel_rom(k):
    """ Takes Kelvin argument and returns Romer """
    if k >= 0:      # <=== Check to see if k is below absolute zero
        ro = (k - 273.15) * (21/40) + 7.45
        return ro
    else:
        below_abs("0\u00b0K")

#---------------------------- From Rankine -----------------------------------

def ran_cel(r):
    """ Takes Rankine argument and returns Celsius """
    if r >= 0:      # <=== Check to see if r is below absolute zero
        c = (r - 491.67) * (5/9)
        return c
    else:
        below_abs("0\u00b0R")

def ran_fah(r):
    """ Takes Rankine argument and returns Fahrenheit """
    if r >= 0:      # <=== Check to see if r is below absolute zero
        f = r - 459.67
        return f
    else:
        below_abs("0\u00b0R")

def ran_kel(r):
    """ Takes Rankine argument and returns Kelvin """
    if r >= 0:      # <=== Check to see if r is below absolute zero
        k = r * (5/9)
        return k
    else:
        below_abs("0\u00b0R")

def ran_del(r):
    """ Takes Rankine argument and returns Delisle """
    if r >= 0:      # <=== Check to see if r is below absolute zero
        de = (671.67 - r) * (5/9)
        return de
    else:
        below_abs("0\u00b0R")

def ran_new(r):
    """ Takes Rankine argument and returns Newton """
    if r >= 0:      # <=== Check to see if r is below absolute zero
        n = (r - 491.76) * (5/6)
        return n
    else:
        below_abs("0\u00b0R")

def ran_rea(r):
    """ Takes Rankine argument and returns Reaumur """
    if r >= 0:      # <=== Check to see if r is below absolute zero
        re = (r - 491.67) * (4/9)
        return re
    else:
        below_abs("0\u00b0R")

def ran_rom(r):
    """ Takes Rankine argument and returns Romer """
    if r >= 0:      # <=== Check to see if r is below absolute zero
        ro = (r - 491.67) * (7/24) + 7.5
        return ro
    else:
        below_abs("0\u00b0R")

#-------------------------- From Delisle -------------------------------------


def del_cel(de):
    """ Takes Delisle argument and returns Celsius """
    if de >= 559.73:        # <=== Check to see if de is below absolute zero
        c = 100 - de * (2/3)
        return c
    else:
        below_abs("559.73\u00b0De")

def del_fah(de):
    """ Takes Delisle argument and returns Fahrenheit """
    if de >= 559.73:        # <=== Check to see if de is below absolute zero
        f = 212 - de * (6/5)
        return f
    else:
        below_abs("559.73\u00b0De")

def del_kel(de):
    """ Takes Delisle argument and returns Kelvin """
    if de >= 559.73:        # <=== Check to see if de is below absolute zero
        k = 373.15 - de * (2/3)
        return k
    else:
        below_abs("559.73\u00b0De")

def del_ran(de):
    """ Takes Delisle argument and returns Rankine """
    if de >= 559.73:        # <=== Check to see if de is below absolute zero
        r = 671.67 - de * (6/5)
        return r
    else:
        below_abs("559.73\u00b0De")

def del_new(de):
    """ Takes Delisle argument and returns Newton """
    if de >= 559.73:        # <=== Check to see if de is below absolute zero
        n = 33 - de * (8/15)
        return n
    else:
        below_abs("559.73\u00b0De")

def del_rea(de):
    """ Takes Delisle argument and returns Reaumur """
    if de >= 559.73:        # <=== Check to see if de is below absolute zero
        re = 80 - de * (11/50)
        return re
    else:
        below_abs("559.73\u00b0De")

def del_rom(de):
    """ Takes Delisle argument and returns Romer """
    if de >= 559.73:        # <=== Check to see if de is below absolute zero
        ro = 60 - de * (7/20)
        return ro
    else:
        below_abs("559.73\u00b0De")

#-------------------------- From Newton --------------------------------------

def new_cel(n):
    """ Takes Newton argument and returns Celsius """
    if n >= -90.14:     # <=== Check to see if n is below absolute zero
        c = n * (100/33)
        return c
    else:
        below_abs("-90.14\u00b0N")

def new_fah(n):
    """ Takes Newton argument and returns Fahrenheit """
    if n >= -90.14:     # <=== Check to see if n is below absolute zero
        f = n * (60/11) + 32
        return f
    else:
        below_abs("-90.14\u00b0N")

def new_kel(n):
    """ Takes Newton argument and returns Kelvin """
    if n >= -90.14:     # <=== Check to see if n is below absolute zero
        k = n * (100/33) + 273.15
        return k
    else:
        below_abs("-90.14\u00b0N")

def new_ran(n):
    """ Takes Newton argument and returns Rankine """
    if n >= -90.14:     # <=== Check to see if n is below absolute zero
        r = n * (60/11) + 491.67
        return r
    else:
        below_abs("-90.14\u00b0N")

def new_del(n):
    """ Takes Newton argument and returns Delisle """
    if n >= -90.14:     # <=== Check to see if n is below absolute zero
        de = (33 - n) * (50/11)
        return de
    else:
        below_abs("-90.14\u00b0N")

def new_rea(n):
    """ Takes Newton argument and returns Reaumur """
    if n >= -90.14:     # <=== Check to see if n is below absolute zero
        re = n * (35/22) + 7.5
        return re
    else:
        below_abs("-90.14\u00b0N")

def new_rom(n):
    """ Takes Newton argument and returns Romer """
    if n >= -90.14:     # <=== Check to see if n is below absolute zero
        ro = n * (35/22) + 7.5
        return ro
    else:
        below_abs("-90.14\u00b0N")

#---------------------------- From Reaumur -----------------------------------

def rea_cel(re):
    """ Takes Reaumur argument and returns Celsius """
    if re >= -218.52:       # <=== Check to see is re is below absolute zero
        c = re * (5/4)
        return c
    else:
        below_abs("-218\u00b0R\u00e9")

def rea_fah(re):
    """ Takes Reaumur argument and returns Fahrenheit """
    if re >= -218.52:       # <=== Check to see is re is below absolute zero
        f = re * (9/4) + 32
        return f
    else:
        below_abs("-218\u00b0R\u00e9")

def rea_kel(re):
    """ Takes Reaumur argument and returns Kelvin """
    if re >= -218.52:       # <=== Check to see is re is below absolute zero
        k = re * (5/4) + 273.15
        return k
    else:
        below_abs("-218\u00b0R\u00e9")

def rea_ran(re):
    """ Takes Reaumur argument and returns Rankine """
    if re >= -218.52:       # <=== Check to see is re is below absolute zero
        r = re * (9/4) + 491.67
        return r
    else:
        below_abs("-218\u00b0R\u00e9")

def rea_del(re):
    """ Takes Reaumur argument and returns Delisle """
    if re >= -218.52:       # <=== Check to see is re is below absolute zero
        de = (80 - re) * (15/8)
        return de
    else:
        below_abs("-218\u00b0R\u00e9")

def rea_new(re):
    """ Takes Reaumur argument and returns Newton """
    if re >= -218.52:       # <=== Check to see is re is below absolute zero
        n = re * (33/80)
        return n
    else:
        below_abs("-218\u00b0R\u00e9")

def real_rom(re):
    """ Takes Reaumur argument and returns Romer """
    if re >= -218.52:       # <=== Check to see is re is below absolute zero
        ro = re * (21/32) + 7.5
        return ro
    else:
        below_abs("-218\u00b0R\u00e9")

#--------------------------- From Romer --------------------------------------

def rom_cel(ro):
    """ Takes Romer argument and returns Celsius """
    if ro >= -135.90:       # <=== Check to see if ro is below absolute zero
        c = (ro - 7.5) * (40/21)
        return c
    else:
        below_abs("-135.90\u00b0R\u00f8")

def rom_fah(ro):
    """ Takes Romer argument and returns Fahrenheit """
    if ro >= -135.90:       # <=== Check to see if ro is below absolute zero
        f = (ro - 7.5) * (24/7) + 32
        return f
    else:
        below_abs("-135.90\u00b0R\u00f8")

def rom_kel(ro):
    """ Takes Romer argument and returns Kelvin """
    if ro >= -135.90:       # <=== Check to see if ro is below absolute zero
        k = (ro - 7.5) * (40/21) + 273.15
        return k
    else:
        below_abs("-135.90\u00b0R\u00f8")

def rom_ran(ro):
    """ Takes Romer argument and returns Rankine """
    if ro >= -135.90:       # <=== Check to see if ro is below absolute zero
        r = (ro - 7.5) * (24/7) + 491.67
        return r
    else:
        below_abs("-135.90\u00b0R\u00f8")

def rom_del(ro):
    """ Takes Romer argument and returns Delisle """
    if ro >= -135.90:       # <=== Check to see if ro is below absolute zero
        de = (60 - ro) * (20/7)
        return de
    else:
        below_abs("-135.90\u00b0R\u00f8")

def rom_new(ro):
    """ Takes Romer argument and returns Newton """
    if ro >= -135.90:       # <=== Check to see if ro is below absolute zero
        n = (ro - 7.5) * (22/35)
        return n
    else:
        below_abs("-135.90\u00b0R\u00f8")

def rom_rea(ro):
    """ Takes Romer argument and returns Reaumur """
    if ro >= -135.90:       # <=== Check to see if ro is below absolute zero
        re = (ro - 7.5) * (32/21)
        return re
    else:
        below_abs("-135.90\u00b0R\u00f8")
