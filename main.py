#
#
import ex01

valor = input("Digite um valor: ")

print(ex01.tratamento_int(valor))
print(ex01.tratamento_float(valor))
print(ex01.tratamento_string(valor))
print(ex01.tratamento_list(valor))
print(ex01.tratamento_tuple(valor))
print(ex01.tratamento_dict(valor))
print(ex01.tratamento_set(valor))
print(ex01.tratamento_ZeroDivisionError(valor))

print(ex01.tratamento_IndexError(valor))

print(ex01.tratamento_ValueError(valor))
print(ex01.tratamento_AttributeError(valor))

print(ex01.tratamento_ImportError(valor))


