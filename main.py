#M1L1 KODLAND
meme_dict = {
    "CRINGE": "Algo raro o embarazoso",
    "LOL": "Respuesta a algo gracioso",
    "ROFL": "Respuesta a algo gracioso o una broma (No muy usado hoy)",
    "CREEPY": "Aterrador, siniestro",
    "TROLL": "Alguien o una accion que intencionalmente molesta a otros"
}

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
    print(meme_dict[word])
else:
    # ¿Qué hacer si no se encuentra la palabra?
    print("No se encontro esa palabra (o esta mal escrita)")
