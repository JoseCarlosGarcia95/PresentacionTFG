# Trabajo fin de grado 2019 - José Carlos García

(HABLAR DE USTED)

Esta presentación, no está hecha en beamer como es habitual, aunque utilizo LaTeX por debajo,  con motivo de innovar en el tema de la presentación.

Antes de empezar la presentación como tal, me gustaría invitaros si os viene bien, a acceder a la siguiente URL: [TAL], al acceder a la URL, podréis ver la presentación directamente en vuestros móviles u ordenadores, además de poder interactuar con los elementos de la presentación (Para completar la información de la presentación)

## Introducción

Estamos en un momento fascinante de la historia, donde los avances tecnológicos nos han guiado a un presente donde no podemos vivir sin tecnología.

_La bomba_ la máquina desarrollada durante la segunda guerra mundial para romper la máquina Enigma, apenas podía hacer 15 operaciones por segundo. A día de hoy, mi ordenador personal es capaz de hacer aproximadamente mil billones de operaciones por segundo. Este hecho, nos permite plantearnos modelos matemáticos más complejos y más afines a la realidad.

Ahora, podemos tener en cuenta modelos más afines con la realidad, teniendo en cuenta la incertidumbre, los errores de medida y casos extremos como los que se pueden observar en los fluidos de la punta de un avión.

En este trabajo se va a presentar el marco teórico necesario para definir y resolver ecuaciones diferenciales difusas, así como la exploración de métodos numéricos y técnicas computacionales con el objetivo de desarrollar técnicas más eficientes, ecológicas y económicas.

Para buscar estas técnicas se van a comparar los resultados, en términos de rendimiento y uso de energía de estos algoritmos.

Antes de comenzar la exposición del tema en cuestión, quiero hacer mención a una cita de Lofti Zadeh, que introdujo la teória difusa en 1965, e introdujo el principio donde se sustentan los principales resultados de esta exposición.

> A medida que aumenta la complejidad, las declaraciones precisas pierden significado y las declaraciones significativas pierden precisión

## ¿Qué es la lógica difusa?

### Función de pertenencia clásica

La construcción de la teoría difusa de conjuntos se basa principalmente en la función de pertenencia en los conjuntos clásicos.

Cuando se introdujo la teoría difusa se tomó la idea de función de pertenencia, y se empezóa trabajar con todos los valores entre [0, 1] y no sólo los valores 0 y 1.

### Ejemplos

Todo esto se puede ver de manera intuitiva mediante varios ejemplos:

- Si queremos construir un conjunto de personas altas clásico, se nos queda un poco cojo debido a que tendríamos que definir un límite inferior, por ejemplo 180cm, pero estaríamos dejando fuera del conjunto de personas altas a aquellas que miden 179cm. La teoría difusa de conjunto nos permite definir como de alta es una persona entre el [0, 1] y de esta manera, que una persona que mida 180cm sea alta, y una persona que mida 179cm sea 90% alta.
- Por otro lado, cuando hay un terremoto, los efectos del mismo se suelen tratar con terminología del tipo: muy devastador, devastador, ... Toda esta vagueza del lenguaje se puede representar mediante el uso de conjuntos difusos.
- Finalmente, los instrumentos de medidas por muy precisos que sean, siempre van a tener errores de medidas. Estos errores de medidas podemos representarlos como "números difusos" que cubren todos los valores posibles.

## Conjuntos difusos

### α-corte

Los α-corte de un conjunto difuso nos permite dividir los conjuntos difusos, en distintos conjuntos clásicos dependientes de un parámetro α

VER DEMO

### Número difuso

Si tenemos que un conjunto difuso cumple que el 1-corte es no vacío, y que la función de pertenencia es cuasicóncova.

Para R, podemos decir que la función de pertenencia es cuasicónvoca si todos los α-corte son intervalos cerrados.

VER DEMO

### Principio de extensión de Zadeh

Estaría bien además que fuese posible calcular la imagen mediante una función clásica entre dos conjuntos, aquí entr en juego el principio de extensión de Zadeh.

VER DIAPOSITIVA

Además, si la función es inyectiva el principio de extensión de Zadeh se simplica aún más.

### Teoremas de continuidad

Ahora vamos a ver algunos resultados que nos muestran que el principio de Zadeh funciona bien y de una forma interesante bajo unas ciertas condiciones:

VER DIAPOSITIVA

