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


# Escreva uma função para tratar o erro IndexError

# Escreva uma função para tratar o erro ValueError
# Escreva uma função para tratar o erro AttributeError

# Escreva uma função para tratar o erro ImportError

# função para tratar entradas int
def tratamento_int(entrada):
    try:
        return int(entrada)
    except ValueError as e:
        return f'Error: {e}, {type(e)=}'

# função para tratar entradas float
def tratamento_float(entrada):
    try:
        return float(entrada)
    except ValueError as e:
        return f'Error: {e}, {type(e)=}'

# função para tratar entradas string
def tratamento_string(entrada):
    try:
        return str(entrada)
    except ValueError as e:
        return f'Error: {e}, {type(e)=}'

# função para tratar entradas list
def tratamento_list(entrada):
    try:
        return list(entrada)
    except ValueError as e:
        return f'Error: {e}, {type(e)=}'

# função para tratar entradas tuple
def tratamento_tuple(entrada):
    try:
        return tuple(entrada)
    except ValueError as e:
        return f'Error: {e}, {type(e)=}'

# função para tratar entradas dict
def tratamento_dict(entrada, chave=None):
    try:
        return dict(entrada)
    except ValueError as e:
        return f'Error: {e}, {type(e)=}'

# função para tratar entradas set
def tratamento_set(entrada):
    try:
        return set(entrada)
    except ValueError as e:
        return f'Error: {e}, {type(e)=}'

# função para tratar erro ZeroDivisionError
def tratamento_ZeroDivisionError(entrada):
    try:
        saida = 1 / int(entrada)
        return f'resultado da divisão: {saida}'
    except ZeroDivisionError as e:
        return f'Error: {e}, {type(e)=}'
    except ValueError as e:
        return f'Error: {e}, {type(e)=}'
    else:
        return f'Não houve erro ded erro ZeroDivisionError'



# função para tratar erro IndexError
def tratamento_IndexError(entrada):
    try:
        return entrada[10]
    except IndexError as e:
        return f'Error: {e}, {type(e)=}'



# função para tratar erro ValueError
def tratamento_ValueError(entrada):
    try:
        return int(entrada)
    except ValueError as e:
        return f'Error: {e}, {type(e)=}'

# função para tratar erro AttributeError
def tratamento_AttributeError(entrada):
    try:
        return entrada.a
    except AttributeError as e:
        return f'Error: {e}, {type(e)=}'



# função para tratar erro ImportError
def tratamento_ImportError(entrada):
    try:
        return __import__(entrada)
    except ImportError as e:
        return f'Error: {e}, {type(e)=}'

