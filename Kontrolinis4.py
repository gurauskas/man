#
# Ketvirta užduotis - Tkinter
#
# Sukurti programą su TKinter. Programa turi turėti:
# Laukelį, į kurį įvedama temperatūrą
# Mygtuką, kurį paspaudus į laukelį įrašyta temperatūrą būtų konvertuojama iš farenheito į celsijų. Konvertuota temperatūra turi būti atvaizduota programoje kaip tekstas.
# Mygtuką, kurį paspaudus į laukelį įrašyta temperatūrą būtų konvertuojama iš celsijaus į farenhaitą. Konvertuota temperatūra turi būti atvaizduota programoje kaip tekstas.
# Tekstą, kuris atvaizduos temperatūros konvertavimo rezultatą
# #


from tkinter import *

langas = Tk()
langas.title('TEMPERATUROS ')
langas.geometry("250x200")
virsutinis = Frame(langas)
apatinis = Frame(langas)


def spausdinti():
    print("IS C I F ")


def spausdinti1():
    print("IS F I C !")

mygtukas1 = Button(langas, text="is c i f ", command=spausdinti)
mygtukas2 = Button(langas, text="is F i C", command=spausdinti1)
laukas2 = Entry(langas)
uzrasas = Label(langas, text="rezultatas :")

print("Spausdina!")
mygtukas1.grid(row=0, column=2)
mygtukas2.grid(row=5, column=2)
laukas2.grid(row=1 , column = 4)
uzrasas.grid(row=2 , column= 5)
langas.mainloop()
