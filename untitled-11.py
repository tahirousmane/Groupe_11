class Compte:
    def __init__(self):
        self.numerocompteclient= ""
        self.balanceclient= ""
client_x = Compte()
client_x.numerocompteclient= "75777012"
client_x.balanceclient= "50euro"
print(client_x.numerocompteclient)
print(client_x.balanceclient)

class CompteEpargne:
    def __init__(self):
        self.nom = "Tahir"
        self.prenom = "Ousmane"
        self.adresse = "dang"
        self.compte1 = "4545"
        self.balance = 0
    def ajoute_argeant(self,montant):
        self.balance=montant
        print("vous avez ajouter 50euro ou Compte".format(montant,self.nom))
client_x= Compte()
client_x.nom="tahir"
client_x.ajouter_argeant="50euro"
print(client_x.balanceclient)
