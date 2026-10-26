# Ontología de Clasificación Animal y Deducción Lógica

**Integrantes:**
- David Vázquez Torres
- Rogelio Vázquez Razón

**Materia:** Programación Lógica (7SE)  
**Institución:** Instituto Tecnológico de Ensenada

---

## 1. Definición de Predicados

La representación del conocimiento utiliza la siguiente sintaxis formal:

* $M(x)$: $x$ es un mamífero
* $T(x, y)$: $x$ tiene el atributo o rasgo $y$
* $A(x, y)$: $x$ se alimenta de $y$
* $Acc(x, y)$: $x$ realiza la acción $y$
* $E(x, y)$: $x$ posee el patrón o color $y$
* $C(x, y)$: $x$ pertenece a la clase o especie $y$

---

## 2. Grafo de la Ontología Taxonómica

Diagrama en Mermaid de la jerarquía taxonómica y vínculos de confusión entre especies estudiadas.

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