### Aritmética difusa

La definición clásica de derivada implica un límite, una resta y un cociente. Parece lógico plantearse estas operaciones para números difusos buscando una definición de derivada difusa.

Por ello, debido a la equivalencia entre trabajar con conjuntos difusos y sus α-corte, podemos definir operaciones aritméticas de una forma intuitiva:

VER DIAPOSITIVA

### Problemas al definir estas operaciones aritméticas

TODO: EXPLICAR DIAPOSITIVA

### Otras definiciones de diferencia

Dado que necesitamos una definición de derivada, que al menos nos asegure que una derivada constante existe,la más intuitiva es forzar que en nuestra definición esté resuelto de forma implícita nuestro problema.

De la misma forma, teniendo en cuenta otras propiedades que se cumplen en la resta de números reales, podemos definir teniendo en cuenta la idea de diferencia de Hukuhara, un concepto más general.

Todas estas definiciones de diferencia, nos darán distintas definiciones de derivadas, que pasamos a explorar ahora.

(INDICAR DONDE VER MÁS EN EL TRABAJO)

## Ecuaciones diferenciales difusas

### Derivada según Hukuhara

Teniendo en cuenta la definición de derivada clásica y la diferencia de Hukuhara podemos hacer la primera definición de derivada difusa.

Mostrar ejemplos.

### ¿Podemos construir funciones diferenciables de Hukuhara?

A continuación, vamos a mostrar un resultado que nos permitirá construir funciones H-Diferenciables mediante funciones reales diferenciables.

Este resultado básicamente nos dice, que bajo ciertas condiciones podemos afirmar que ña derivada del producto de un número difuso por una función real, es el número difuso multiplicado por la derivada de la función real.

### Otras propiedades

A continuación, vamos a ver un resultado parecido al que tenemos en el cálculo clásico de álgebra de derivadas.

Cabe mencionar también, que dentro del ámbito del cálculo difuso también existe un resultado que relaciona las funciones diferenciables y las funciones continuas, como en el cálculo clásico. Este resultado se puede encontrar dentro del trabajo de fin de grado.

### Derivada de Hukuhara generalizada

Aunque la deirvada de Hukuhara parece funcionar bien, seguimos teniendo algunos problemas en funciones relativamente sencillas como las funciones lineales, la derivada de Hukuhara generalizada viene a solucionar este problema.

La derivada de Hukuhara generalizada generaliza el concepto de derivada teniendo en cuenta, los valores de $h$ cuando se acerca por la derecha, o por la izquierda.

Si nos fijamos en la primera propiedad, no es más que la misma propiedad que debe cumplir para ser derivable según Hukuhara.

### Otras definiciones de derivadas

También podemos encontrar el concepto de Derivada de Hukuhara generalizada, en este caso teniendo en cuenta la diferencia generalizada de Hukuhara, y dos casos más que podemos encontrar directamente dentro del trabajo de fin de grado.

### Algunas nociones sobre integrales

Una vez definidas las derivadas difusas, vamos a explorar de manera somera las integrales difusas.

Las definiciones que se aplican aquí son semejantes a las definiciones utilizadas en el cálculo clásico, además, los resultados de teoremas clásicos del cálculo, lo vemos aquí.

Tenemos álgebra de integrales, equivalencia entre integrales de $\alpha$-corte y el Teorema fundamental del cálculo.

### Ecuaciones diferenciales difusas

Una vez introducidos estos conceptos, podemos pasar a definir el concepto de ecuación diferencial difusa.

La definición de ecuación diferencial difusa, nace manera natural, cambiando en la definición clásica los elementos por elementos difusos.

### Teorema de equivalencia

A continuación, se presenta uno de los teoremas más importanets de este trabajo. Este teorema es el preludio de todos los métodos numéricos que se van a desarrollar a continuación, y no es casualidad que el título de esta diapositiva se marque con un color llamativo.

Este teorema nos permite afirmar bajo unas condiciones de regularidad, la equivalencia que existe entre resolver una ecuación diferencial difusa y su versión clásica.

## Computación científica de alto rendimiento

Este capítulo tiene el objetivo de exprimir al máximo los recursos que tenemos disponibles.

Además, vasmos a hacer un especial hincapie especial en el consumo energético de los algoritmos y de las técnicas computacionales para tratar de reducir el impacto medio ambiental y obtener los resultados en el menor tiempo posible.
