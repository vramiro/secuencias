Desafio del mes: alineamiento de secuencias geneticas
========

Una solución de fuerza bruta para el desafio del mes de http://www.programando.org
Más info del desafío en http://www.programando.org/blog/2013/03/desafio-marzo-slash-abril-adn-forense/

Ejemplos de ejecución

<pre>
$ python main.py datos.txt
El culpable es el sospechoso numero 3 (AGTGATA).
</pre>

con debug

<pre>
python main.py input.txt 1
AGTGATG/A-AATGC -> -6
AGTGATG/AAATG-C -> -6
AGTGATG/-AAATGC -> -14
AGTGATG/AAATGC- -> -6
AGTGATG/AAA-TGC -> -6
AGTGATG/AAAT-GC -> -8
AGTGATG/AA-ATGC -> -6
('AGTGATG', 'AAATGC', -6)
AGTGATG/--AGGAA -> -6
AGTGATG/-AG-GAA -> -14
AGTGATG/A-GGAA- -> 8
AGTGATG/A-GG-AA -> 0
AGTGATG/-AGGA-A -> 0
AGTGATG/AGGA--A -> 0
AGTGATG/AGG-A-A -> 8
AGTGATG/-AGGAA- -> 0
AGTGATG/AG--GAA -> 2
AGTGATG/AGGA-A- -> 0
AGTGATG/A--GGAA -> 2
AGTGATG/A-G-GAA -> -6
AGTGATG/AG-G-AA -> 8
AGTGATG/A-GGA-A -> 8
AGTGATG/-AGG-AA -> -8
AGTGATG/AG-GAA- -> 16
AGTGATG/AG-GA-A -> 16
AGTGATG/-A-GGAA -> -6
AGTGATG/AGG-AA- -> 8
AGTGATG/AGGAA-- -> 8
AGTGATG/AGG--AA -> 0
('AGTGATG', 'AGGAA', 16)
AGTGATG/AGTGATA -> 28
('AGTGATG', 'AGTGATA', 28)
AGTGATG/GATTACA -> 0
('AGTGATG', 'GATTACA', 0)
El culpable es el sospechoso numero 3 (AGTGATA)
</pre>
