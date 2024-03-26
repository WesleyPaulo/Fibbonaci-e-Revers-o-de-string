def inverter_string(string):
    
    # Converte a string para uma lista
    caracteres = list(string)
    
    # Obtém o comprimento da string
    tamanho = len(caracteres)
    
    # Cria uma lista vazia para os caracteres invertidos
    invertida = []
    
    # Itera reversamente pegando os caracteres e colocando na lista invertida
    for i in range(tamanho - 1, -1, -1):
        invertida.append(caracteres[i])
    
    # Cria a string com novos caracteres
    string_invertida = ''.join(invertida)
    
    return string_invertida

string = input("Digite uma string: ")
string_invertida = inverter_string(string)
print("String invertida:", string_invertida)