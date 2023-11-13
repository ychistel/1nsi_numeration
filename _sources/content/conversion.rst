Convertir des nombres entiers
=============================

Écriture binaire à écriture décimale
--------------------------------------

La conversion d'un nombre binaire en écriture décimale se fait en associant à chaque chiffre de l'écriture binaire la puissance de 2 qui correspond à sa position.

Le tableau ci-dessous redonne les 8 premières puissances de 2, soit pour 1 octet :

.. table:: Puissances de 2
   :widths: auto
   :align: center
      
   ============= ============= ============= ============= ============= ============= ============= =============
   :math:`2^{7}` :math:`2^{6}` :math:`2^{5}` :math:`2^{4}` :math:`2^{3}` :math:`2^{2}` :math:`2^{1}` :math:`2^{0}`
   ============= ============= ============= ============= ============= ============= ============= =============
   128           64            32            16            8             4             2             1
   ============= ============= ============= ============= ============= ============= ============= =============   

.. admonition:: Exemple

   Le nombre binaire 1101 est associée aux puissances de 2 d'exposant 0, 2 et 3 (de gauche à droite). 

   .. math::

      1101_{2}=2^{3}+2^{2}+2^{0}=8+4+1=13_{10}

   Donc le nombre binaire 1101 s'écrit 13 en décimal.

Écriture décimale à écriture binaire
--------------------------------------

La conversion d'un nombre entier décimal en écriture binaire se fait en décomposant ce nombre en une somme de puissance de 2, en commençant par la plus grande puissance possible.

Voici un algorithme présentant la méthode:

.. code-block:: text

   n désigne le nombre en écriture décimale

   Tant que n non nul:
      On soustrait la plus grande puissance de 2 au nombre n
      On affecte la différence au nombre n.

   On renvoie les différentes puissances de 2 utilisées

.. admonition:: Exemple

   On donne ci-dessous la conversion en binaire du nombre décimal 41:

   - :math:`32=2^{5}` est la plus grande puissance de 2 que l'on peut enlever à 41;
      il reste :math:`41-32=9`.
   - :math:`8=2^{3}` est la plus grande puissance de 2 que l'on peut enlever à 9; 
      il reste alors :math:`9-8=1`.
   - :math:`1=2^{0}` est la plus grande puissance de 2 que l'on peut enlever à 1; 
      il reste alors :math:`1-1=0`.

   Le nombre 41 s'écrit en binaire:

   .. math::
   
      \begin{align*}
      41_{10} &= 2^{5} + 2^{3} + 2^{0}\\
      41_{10} &= 1 \times 2^{5} + 0 \times 2^{4} + 1 \times 2^{3} + 0 \times 2^{2} + 0 \times 2^{1} + 1 \times 2^{0}\\
      41_{10} &= 101001_{2}
      \end{align*}

.. tip::

   Pour convertir un nombre entier décimal en binaire, on peut remplacer la soustraction par la division euclidienne. En voici l'algorithme:
   
   .. code::
   
      n est le nombre décimal à convertir en binaire
      
      Tant que n est non nul:
         On divise n par 2.
         On affecte à n le quotient entier obtenu
            
      On renvoie les restes des divisions en partant du dernier calculé.

   Ci-dessous les différentes divisions euclidiennes à calculer.

   .. figure:: ../img/div-succ-binaire.png
      :width: 400px
      :align: center

   Comme pour la méthode précédente, on obtient :math:`41_{10}=101001_{2}`.

Écriture binaire à écriture hexadécimale
----------------------------------------

La conversion d'un nombre binaire en écriture hexadécimale est beaucoup plus simple. 

On regroupe les chiffres de l'écriture binaire par groupe de 4 bits appelé **quartet**, en commençant par la gauche. 
Ensuite on convertit chaque quartet en chiffre hexadécimal.

.. admonition:: Exemple

   Le nombre 1101001 est écrit sur 7 bits.
   
   On le décompose en 2 quartets 110 et 1001. On ajoute le bit 0 au début du premier quartet sans que ça change sa valeur. 
   
   On convertit chaque quartet: 
   
   - :math:`0110_{2}=6_{16}` 
   - :math:`1001_{2}=9_{16}` 
   
   Le nombre binaire 1101001 s'écrit 69 en hexadécimal.

Écriture hexadécimale à écriture binaire
----------------------------------------

La conversion en binaire d'un nombre hexadécimal est simple aussi. 

Chaque chiffre hexadécimal est remplacé par son quartet en binaire. 

.. admonition:: Exemple
   
   Le nombre :math:`A8_{16}` a pour chiffres hexadécimaux A et 8.
   
   - Le chiffre A se convertit en binaire par 1010;
   - le chiffre 8 se convertit en binaire par 1000. 
   
   En associant ces deux quartets, on obtient l'écriture binaire : :math:`A8_{16} = 10101000_{2}`.

Écriture hexadecimale et à écriture décimale
--------------------------------------------

La conversion d'un nombre en écriture hexadécimale en écriture décimale se fait comme en binaire. Chaque chiffre de l'écriture hexadécimale est multiplié par la puissance de 16 à laquelle correspond sa position.

Le tableau ci-dessous redonne les 5 premières puissances de 16 :

.. table:: Puissances de 16
   :widths: auto
   :align: center
      
   ============== ============== ============== ============== ==============
   :math:`16^{4}` :math:`16^{3}` :math:`16^{2}` :math:`16^{1}` :math:`16^{0}` 
   ============== ============== ============== ============== ==============
   65536          4096           256            16             1           
   ============== ============== ============== ============== ==============

.. admonition:: Exemple

   Par exemple, le nombre :math:`A8_{16}` se convertit en décimal en effectuant le calcul:
    
   .. math::
    
      \begin{align*}
      A8_{16} &= A \times 16^{1} + 8 \times 16^{0}\\
      \phantom{A8_{16}} &= 10 \times 16 + 8 \times 1\\
      \phantom{A8_{16}} &= 160+8\\
      A8_{16} &= 168_{10}
      \end{align*}

   Le nombre hexadécimal :math:`A8_{16}` a pour valeur décimale 168.

Écriture décimale à écriture hexadécimale
-----------------------------------------

La conversion d'un nombre décimal en hexadécimal est plus délicate. On peut utiliser les mêmes méthodes que pour la conversion en binaire, à savoir par soustraction de puissances de 16 ou les divisions euclidiennes par 16.

.. admonition:: Exemple

   Le nombre entier positif 453 se convertit en hexadécimal par :math:`453_{10}=1C5_{16}`. 

   On donne les divisions successives de la conversion.

   .. image:: ../img/div-succ-hexa.png
      :width: 400px
      :align: center

.. tip::

   Pour convertir un nombre hexadécimal en décimal et inversement, il est parfois plus simple de passer par l'écriture binaire.
