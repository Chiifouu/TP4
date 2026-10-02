
""" testing"""
class Noeud :
    def __init__(self, val):
        self.val = val
        self.enfants = []

    """ """
    def ajt_noeud(self,enfant):
        self.enfants.append(enfant)

    def afficher(self):
        print(self.val)
        for enfant in self.enfants:
            enfant.afficher()

        #print(self.valeur)
        #for enfant in self.enfant:
            #enfant.expr(enfant)

    def evaluer(self,var []):*
    




