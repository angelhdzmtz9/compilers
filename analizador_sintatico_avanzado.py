def es_valida(expr):
    operadores_matematicos = set("+-*/")
    par_abiertos = 0
    ultima = ""
    i = 0

    while i < len(expr):
        c = expr[i]

        if c == " ":
            i += 1
            continue
        elif c.isdigit():
            ultima = "num"
        elif c == "(":
            par_abiertos += 1
            ultima = "par_abre"
        elif c == ")":
            par_abiertos -= 1
            if par_abiertos < 0:
                return False
            if ultima in ["op", "par_abre"]:
                return False
            ultima = "par_cierra"
        elif c in operadores_matematicos:
            if ultima != "num" and ultima != "par_cierra":
                return False
            ultima = "op"
        elif expr[i:i+3] == "AND":
            if ultima != "num" and ultima != "par_cierra":
                return False
            ultima = "op"
            i += 3
            continue
        elif expr[i:i+2] == "OR":
            if ultima != "num" and ultima != "par_cierra":
                return False
            ultima = "op"
            i += 2
            continue
        elif expr[i:i+3] == "NOT":
            if ultima != "num" and ultima != "par_cierra" and ultima != "":
                return False
            ultima = "op"
            i += 3
            continue
        else:
            return False  # Caracter inválido

        i += 1

    if par_abiertos != 0:
        return False
    if ultima in ["op", "par_abre"]:
        return False
    return True

# Entrada del usuario
print("Introduce expresiones para validar. Escribe 'salir' para terminar.")
while True:
    expr = input(">> ")
    if expr.lower() == "salir":
        break
    if es_valida(expr):
        print(" Expresión válida\n")
    else:
        print(" Expresión inválida\n")
