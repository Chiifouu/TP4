from noeud import Noeud

x = Noeud("exp")
y = Noeud("+")

x.ajt_noeud(y)
y.ajt_noeud(Noeud(2))
y.ajt_noeud(Noeud("y"))

x.afficher()