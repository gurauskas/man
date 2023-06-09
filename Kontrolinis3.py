import logging

# Nustatome loggerio konfigūraciją
logging.basicConfig(filename='rezultatai.log', level=logging.INFO, encoding="UTF-8" ,format='%(asctime)s - %(message)s')

def apskaiciuoti_plota_ir_perimetra(ilgis, plotis):
    plotas = ilgis * plotis
    perimetras = 2 * (ilgis + plotis)
    return plotas, perimetras

def ivesti_reiksmes():
    ilgis = float(input("Įveskite stačiakampio ilgį: "))
    plotis = float(input("Įveskite stačiakampio plotį: "))
    return ilgis, plotis

def main():
    ilgis, plotis = ivesti_reiksmes()
    plotas, perimetras = apskaiciuoti_plota_ir_perimetra(ilgis, plotis)

    # Išspausdiname rezultatą į terminalą
    print("Plotas:", plotas)
    print("Perimetras:", perimetras)

    # Įrašome rezultatą į failą naudodami loggerį
    logging.info("Plotas: %s", plotas)
    logging.info("Perimetras: %s", perimetras)

if __name__ == '__main__':
    main()