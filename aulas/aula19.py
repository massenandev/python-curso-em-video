# vai printar a frase inteira
# frase é um objeto, portanto, possui métodos
frase = 'Curso em Vídeo Python'
print(frase)

# vai printar o terceiro caractere da frase
frase = 'Curso em Vídeo Python'
print(frase[3])

# vai fatiar da 3a letra à 12a
frase = 'Curso em Vídeo Python'
print(frase[3:13])

# vai printar do inicio ao 13o caractere
frase = 'Curso em Vídeo Python'
print(frase[:13])

# vai printar do 13o ao final
frase = 'Curso em Vídeo Python'
print(frase[13:])

# vai printar a frase da posição 1 à 14a, pulando de 2 em 2 - tudo junto
frase = 'Curso em Vídeo Python'
print(frase[1:15:2])

# vai printar de onde não se sabe o início nem o final, pulando de 2 em 2
frase = 'Curso em Vídeo Python'
print(frase[::2])

# pra printar uma frase inteira grande:
print("""Welcome! Are you completely new to programming?
about why and how to get started whith Python. Fortunately
an experienced programmer in any programming language
(whatever it may be) can pick up Python very quickly.
Its also easy for beginners to use and learn, so jump in!""")

# pra contar quantas vezes tem a letra o
frase = 'Curso em vídeo Python'
print(frase.count('o'))

# pega a frase, joga pra maiuscula e conta quantas vezes tem O nessa frase em maiusculo
frase = 'Curso em vídeo Python'
print(frase.upper().count('o'))

# pra saber o tamanho da frase
frase = 'Curso em vídeo Python'
print(len(frase)) # .strip() remove os espaços em branco

# pra substituir, tendo possibilidade de mudar, mesmo strings sendo imutáveis em py
frase = 'Curso em vídeo Python'
print(frase.replace('Python', 'Android'))

# strings são imutáveis em python. Logo, ele não aceitaria:
#frase = 'Curso em vídeo Python'
#frase[0] = 'J'

# como o frase.replace não foi salva em nenhuma variável, não muda a string
frase = 'Curso em vídeo Python'
frase.replace('Python', 'Android')
print(frase) # logo, ele vai printar a linha 58 sem mudanças

# como estamos atribuindo a uma variável, agora sim, ele substituirá
frase = 'Curso em vídeo Python'
frase = frase.replace('Python', 'Android')
print(frase)

# pra verificar se curso está na frase:
frase = 'Curso em vídeo Python'
print('Curso' in frase) # booleano

# pra verificar se há uma palavra na frase e a posição:
frase = 'Curso em Vídeo Python' # o python é case sensitive
print(frase.find('video')) # -1 quer dizer que não existe
print(frase.find('Vídeo')) # na posição 9
print(frase.lower().find('video')) #

# frase dividida em várias listas
frase = 'Curso em Vídeo Python'
print(frase.split())

# mostra o primeiro item do array splitado
frase = 'Curso em Vídeo Python'
dividido = frase.split()
print(dividido[0])

# dentro do segundo item do array, pegue o caractere na terceira posição, de 0 a 3
frase = 'Curso em Vídeo Python'
dividido = frase.split()
print(dividido[2][3])