import requests
si = 0
while si == 0:
    si = int(input("Ingresar usuario para buscar (0) o buscar por defecto el 179571326? (1):  "))
    if si == 0:
        seller_id = input("Ingresar usuario: ")
        url = "https://api.mercadolibre.com/sites/MLA/search?seller_id=" + seller_id
        respuesta = requests.get(url)
        response_json = respuesta.json()
        resultados= response_json["results"]
        log = open("Log-" + seller_id + ".txt", "w")
        for item in resultados:
            log.write("ID: " + item["id"] + "\n")
            log.write("Título: " + item["title"] + "\n")
            log.write("Categoria: " + item["category_id"] + "\n")
            log.write("\n")
        log.close()
    else:
        url = "https://api.mercadolibre.com/sites/MLA/search?seller_id=179571326"
        respuesta = requests.get(url)
        response_json = respuesta.json()
        resultados = response_json["results"]
        log = open("Log-" + seller_id + ".txt", "w")
        for item in resultados:
            log.write("ID: " + item["id"] + "\n")
            log.write("Título: " + item["title"] + "\n")
            log.write("Categoria: " + item["category_id"] + "\n")
            log.write("\n")
        log.close()
