from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import requests
import random

class ActionTest(Action):
   def name(self):
      return "action_test"

   def run(self, dispatcher, tracker, domain):
        # pega os valores de cada slots
        tipo_imovel = tracker.get_slot('tipo_imovel')
        #imovel_de_entrada = racker.get_slot('imovel_de_entrada')
        bairro = tracker.get_slot('bairro')
        contato = tracker.get_slot('contato')
        
        # constroi a msg 
        response = """ Dados pegos na conversa: user procura imovel do tipo '{}' no bairro '{}' e forneceu '{}' como contato""".format(tipo_imovel,bairro, contato)
        try:
          dispatcher.utter_message(response)
        except ValueError:
          dispatcher.utter_message(ValueError)

