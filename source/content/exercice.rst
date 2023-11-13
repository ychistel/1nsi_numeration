Exercices
=========

Exercice 1
-----------

#. Donner l'écriture décimale des nombres entiers positifs codés en binaire.

   a. :math:`101_{2}`
   b. :math:`10111_{2}`
   c. :math:`11001101_{2}`


#. Donner l'écriture binaire des nombres entiers positifs écrits en décimal.

   a. :math:`54`
   b. :math:`132`
   c. :math:`245`

#. Convertir en notation binaire les nombres hexadécimaux suivants:

   a. :math:`16_{16}`
   b. :math:`3B_{16}`
   c. :math:`5E1_{16}`

#. Convertir en notation hexadécimale les nombres binaires suivants:

   a. :math:`10101_{2}`
   b. :math:`100100_{2}`
   c. :math:`111100001111_{2}`

#. Convertir en notation décimale les nombres suivants écrits en notation hexadécimale:

   a. :math:`3E_{16}`
   b. :math:`4F8_{16}`
   c. :math:`A53C_{16}`

#. Convertir en écriture hexadécimale les nombres suivants:

   a. :math:`168_{10}`
   b. :math:`1001_{10}`
   c. :math:`1616_{10}`


Exercice 2
-------------------------------

On souhaite écrire un code en Python qui convertit l'écriture décimale d'un nombre entier en écriture binaire. On se limite aux nombres entiers dont l'écriture ne dépasse pas 1 octet. 

On reprend l'algorithme donné dans le cours : 

.. code::
   
   # variables
   n : nombre décimal à convertir en binaire
   r : reste de la division entière de n par 2
   
   # conversion
   Tant que n est non nul:
      On calcule le reste entier de n et 2
      On calcule le quotient entier de n par 2 affecté à la variable n.
      On affiche le reste entier
   
#. Écrire en Python l'algorithme qui convertit un nombre en écriture décimale en écriture binaire.
#. Exécuter le code avec différentes valeurs de ``n``. Comment doit-on lire l'affichage pour avoir l'écriture binaire ?
#. On peut améliorer ce script en créant une variable ``nb`` qui contient l'écriture binaire sous forme d'une chaine de caractères. 

   Modifier le code précédent pour obtenir et afficher le nombre binaire sous forme d'une chaine de caractères. Par exemple, si ``n = 7``, la chaine de caractères ``nb`` qui contient son écriture binaire est ``'111'``.

   .. hint::

      On doit créer une chaine de caractères vide au départ, avant la boucle ``while``.

      .. code:: python

         nb = ''

      On concatène cette chaine avec le reste de la division que l'on transforme en chaine de caratère avec la fonction ``str`` ce qui s'écrit :

      .. code:: python

         nb = nb + str(r)

#. Pour finir, on propose de mémoriser l'écriture binaire dans un tableau. On doit:
   
   - créer une variable tableau qui contient 8 zéros : ``t = [0,0,0,0,0,0,0,0]``
   - créer une variable ``i`` qui désigne l'index d'une valeur du tableau; ``i`` est compris entre 0 et 7.
   - à chaque itération de la boucle ``while``, remplacer chaque valeur ``t[i]`` du tableau par le reste de la division et modifier l'index ``i``.

   Par exemple, si ``n = 7``, le tableau ``t`` qui contient son écriture binaire est ``[0,0,0,0,0,1,1,1]``

Exercice 3
----------

On souhaite écrire un code en Python qui convertit l'écriture décimale d'un nombre entier en écriture hexadécimale. On reprend l'algorithme donné dans le cours : 

.. code::
   
   n est le nombre décimal à convertir en hexadécimal
      
   Tant que n est non nul:
      On calcule le reste entier de n et 16
      On calcule la division entière de n par 16 affecté à la variable n.
      Si le reste est inférieur à 10:
         On affiche le reste entier calculé
      Sinon :
         On affiche le chiffre hexadécimal associé (10->A,11->B,etc.)
   
Écrire un script qui convertit un nombre en écriture décimale en écriture hexadécimal.
