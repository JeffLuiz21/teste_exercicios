def inverter_string(string):
    string_invertida = ""
    
    for i in range(len(string) - 1, -1, -1):
        string_invertida += string[i]
    
    return string_invertida

texto = "Olá, mundo!"
texto_invertido = inverter_string(texto)
print("Texto original:", texto)
print("Texto invertido:", texto_invertido)
