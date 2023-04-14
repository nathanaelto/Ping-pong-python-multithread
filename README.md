Un arbitre, un joueur 1 et un joueur 2 jouent
 
L'arbitre génère un nombre aléatoire entre 1000 et 1 000 000
 
L'arbitre envoie ce nombre aux joueurs

Pour les joueurs :
* J'attend un nombre, sinon fin
  * Si nb pair -> nb / 2
  * Si nb impair -> (nb * 3 + 1) / 2
    * Si nb = 1 -> envoie à l'arbitre "Gagné"
    * Sinon -> envoie x à l'autre joueur 
* Continue jusqu'à ce que l'un des joueurs gagne
