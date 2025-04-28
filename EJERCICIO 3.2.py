AFN = {
    0: {'a': [0, 1], 'b': [0, 1], '': [1]},
    1: {'a': [2], 'b': [2], '': [2]},
    2: {} 
}


def procesar_afn(palabra, estado_actuales=[0]):
    if not palabra:
       
        estados_a_explorar = set(estado_actuales)
        while estados_a_explorar:
            estado = estados_a_explorar.pop()
            if estado == 2:
                return True
            if '' in AFN[estado]:
                estados_a_explorar.update(AFN[estado][''])
        return False
    
    simbolo = palabra[0]
    siguiente = palabra[1:]
    nuevos_estados = set()

    for estado in estado_actuales:
        if simbolo in AFN[estado]:
            nuevos_estados.update(AFN[estado][simbolo])
        if '' in AFN[estado]:  
            nuevos_estados.update(AFN[estado][''])
    
    if not nuevos_estados:
        return False
    
    return procesar_afn(siguiente, list(nuevos_estados))


print(procesar_afn("ab"))  # True
print(procesar_afn("aab")) # True
print(procesar_afn(""))    # True
print(procesar_afn("c"))   # False
