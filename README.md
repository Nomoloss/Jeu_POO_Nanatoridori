# Jeu_POO_Nanatoridori

Version originale du jeu de société nommé _Jungo_ en France.

## Déroulement du jeu
Chaque joueur reçoit une main qu'il ne peut pas trier.

Les joueurs jouent chacun leur tour.

Quand son tour arrive, un joueur peut :
 - soit passer son tour et piocher une carte, qu'il peut placer *où il veut* dans sa main
 - soit jouer des cartes situées côte à côte dans sa main et plus fortes que ce qui a déjà été joué.
   Lorsque vous faites cela, vous avez le choix de récupérer ou non ces cartes jouées précédemment et de les placer *où vous voulez* dans votre main.
   
Si personne ne peut jouer au-dessus de ce qui a été posé, le joueur ayant joué cela ferme et remporte le pli, il peut alors jouer ce qu'il veut pour en commencer un nouveau.

Le dernier joueur se débarassant de toutes ses cartes perd une vie.

Rejouer des manches de cette façon jusqu'à ce qu'un joueur perde ses 2 vies.

La partie se termine lorsqu'un joueur perd ses 2 vies. Il est l'unique perdant du jeu, et les autres ont gagné.

## Puissance des cartes

Les cartes vont de 1 à 7. Les cartes de plus grande valeur sont plus fortes.

Les paires sont plus fortes que les cartes seules, et la puissance des paires entre elles dépend du chiffre dessus. Donc une paire de 1 est plus forte qu'un 7 tout seul, et une paire de 2 est plus forte qu'une paire de 1.

Les triplets sont plus forts que les paires, et ainsi de suite. (Donc un triplet de 1 est plus fort que n'importe quelle paire, mais moins fort qu'un triplet de 2)

Par exemple :

[2] < [7] < [5] [5] < [6] [6] < [3] [3] [3] < [1] [1] [1] [1] [1] [1]

*Chaque carte est présente en 9 exemplaires dans le jeu

## Comment jouer sur la console
4 joueurs requis.

Choisissez si vous voulez jouer ou passer avec "j" et "p".

Pour jouer une carte tapez sa position (de 0 à longueur de la main - 1).
Pour jouer plusieurs cartes cartes tapez leurs positions séparées par des virgules.

Exemple : 

Votre main : [1, 2, 5, 3, 6, 6, 3, 1]

Vous ne pouvez pas jouer la paire de 1 puisque les 2 cartes ne sont pas côte à côte. Taper "0,7" ne fera pas avancer le jeu. 
En revanche, vous pouvez jouer la paire de 6 puisque les cartes sont côte à côte. Pour cela, il faudra taper "4,5" ou "5,4" (l'ordre n'importe pas).

Après avoir passé votre tour, choisissez avec "y" ou "n" si vous souhaitez garder la carte piochée. De la même façon, choisissez avec "y" ou "n" si vous souhaitez garder la/les carte(s) jouée(s) précédemment lorsque vous jouez plus fort.

Dans les deux cas, si vous souhaitez la/les conserver, vous devrez indiquer leur position (de 0 à longueur de votre main -1) d'insertion.

Exemple :

Votre main : [2, 3, 6]

Vous avez joué une paire de 4 sur une paire de 3 et vous avez décidé de récupérer la paire de 3 pour vous faire un triplet de 3.

Tapez 1 et votre main deviendra : [2, 3, 3, 3, 6]
