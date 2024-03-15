frase = 'curso em video Python'
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print("""function encodeFeatureCollection(value) {
  var string = ee.String.encodeJSON(value)
  var stringLength = string.length()
  var maxLength = 100000
  var maxProperties = 1000
  var values = ee.List.sequence(0, stringLength, maxLength)
    .map(function (start) {
      start = ee.Number(start)
      var end = start.add(maxLength).min(stringLength)
      return string.slice(start, end)""")
# Análise

len(frase)  # Comprimento da frase
frase.count('o', 0, 13)  # Contar quantos 'o' tem na frase
frase.find('deo')  # Identifica o local onde está
frase.find('Android')  # Retorna -1, para quando não encontra
var = 'curso' in frase  # Retorna True ou False
frase.replace('Python', 'Android')  # Substitui
frase.upper()  # Maiúsculo
frase.lower()  # Minúsculo
frase.capitalize()  # Apenas a peimeira letra Maiúsculo
frase.title()  # Primeira letra de cada frase
frase.strip()  # Elimina espaços vazios no início e fim da string
frase.rstrip()  # Direita
frase.lstrip()  # Esquerda

# Divisão

frase.split()  # Divide a string em palavras separadas dentro de uma lista
'-'.join(frase)  # Juntar uma string que estão em lista
