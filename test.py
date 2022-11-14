import unittest
from unittest.mock import patch
import questionnaire
import os
import questionnaire_import
import json

'''
def additionner(a, b):
    return a + b


def conversion_numbre():
    num_str = input("Donner un nombre:  ")
    return int(num_str)

class TestUnitaireDemo(unittest.TestCase):
    # Mise en place ou préparation des données 
    def setUp(self):
        print("setUp")

    # Nettoyage
    def tearDown(self):
        print ("tearDown")

        
    def test_additionner(self):
        print("test_addition")
        self.assertEqual(additionner(5, 10), 15)


    def test_conversion_numbre(self):
        with patch("builtins.input", return_value="10"):
            self.assertEqual(conversion_numbre(), 10)
        with patch("builtins.input", return_value="abcd"):
            self.assertEqual(conversion_numbre(), 10)
'''

class TestQuestion(unittest.TestCase):
    def test_reponse(self):
        choix = ("choix1", "choix2", "choix3")
        q = questionnaire.Question("titre_question", choix, "choix2")
        with patch("builtins.input", return_value="1"):
            self.assertFalse(q.poser(1, 1))
        with patch("builtins.input", return_value="2"):
            self.assertTrue(q.poser(1, 1))



class TestQuestionnaire(unittest.TestCase):
    def setUp(self):
        print("setUp")

    # Nettoyage
    def tearDown(self):
        print ("tearDown")

    def test_questionnaire_lancer_questionnaire(self):
        file_name = os.path.join("test_data","cinema_alien_debutant.json")
        q = questionnaire.Questionnaire.from_json_file(file_name)
        self.assertIsNotNone(q)

        self.assertEqual(len(q.questions), 10)
        self.assertEqual(q.titre, "Alien")
        self.assertEqual(q.categorie, "Cinéma")
        self.assertEqual(q.difficulte, "débutant")

        # with patch("builtins.input", return_value="1"):
        #    self.assertEqual(q.lancer(), 4)


        # nbre de question = 10

        # catégorie, titre, dificulté
        #  patcher le input --> forcer de répondre toujours 1
        # lancer et tester que le score est bien 4


class TestImportQuestionnaire(unittest.TestCase):
    def test_import_format_json(self): 
        questionnaire_import.generate_json_file("Animaux", "Les chats", "https://www.codeavecjonathan.com/res/mission/openquizzdb_50.json")
        file_names = ("animaux_leschats_confirme.json","animaux_leschats_expert.json","animaux_leschats_debutant.json")

        for file_name in file_names:
            self.assertTrue(os.path.isfile(file_name))
            file = open(file_name, 'r')
            json_data = file.read()
            file.close()
            try:
                data = json.loads(json_data)
            except:
                self.fail("Probleme de fichier " + file_name)

            self.assertIsNotNone(data.get("titre"))
            self.assertIsNotNone(data.get("questions"))
            self.assertIsNotNone(data.get("difficulte"))
            self.assertIsNotNone(data.get("categorie"))

            for question in data.get("questions"):
                self.assertIsNotNone(question.get("titre"))
                self.assertIsNotNone(question.get("choix"))
                for choix in question.get("choix"):
                    self.assertGreater(len(choix[0]), 0)
                    self.assertTrue(isinstance(choix[1]), bool)

                bonne_reponse = [choix[0] for choix in question.get("choix") if choix[1]]
                self.assertEqual(len(bonne_reponse), 1)
unittest.main()