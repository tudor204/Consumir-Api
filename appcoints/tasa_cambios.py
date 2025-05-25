import requests

#invocar al método get con la url específica
#dirección con clave key válida
r = requests.get("https://rest.coinapi.io/v1/exchangerate/BTC/EUR?apikey=1da147e1-614b-4a9d-864f-74bcbd0134b0")

print("codigo http de respuesta: ",r.status_code)

print("cabecera: ",r.headers['content-type'])

print("enconding: ",r.encoding)

print("respuesta en str: ",r.text)
print(type(r.text))

print("respuesta en json: ",r.json())
print(type(r.json()))