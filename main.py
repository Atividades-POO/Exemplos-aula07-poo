#
# Autores:
# Michel Silva
# Emanuel Frank
# Carlos Eduardo
# data: 07/07/2022
#
# Crie função de tratamento para entradas “int”.
# Crie função de tratamento para entradas “float”.
# Crie função de tratamento para entradas “string”.
# Crie função de tratamento para entradas “list”.
# Crie função de tratamento para entradas “tuple”.
# Crie função de tratamento para entradas “dict”.
# Crie função de tratamento para entradas “set”.
# Escreva uma função para tratar o erro ZeroDivisionError

# Escreva uma função para tratar o erro TypeError
# Escreva uma função para tratar o erro IndexError
# Escreva uma função para tratar o erro KeyError
# Escreva uma função para tratar o erro ValueError
# Escreva uma função para tratar o erro AttributeError
# Escreva uma função para tratar o erro SyntaxError
# Escreva uma função para tratar o erro ImportError

# função para tratar entradas int
def tratamento_int(entrada):
    try:
        return int(entrada)
    except ValueError as e:
        return "Valor inteiro inválido"

# função para tratar entradas float

