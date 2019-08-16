# -*- coding: utf-8 -*-
from typing import Dict, Text, Any, List, Union, Optional
from rasa_sdk import Action
from rasa_core_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
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


class UsuarioForm(FormAction):
      """Exemplo de um custom form action """
      
      def name(self)-> Text:
            """nome unico """
            return "usuario_form"
         

      # retorna uma lista de slots
      @staticmethod  
      def slots_requeridos(tracker: Tracker) -> List[Text]:
            """uma lista de slots a serem preenchidos """
            return ["nome", "contato", "bairro"]

      
      def submit(self):
            """ define o que será feito quando tods os slots tiverem sido preenchidos"""

            dispatcher.utter_template('utter_', tracker)
            return []


      
