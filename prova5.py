# Definir a string (pode ser informada ou pré-definida)
string = input("Digite uma string: ")

# Inverter a string sem usar funções prontas
inverted_string = ""
for char in string:
    inverted_string = char + inverted_string  # Adiciona o caractere no início

# Exibir a string invertida
print("String invertida:", inverted_string)
