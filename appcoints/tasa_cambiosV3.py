import requests
from config import APIKEY
from models import *

allcoin = AllCoinApiIo()

#consulta de todas las monedas

allcoin.getAllcoins(APIKEY)


print(f"La cantidad de criptos son: {len(allcoin.lista_criptos)}.\
        y la cantidad de no criptos son: {len(allcoin.lista_no_criptos)}")


############################################################
        
moneda_cripto = input("Ingrese una criptomoneda válida ").upper()

while moneda_cripto != "" and moneda_cripto.isalpha() == True:  
    if moneda_cripto in allcoin.lista_criptos:
        r = requests.get(f"https://rest.coinapi.io/v1/exchangerate/{moneda_cripto}/EUR?apikey={APIKEY}")
        respuesta = r.json()
        if r.status_code == 200:
            print("{:,.2f}€".format(respuesta["rate"]))
            break
        else:
            print(respuesta["error"])
    moneda_cripto = input("Ingrese una criptomoneda válida ").upper()  

