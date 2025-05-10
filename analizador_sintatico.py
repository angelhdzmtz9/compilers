def es_valida(expr):
    operadores = set("+-*/")
    par_abiertos = 0
    ultima = ""

    for c in expr:
        if c == " ":
            continue
        elif c.isdigit():
            ultima = "num"
        elif c in operadores:
            if ultima != "num" and ultima != "par_cierra":
                return False
            ultima = "op"
        elif c == "(":
            par_abiertos += 1
            ultima = "par_abre"
        elif c == ")":
            par_abiertos -= 1
            if par_abiertos < 0:
                return False
            if ultima == "op" or ultima == "par_abre":
                return False
            ultima = "par_cierra"
        else:
            return False  # carácter inválido

    if par_abiertos != 0:
        return False
    if ultima in ["op", "par_abre"]:
        return False
    return True

#  Ciclo para ingresar expresiones manualmente desde la terminal
while True:
    entrada = input("Ingresa una expresión (o escribe 'salir' para terminar): ")
    
    if entrada.lower() == 'salir':
        print("Saliendo...")
        break
    
    if es_valida(entrada):
        print(" Expresión válida")
    else:
        print(" Expresión inválida")