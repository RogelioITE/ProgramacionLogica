"""
Práctica de Diccionarios y Tuplas - Programación Lógica

Estructuras utilizadas:
- Hecho: Tupla (Predicado, Valor) o (Predicado, True)
- Regla: Tupla (Condiciones, Conclusión) dentro del diccionario REGLAS
- Jerarquías y Confundibles: Tuplas de pares (Entidad, Relacionado)
"""

# Definición del hecho base de mamífero: M(x)
M = ("M", True)

# Definición de acción recurrente para mamíferos marinos
VIVIR_EN_AGUA = ("Acc", "vivir en el agua")

# Reglas del sistema experto (Regla N -> ([Condiciones], Conclusión))
REGLAS = {
    1: ([("T", "pelo"), ("Acc", "dar leche")], M),
    2: ([("T", "plumas")], ("C", "ave")),
    3: ([("Acc", "volar"), ("Acc", "poner huevos")], ("C", "ave")),
    4: ([M, ("A", "carne")], ("C", "carnívoro")),
    5: ([M, ("T", "pezuñas")], ("C", "ungulado")),
    6: ([("C", "carnívoro"), ("E", "manchas oscuras"), ("E", "leonado")], ("C", "guepardo")),
    7: ([("C", "carnívoro"), ("E", "rayas negras")], ("C", "tigre")),
    8: ([("C", "ungulado"), ("T", "cuello largo"), ("E", "manchas oscuras")], ("C", "jirafa")),
    9: ([("C", "ungulado"), ("E", "rayas negras")], ("C", "cebra")),
    10: ([("C", "ave"), ("Acc", "nadar"), ("E", "blanco y negro")], ("C", "pingüino")),
    11: ([("C", "ave"), ("Acc", "volar muy bien")], ("C", "albatros")),
    12: ([("Acc", "dar leche"), ("Acc", "respirar por pulmones")], M),
    13: ([M, VIVIR_EN_AGUA, ("T", "espiráculo"), ("T", "aleta dorsal"), ("T", "aleta caudal horizontal")], ("C", "delfín")),
    14: ([("C", "pez"), ("T", "branquias"), ("T", "aleta caudal vertical")], ("C", "tiburón")),
    15: ([("Acc", "dar leche"), ("T", "sangre caliente"), ("Acc", "respirar por pulmones")], M),
    16: ([M, VIVIR_EN_AGUA, ("T", "colmillo largo helicoidal")], ("C", "narval")),
    17: ([M, VIVIR_EN_AGUA, ("E", "totalmente blanco"), ("NO", "T", "colmillo largo helicoidal")], ("C", "beluga")),
    18: ([M, VIVIR_EN_AGUA, ("T", "dos colmillos hacia abajo"), ("Acc", "salir a tierra")], ("C", "morsa")),
}

# Base de hechos iniciales observados por animal
ANIMALES = {
    "delfín": [
        ("Acc", "dar leche"),
        ("Acc", "respirar por pulmones"),
        VIVIR_EN_AGUA,
        ("T", "espiráculo"),
        ("T", "aleta dorsal"),
        ("T", "aleta caudal horizontal")
    ],
    "tiburón": [
        ("C", "pez"),
        VIVIR_EN_AGUA,
        ("T", "branquias"),
        ("T", "aleta caudal vertical")
    ],
    "narval": [
        ("Acc", "dar leche"),
        ("T", "sangre caliente"),
        ("Acc", "respirar por pulmones"),
        VIVIR_EN_AGUA,
        ("T", "colmillo largo helicoidal")
    ],
    "beluga": [
        ("Acc", "dar leche"),
        ("T", "sangre caliente"),
        ("Acc", "respirar por pulmones"),
        VIVIR_EN_AGUA,
        ("E", "totalmente blanco")
    ],
    "morsa": [
        ("Acc", "dar leche"),
        ("T", "sangre caliente"),
        ("Acc", "respirar por pulmones"),
        VIVIR_EN_AGUA,
        ("T", "dos colmillos hacia abajo"),
        ("Acc", "salir a tierra")
    ],
    "tigre": [
        ("T", "pelo"),
        ("Acc", "dar leche"),
        ("A", "carne"),
        ("E", "rayas negras")
    ],
    "jirafa": [
        ("T", "pelo"),
        ("Acc", "dar leche"),
        ("T", "pezuñas"),
        ("T", "cuello largo"),
        ("E", "manchas oscuras")
    ],
    "pingüino": [
        ("T", "plumas"),
        ("Acc", "nadar"),
        ("E", "blanco y negro")
    ]
}

# Relaciones taxonómicas y de confusión
JERARQUIA = (
    ("delfín", "mamífero"),
    ("narval", "mamífero"),
    ("beluga", "mamífero"),
    ("morsa", "mamífero"),
    ("tigre", "carnívoro"),
    ("jirafa", "ungulado"),
    ("pingüino", "ave"),
    ("tiburón", "pez")
)

CONFUNDIBLES = (
    ("delfín", "tiburón"),
    ("narval", "beluga"),
    ("narval", "morsa")
)


def inferir(hechos_iniciales):
    # Aplica las reglas una y otra vez hasta que ya no salgan hechos nuevos
    
    hechos = set(hechos_iniciales)
    usadas = []
    cambio = True

    while cambio:
        cambio = False
        for num, (condiciones, conclusion) in REGLAS.items():
            if num in usadas:
                continue

            cumplida = True
            for c in condiciones:
                if c[0] == "NO":
                    hecho_negado = c[1:]
                    if hecho_negado in hechos:
                        cumplida = False
                        break
                else:
                    if c not in hechos:
                        cumplida = False
                        break

            if cumplida and conclusion not in hechos:
                hechos.add(conclusion)
                usadas.append(num)
                cambio = True

    return hechos, usadas


if __name__ == "__main__":
    print("=" * 65)
    print(" INFERENCIA DE CLASES Y ESPECIES MEDIANTE LÓGICA DE PREDICADOS")
    print("=" * 65)

    for animal, hechos_obs in ANIMALES.items():
        hechos_inferidos, reglas_aplicadas = inferir(hechos_obs)
        clases = sorted([valor for predicado, valor in hechos_inferidos if predicado == "C"])
        es_mamifero = M in hechos_inferidos

        print(f"\nAnimal: {animal.upper()}")
        print(f"  • Es Mamífero: {es_mamifero}")
        print(f"  • Clases/Especies deducidas: {clases}")
        print(f"  • Reglas activadas: {reglas_aplicadas}")

    print("\n" + "=" * 65)
    print(" VÍNCULOS Y RELACIONES ONTOLÓGICAS")
    print("=" * 65)
    print("\nJerarquía Taxonómica:")
    for hijo, padre in JERARQUIA:
        print(f"  - {hijo} ──(es un)──> {padre}")

    print("\nEspecies Confundibles:")
    for a, b in CONFUNDIBLES:
        print(f"  - {a} <──(se confunde con)──> {b}")