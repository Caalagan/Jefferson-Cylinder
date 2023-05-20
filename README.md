# Jefferson-Cylinder

prob :

Pas tout le temps et pas sûr:
Change plusieures ligne au lieu d'une : change toujours la ligne 1 et 2 alors que bah non en fait

A faire du plus au moins urgent :

Finir l'affichage graphique :

    ETAPES :

    URGENT
    -> finir la partie chiffrement : affichage clear / chiffré (Mieux les placer ) - puis bouton pour finir le chiffrement & afficher la clé et le nombre de ligne a sauter pour avoir la phrase en clair( nombre de ligne a sauter a finir )

    URGENT
    -> changer le code : quand on lance le fichier affichage_graphique.py on doit tomber sur une fenetre qui propose chiffrage / déchiffrage


    -> Faire la partie déchifrement : quand elle est lancé : prend le fichier cylindre.txt et demande a l'utilisateur si c'est bien le bon cylindre.txt (si non on lui demande de le changer)

    ////////////
    Puis demande la clé (si non on lui demande de la changer)
                    OU
    On fait comme dans la partie chiffrage : on affiche les cylindre et on reprend le meme systeme pour choisir la clé
    ////////////

    Puis affiche les cylindres dans le bon ordre

    (A voir si on met un truc pour montrer ou est la ligne en clair et la ligne chiffré)

Voies d'améliorations :

Pour l'affichage graphique on peut :

    Faire deux fichier : un pour chiffrement et un pour déchiffrement

    Pour le chiffrement on fait comme dans la consigne et on peut même rajouter un fichier pour enregistrer la clé si on veut la partager pour le déchiffrement.

    Pour le déchiffrement on demande a l'utilisateur si le cylindre.txt contient bien le bon cylindre sinon le lui demande de le changer pui on le demande si c'est bien la clé qu'il veut.

    OU

    Faire un seul fichier avec un menu au début qui propose chiffrement/déchiffrement

    Ajouter un bouton pour faire le chiffrement ou non : si oui alors on continue et affiche les fleches sinon on réaffiche les boutons pour changer la clé

Ajouter des commentaires à chaque fonction pour les expliquer

Prendre en compte les accents

Comment ça marche :

Cet appareil est constitué d’un certain nombre de disques, 36 pour l’original, pivotants autour d’un axe et sur lesquels sont inscrits des alphabets désordonnés. Les deux correspondants disposent des mêmes disques.

Chaque disque est identifiable par un numéro. La clé est l’ordre dans lequel les disques sont insérés sur l’axe, il s’agit donc d’une suite de numéros.

Pour chiffrer un message, l’expéditeur arrange les disques selon la clé, puis les fait pivoter de telle sorte que le message apparaisse sur une même ligne du cylindre. Le message chiffré sera alors le contenu de la sixième ligne suivante (ce dernier choix n’est que conventionnel, on aurait pu en effectuer un autre).

Pour déchiffrer un message, le destinataire arrange bien sûr lui aussi les disques selon la clé, puis les fait pivoter de telle sorte que le message chiffré apparaisse sur une même ligne du cylindre. Le message d’origine sera alors le contenu de la sixième ligne précédente.

Résumé :

Chiffrer un message :

1. Arranger les disques selon la clé

2. Faire pivoter les disques de telle sorte que le message apparaisse sur une même ligne du cylindre

3. Le message chiffré est le contenu de la sixième ligne suivante

Déchiffrer un message :

1. Arranger les disques selon la clé

2. Faire pivoter les disques de telle sorte que le message chiffré apparaisse sur une même ligne du cylindre

3. Le message d’origine est le contenu de la sixième ligne précédente

Foncionnalitées a implémenter (Version console):

1. Tirage aléatoire d'une chaîne de caractère constituée des 26 lettres de l'alphabet.

2. Écriture de n lignes dans un fichier texte, n étant un paramètre entier strictement positif, chacune d'elles étant générée selon le tirage précédent.

3. Lecture d'un fichier texte dont chaque ligne contient une permutation des 26 lettres de l’alphabet en majuscules et création d'un dictionnaire dont les clés sont les entiers compris entre un 1 et le nombre de lignes du fichier, la valeur correspondante à une clé i étant la i-ème ligne du fichier.

(Validité d'une clé) 4. Vérification si une liste de n entiers est une permutation des entiers compris (au sens large) entre 1 et n.

(Validité d'une clé) 5. Génération d'une permutation des entiers compris (au sens large) entre 1 et n.

(Chiffrement d'une seule lettre) 6. Chiffrement d'une lettre relativement à une permutation des 26 lettres de l’alphabet en majuscules : on retourne la lettre située 6 positions après elle dans la permutation. On suppose bien sûr que l’alphabet en question est circulaire.

7. À partir d'un cylindre, i.e. un dictionnaire comme décrit précédemment, et d'une clé, i.e. l'ordre des cylindres, chiffrer un texte selon l'algorithme de Jefferson.

8. Même chose mais cette fois pour déchiffrer un texte.

Fonctionnalitées a implémenter (Version graphique): (CF images du cours)

1. On aura d'abord une première fonctionnalité qui à partir d'un fichier texte du format décrit dans la partie 2 affiche verticalement les différents cylindres dans l'ordre du fichier puis permet de sélectionner la clé, i.e. l'ordre des cylindres.

2. En cliquant successivement sur les nombres de la dernière ligne on peut alors constituer la clé

3. On réordonne alors les cylindres selon la clé

4. Grâce aux flèches (flèches cliquable avec la souris) on peut alors faire pivoter les cylindres et ainsi choisir le texte à chiffrer puis récupérer le texte une fois chiffré

Bonus :

Construire physiquement, c'est-à-dire avec des disques et un axe, un cylindre de Jefferson.

On pourra le réaliser avec une imprimante 3D ou en démontrant des talents de menuisier voire de ferronnier.

Une grande qualité est attendue pour que ce bonus soit valorisé.
