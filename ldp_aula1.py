# -*- coding: utf-8 -*-
"""LDP-aula1

**Conteudo Web 1- Aula 1 Variáveis e tipos de dados**
"""

Nota_1 = int(input("Digite a primeira nota:"))
Nota_2 = int(input("Digite a segunda nota:"))
Nota_3 = int(input("Digite a terceira nota:"))
Nota_4 = int(input("Digite a quarta nota:"))
#observe que utuilizamos a função int(), pois sem ela o python entenderia as notas como string, pois todo retorno de input por padrão é uma string

#Obtendo a média
media = (Nota_1 + Nota_2 + Nota_3 + Nota_4)/4

#Condição para a aprovação do aluno
if media >= 6:
  situacao = "Aprovado"
else:
  situacao = "Reprovado"

#Média final e situação do aluno
print(f"A média das notas é: {media}")
print(f"O aluno está: {situacao}")

"""**Aula 2 Estrutras condicionais**"""

1 > 2

1 == 2

a = "aluna"
b = "aluno"
a is b

"""No Brasil o voto é facultativo para pessoas entre 16 e 18 e maiores de 70 anos.

```
elif 16 <= idade < 18 or idade > 70:
    return "Voto facultativo."
```

Sendo assim, segue a lógica do programa que determina se o voto é obrigatório ou não para determinada data de nascimento:
"""

from datetime import date

# Função para calcular a idade
def calcular_idade(ano_nascimento):
    ano_atual = date.today().year
    return ano_atual - ano_nascimento

# Função para verificar se o voto é obrigatório
def verificar_voto(ano_nascimento):
    idade = calcular_idade(ano_nascimento)

    if idade < 16:
        return "Não pode votar."
    elif 16 <= idade < 18 or idade > 70:
        return "Voto facultativo."
    else:
        return "Voto obrigatório."

ano_nascimento = int(input("Digite o ano de nascimento: "))
resultado = verificar_voto(ano_nascimento)
print(resultado)

"""
Note que utilizamos o operador booleano OR que indica que o voto é facultativo
para maior ou igual a 16 anos e menor que 18
OU
para idades maiores do que 70 anos
e dessa forma é possivel através de duas logicas diferentes criar critérios mais complexos
"""

"""**Aula 3 Estruturas de Repetição**"""

numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    print(numero)

numero = int(input("Digite um número ou 0 para sair:"))
while numero != 0:
  if numero % 2 == 0:
    print("O número é par")
  else:
    print("O número é impar")
  numero = int(input("Digite outro número ou 0 para sair:"))

for numero in range(1, 11):
    if numero % 2 == 0:
        print("O primeiro número par encontrado é:", numero)
        break

for numero in range(1, 11):
    if numero == 5:
        continue
    print(numero)

#Lista de Filmes para classificação
filmes = ["Matrix","Titanic","O poderoso cherfão","Jurassic Park","Avatar"]
filmes

#Mensagem de boas-vindas
print("Bem-vindo à classificação de filmes")
print("Você terá cinco filmes para classificar")
print("Digite 0 a qualquer momento para sair da classificação")

#Loop para iterar sobre cada filme na lista
for filme in filmes:
  #Solicita a classificação do usuario
  classificacao = int(input(f"Como você classificaria '{filme}' de 1 a 5? (0 para sair):"))
  #Verifica se o usuario deseja parar
  if classificacao == 0:
    print("É uma pena que você não irá mais classificar filmes")
    break #Ecerra o loop
  #Verifica se a classificação é um valor válido
  if classificacao < 1 or classificacao > 5:
    print("Digite um valor válido (1 a 5) para classificação")
  else:
  #Exibe a classificação e passa para o proximo filme
    print(f"Você classificou o filme '{filme}' com {classificacao} estrelas")
#Agradecimentod no final do loop
print("Agradecemos a sua participação na classificação de filmes")

"""**Aula 4 Funções**"""

# Cria uma lista de números
numeros = [1, 2, 3, 4, 5]

# Usa a função len() para calcular o comprimento da lista
comprimento = len(numeros)

# Usa a função print() que exibe o objeto no formato de texto
print(comprimento)

# Definindo uma função chamada "soma"
def soma(a, b):
    resultado = a + b
    return resultado

# Chamando a função e armazenando o resultado em uma variável
a = int(input("Digite o primeiro valor da soma: "))
b = int(input("Digite o segundo valor da soma: "))
resultado_soma = soma(a, b)


# Imprimindo o resultado
print(resultado_soma)

# função lambda para calcular o quadrado de um número
quadrado = lambda x: x**2

a = int(input("Digite o valor que deseja saber o quadrado dele: "))
# usando a função lambda
resultado = quadrado(a)
print(f"Quadrado de {a}:", resultado)

# Lista de notas dos estudantes
notas = [7.5, 2.0, 6.5, 9.0, 7.0]

# Função regular para calcular a média
def calcular_media(notas):
    total = sum(notas)
    media = total / len(notas)
    return media

# Função lambda para arredondar a média para duas casas decimais
arredondar_media = lambda media: round(media, 2)

# Calcular a média
media = calcular_media(notas)
media_arredondada = arredondar_media(media)

# Verificar se os estudantes foram aprovados
situacao = "Aprovado" if media_arredondada >= 7 else "Reprovado"

# Resultados
print(f"Média do aluno: {media_arredondada}")
print(f"O aluno está: {situacao}")

"""**DESAFIO**

"""

valor_da_compra = float(input("Digite o valor da compra: "))
desconto = float(input("Digite o valor do desconto "))

def validar_desconto(desconto):
  if desconto < 1 or desconto > 99:
    print("Desconto inválido")
    return valor_da_compra
  else:
    return aplicar_desconto(desconto)

def aplicar_desconto(desconto):
  total_com_desconto = valor_da_compra - (valor_da_compra * (desconto/100))
  return total_com_desconto

total_com_desconto = validar_desconto(desconto)
print(f"Valor com desconto: {total_com_desconto}")