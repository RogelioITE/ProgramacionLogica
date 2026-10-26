# Ontología de Clasificación Animal y Deducción Lógica

**Materia:** Programación Lógica (7SE)  
**Docente:** María de Lourdes Aguillón Ruiz  
**Institución:** Instituto Tecnológico de Ensenada  

---

## 1. Definición de Predicados

La representación formal del conocimiento se basa en la siguiente sintaxis lógica:

* $M(x)$: $x$ es un mamífero
* $T(x, y)$: $x$ tiene el atributo o rasgo $y$
* $A(x, y)$: $x$ se alimenta de $y$
* $Acc(x, y)$: $x$ realiza la acción $y$
* $E(x, y)$: $x$ posee el patrón o color $y$
* $C(x, y)$: $x$ pertenece a la clase o especie $y$

---

## 2. Grafo de la Ontología Taxonómica

Diagrama en Mermaid de la jerarquía taxonómica y vínculos de confusión entre especies:

```mermaid
graph TD
    %% Clases Generales
    Mamifero["Mamífero M(x)"]
    Ave["Ave C(x, ave)"]
    Pez["Pez C(x, pez)"]

    %% Subclases
    Carnivoro["Carnívoro C(x, carnívoro)"]
    Ungulado["Ungulado C(x, ungulado)"]

    %% Especies Terrestres
    Guepardo["Guepardo C(x, guepardo)"]
    Tigre["Tigre C(x, tigre)"]
    Jirafa["Jirafa C(x, jirafa)"]
    Cebra["Cebra C(x, cebra)"]

    %% Especies Marinas
    Delfin["Delfín C(x, delfín)"]
    Narval["Narval C(x, narval)"]
    Beluga["Beluga C(x, beluga)"]
    Morsa["Morsa C(x, morsa)"]
    Tiburon["Tiburón C(x, tiburón)"]
    Pinguino["Pingüino C(x, pingüino)"]
    Albatros["Albatros C(x, albatros)"]

    %% Relaciones Taxonómicas (Es Un)
    Mamifero --> Carnivoro
    Mamifero --> Ungulado
    Mamifero --> Delfin
    Mamifero --> Narval
    Mamifero --> Beluga
    Mamifero --> Morsa

    Carnivoro --> Guepardo
    Carnivoro --> Tigre

    Ungulado --> Jirafa
    Ungulado --> Cebra

    Ave --> Pinguino
    Ave --> Albatros

    Pez --> Tiburon

    %% Relaciones de Confusión
    Delfin -.-|Se confunde con| Tiburon
    Narval -.-|Se confunde con| Beluga
    Narval -.-|Se confunde con| Morsa
```

---

## 3. Grafo de Deducción Lógica y Reglas

Flujo de reglas ($R_1$ a $R_{18}$) utilizadas para deducir la clase o especie a partir de los atributos observados:

```mermaid
graph LR
    subgraph Atributos Observados
        A1["T(x, pelo)"]
        A2["Acc(x, dar leche)"]
        A3["Acc(x, respirar pulmones)"]
        A4["T(x, plumas)"]
        A5["T(x, espiráculo)"]
        A6["T(x, colmillo helicoidal)"]
        A7["E(x, totalmente blanco)"]
        A8["T(x, branquias)"]
    end

    subgraph Deducciones Intermedias
        R1_12_15{"R1, R12, R15"}
        R2_3{"R2, R3"}
        M_Node["M(x) - Mamífero"]
        Ave_Node["C(x, ave)"]
    end

    subgraph Deducción Final
        Delfin_Node["C(x, delfín) [R13]"]
        Narval_Node["C(x, narval) [R16]"]
        Beluga_Node["C(x, beluga) [R17]"]
        Tiburon_Node["C(x, tiburón) [R14]"]
    end

    A1 & A2 --> R1_12_15
    A2 & A3 --> R1_12_15
    R1_12_15 --> M_Node

    A4 --> R2_3
    R2_3 --> Ave_Node

    M_Node & A5 --> Delfin_Node
    M_Node & A6 --> Narval_Node
    M_Node & A7 --> Beluga_Node
    A8 --> Tiburon_Node
```

---

## 4. Matriz de Hechos y Diferenciadores Específicos

| Animal | Hechos Base Observados | Deducción por Regla | Especie con la que se Confunde | Rasgo Diferenciador Clave |
| :--- | :--- | :--- | :--- | :--- |
| **Delfín** | Amamanta, respiración pulmonar, espiráculo, aleta caudal horizontal | $M(x)$ (R12), $C(x, \text{delfín})$ (R13) | Tiburón | Espiráculo y aleta horizontal (no vertical) |
| **Tiburón** | Pez, branquias, aleta caudal vertical | $C(x, \text{pez})$, $C(x, \text{tiburón})$ (R14) | Delfín | Branquias y aleta caudal vertical |
| **Narval** | Amamanta, sangre caliente, pulmones, colmillo helicoidal | $M(x)$ (R12), $C(x, \text{narval})$ (R16) | Beluga / Morsa | Gran colmillo largo en forma de espiral |
| **Beluga** | Amamanta, sangre caliente, pulmones, totalmente blanco | $M(x)$ (R12), $C(x, \text{beluga})$ (R17) | Narval | Coloración blanca y ausencia de colmillo |
| **Morsa** | Amamanta, sangre caliente, pulmones, dos colmillos hacia abajo, sale a tierra | $M(x)$ (R12), $C(x, \text{morsa})$ (R18) | Narval | Dos colmillos apuntando hacia abajo y desplazamiento en tierra |
