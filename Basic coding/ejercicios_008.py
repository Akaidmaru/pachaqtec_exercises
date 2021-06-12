counted_words = {}
remove_chars = ",¿?¡!\n'\"."

text = """Hola, mundo. Esto es una cadena, se supone que debe tener varias palabras pues 
vamos a realizar un conteo de frecuencia de las mismas usando el lenguaje de programación Python. 
Ya no sé qué escribir pero sigo escribiendo para que poco a poco la cadena sea más larga y el 
ejercicio de programación sea demostrable. Creo que con todo esto que he escrito es suficiente."""


for char in remove_chars:
    text = text.replace(char, "")

word_list = text.lower().split(" ")

for word in word_list:
    if word in counted_words:
        counted_words[word] += 1
    else:
        counted_words[word] = 1

for key, value in counted_words.items():
    print("La palabra", key, "aparece:", value, "veces")
