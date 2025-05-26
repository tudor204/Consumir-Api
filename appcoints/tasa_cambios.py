import requests

apikey = "1da147e1-614b-4a9d-864f-74bcbd0134b0"
#Ejercicio 3, crear inputa para cargar la moneda digital
moneda_cripto = input("Ingrese una criptomoneda válida ").upper()

while moneda_cripto != "" and moneda_cripto.isalpha() == True:

    #invocar al método get con la url específica
    r = requests.get(f"https://rest.coinapi.io/v1/exchangerate/{moneda_cripto}/EUR?apikey={apikey}")

    respuesta = r.json()

    #Ejercicio 2, capturar errores
    if r.status_code == 200:
    #ejercicio 1, capturar el rate
        print("{:,.2f}€".format(respuesta["rate"]))
        break
    else:
        print(respuesta["error"])

    moneda_cripto = input("Ingrese una criptomoneda válida ").upper()



    



"""
print("codigo http de respuesta: ",r.status_code)
print("cabecera: ",r.headers['content-type'])
print("enconding: ",r.encoding)
print("respuesta en str: ",r.text)
print(type(r.text))
print("respuesta en json: ",r.json())
print(type(r.json()))
"""