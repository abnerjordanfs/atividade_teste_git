
distancia = float
chovendo = bool

def valor_frete(distancia, chovendo):
    valor = 0
    if chovendo == True:
        valor = 2
    if distancia <= 5:
        valor += 5     
    elif distancia >5 and distancia <= 10:
        valor += 8
    else:
        valor += 10
    return valor
print("valor:", valor_frete(7.5,True))
