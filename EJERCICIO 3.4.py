AFD = {
    frozenset([0]): {'a': frozenset([0, 1]), 'b': frozenset([0, 1])},
    frozenset([0,1]): {'a': frozenset([0, 1, 2]), 'b': frozenset([0, 1, 2])},
    frozenset([0,1,2]): {'a': frozenset([0, 1, 2]), 'b': frozenset([0, 1, 2])}
}

estado_finales = [frozenset([0,1,2])]

def procesar_afd(palabra):
    estado_actual = frozenset([0])
    
    for simbolo in palabra:
        if simbolo in AFD.get(estado_actual, {}):
            estado_actual = AFD[estado_actual][simbolo]
        else:
            return False
    
    return estado_actual in estado_finales

# Ejemplo
print(procesar_afd("ab"))  # True
print(procesar_afd("aab")) # True
print(procesar_afd(""))    # False (en este AFD no acepta vacío, deberíamos ajustarlo si queremos)
print(procesar_afd("c"))   # False
