.. 1NSI

.. toctree::
   :maxdepth: 1
   
Numération en informatique
==========================

Un ordinateur ne manipule que des données écrites en binaire. Pour les humains, la lecture de données binaires est difficile et n'est pas historiquement l'écriture utilisée. Pour rendre lisible les données binaires, on les convertit dans notre système décimal en passant par le système d'écriture hexadécimal qui facilite la conversion et la lecture. Commençons par définir les trois numérations **décimale**, **binaire** et **hexadécimale**.

Numération décimale
-------------------

L'écriture décimale, **en base** 10, d'un nombre entier est de la forme: 
:math:`a_{n} \times 10^{n}+ \ldots + a_{2} \times 10^{2} + a_{1} \times 10^{1} + a_{0} \times 10^{0}`

On rappelle que : :math:`10^{1}=10` et :math:`10^{0}=1`.

La numération décimale utilise les 10 chiffres : 0, 1, 2, 3, 4, 5, 6, 7, 8 et 9.

.. admonition:: Exemple

    Comment se décompose le nombre entier 206 ?

    .. math::
    
        \begin{align*}
        206 &= 2 \times 100 + 0 \times 10 + 6 \times 1\\
        \phantom{1204} &= 2 \times 10^{2} + 0 \times 10^{1} + 6 \times 10^{0}
        \end{align*}

    On peut représenter cette écriture dans un tableau :

    .. table:: Numération décimale
        :align: center
        
        ============== ============== ============== ==============
        :math:`10^{3}` :math:`10^{2}` :math:`10^{1}` :math:`10^{0}`
        ============== ============== ============== ==============
        0              2              0              6
        ============== ============== ============== ==============

Numération binaire
------------------

La numération binaire utilise seulement les chiffres 0 et 1. Dans cette base, un nombre binaire se décompose avec des puissances de 2. Chaque chiffre 0 et 1 est appelé un **bit** de l'anglais **Binary digit**.

.. On appelle **mot binaire** une valeur composée de plusieurs bits.

Le bit situé à **gauche** correspond à la plus grande puissance de 2. C'est le **bit de poids fort**.

Le bit situé à **droite** correspond à la plus petite puissance de 2. C'est le **bit de poids faible**.

On rencontre souvent des mots de 8 bits : ils forment un **octet**.

.. admonition:: Exemple

   Comment se décompose le nombre entier 206 en binaire ?

   .. math::
    
      \begin{align*}
      206 &= 1 \times 128 + 1 \times 64 + 1 \times 8 + 1 \times 4 + 1 \times 2 \\
      \phantom{206} &= 1 \times 2^{7} + 1 \times 2^{6} + 1 \times 2^{3} + 1 \times 2^{2} + 1 \times 2^{1}
      \end{align*}

   On peut représenter cette écriture dans un tableau :

   .. table:: Numération décimale
      :widths: auto
      :align: center
        
      ============= ============= ============= ============= ============= ============= ============= =============
      :math:`2^{7}` :math:`2^{6}` :math:`2^{5}` :math:`2^{4}` :math:`2^{3}` :math:`2^{2}` :math:`2^{1}` :math:`2^{0}`
      ============= ============= ============= ============= ============= ============= ============= =============
      1              1            0              0            1             1             1             0
      ============= ============= ============= ============= ============= ============= ============= =============
        
   Le nombre en écriture décimale :math:`206_{10}` s'écrit en binaire :math:`11001110_{2}`.

.. note::

    1. Il existe des *mots binaires* de 16, 32 ou 64 bits.
    2. La mémoire et les unités de stockage sont exprimées en octets. Aujourd'hui les volumes sont de l'ordre du tera-octet : :math:`10^{12}` octets !

Numération hexadécimale
-----------------------

La numération **hexadécimale** est une numération en **base** 16. Cette numération utilise donc 16 chiffres :

- Les 10 chiffres de la numération décimale de 0 à 9;
- et les 6 premières lettres de l'alphabet : A, B, C, D, E et F.

En notation décimale : A=10, B=11, C=12, D=13, E=14 et F=15.

En notation binaire sur 4 bits : A=1010, B=1011, C=1100, D=1101, E=1110 et F=1111.

.. admonition:: Exemple

   On a vu l'écriture du nombre 206 en notation décimale et binaire. 

   En notation hexadécimale :
    
   .. math::
    
      \begin{align*}
      206_{10} &= 12 \times 16^{1} + 14 \times 16^{0}\\
      206_{10} &= CE_{16}
      \end{align*}
        
   On rappelle que la lettre C représente le nombre 12 et la lettre E représente le nombre 14.
