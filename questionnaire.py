# PROJET QUESTIONNAIRE V3 : POO
#
# - Pratiquer sur la POO
# - Travailler sur du code existant
# - Mener un raisonnement
#
# -> Définir les entitées (données, actions)
#
# Question
#    - titre       - str
#    - choix       - (str)
#    - bonne_reponse   - str
#
#    - poser()  -> bool
#
# Questionnaire
#    - questions      - (Question)
#
#    - lancer()
#

import json
import sys

# Liste de tous les questionnaire 

liste_des_fichiers = ['animaux_leschats_confirme.json',
                        'animaux_leschats_debutant.json',
                        'animaux_leschats_expert.json',
                        'arts_museedulouvre_confirme.json',
                        'arts_museedulouvre_debutant.json',
                        'arts_museedulouvre_expert.json',
                        'cinema_alien_confirme.json',
                        'cinema_alien_debutant.json',
                        'cinema_alien_expert.json',
                        'cinema_starwars_confirme.json',
                        'cinema_starwars_debutant.json',
                        'cinema_starwars_expert.json']



class Question:
    def __init__(self, titre, choix, bonne_reponse):
        self.titre = titre
        self.choix = choix
        self.bonne_reponse = bonne_reponse


    def from_json_data(data):
        # ....
        choix = [chx[0]  for chx in data["choix"]]
        bonne_reponse = [chx[0]  for chx in data["choix"] if chx[1]]
        if len(bonne_reponse) != 1: 
            return None
            
        q = Question(data["titre"], choix, bonne_reponse[0])
        return q

    def poser(self, inc, nb_ques):
        print("QUESTION " + str(inc) + "/ " + str(nb_ques))
        print("  " + self.titre)
        for i in range(len(self.choix)):
            print("  ", i+1, "-", self.choix[i])

        print()
        resultat_response_correcte = False
        reponse_int = Question.demander_reponse_numerique_utlisateur(1, len(self.choix))
        if self.choix[reponse_int-1].lower() == self.bonne_reponse.lower():
            print("Bonne réponse")
            resultat_response_correcte = True
        else:
            print("Mauvaise réponse")
            
        print()
        return resultat_response_correcte

    def demander_reponse_numerique_utlisateur(min, max):
        reponse_str = input("Votre réponse (entre " + str(min) + " et " + str(max) + ") :")
        try:
            reponse_int = int(reponse_str)
            if min <= reponse_int <= max:
                return reponse_int

            print("ERREUR : Vous devez rentrer un nombre entre", min, "et", max)
        except:
            print("ERREUR : Veuillez rentrer uniquement des chiffres")
        return Question.demander_reponse_numerique_utlisateur(min, max)
    
class Questionnaire:
    def __init__(self, questions, categorie, titre, difficulte):
        self.questions = questions
        self.categorie = categorie
        self.titre = titre
        self.difficulte = difficulte


    def from_json_data(data):
        questionnaire_brut = data["questions"]
        questions = [Question.from_json_data(question) for question in questionnaire_brut]
        return Questionnaire(questions, data['categorie'], data['titre'], data['difficulte'])

    def lancer(self):
        nb_question = len(self.questions)
        print ("-------------------------------------")
        print("Catégorie: " + self.categorie  + "  "
                "Titre: " + self.titre + "  "
                "Difficulte: " + self.difficulte  + "  "
                "Nombre de question:  "+ str(nb_question))
        print ("-------------------------------------")

        score = 0
        for i in range(nb_question):
            if self.questions[i].poser(i+1, nb_question):
                score += 1
        print("Score final :", score, "sur", nb_question)
        return score

    def from_json_file(fichier):
        # choix_quizz = Quizz.choix_de_quizz_utlisateur(1, len(self.fichiers))

        # fichier =  self.fichiers[choix_quizz]

        # fichier = 'animaux_leschats_confirme.json'
        data = open(fichier, 'r')
        dataJson = json.load(data)
        data.close() 
        return Questionnaire.from_json_data(dataJson)


# Version dynamique du questionnaire: 
def choix_de_quizz_utlisateur(min, max):
    qizz_str = input("Faites un choix de quizz entre " + str(min) + " et " + str(max) + ") :")
    try:
        qizz_int = int(qizz_str)
        if min <= qizz_int <= max:
            return qizz_int 

        print("ERREUR : Vous devez rentrer un nombre entre", min, "et", max)
    except:
        print("ERREUR : Veuillez rentrer uniquement des chiffres")
    return choix_de_quizz_utlisateur(min, max)



if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Donner un nom de fichier ")
        exit(0)

    json_file_name = sys.argv[1]
    Questionnaire.from_json_file(json_file_name).lancer()

else:
    print(__name__)


