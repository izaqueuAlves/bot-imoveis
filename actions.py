# -*- coding: utf-8 -*-
from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk import Action
from rasa_core_sdk.events import SlotSet
import requests
import random

"""

   - para o tcc implementar apenas a venda do imovel;
   - pegar os dados desse imoevl;
   - salvar ou fazer a busca no banco de acordo com esses dados;
   - não perguntar se o usuario tem um imovel como entrada e nem perguntar sobre esse imovel;

"""


class ActionTest(Action):
    def name(self):
        return "action_test"

    def run(self, dispatcher, tracker, domain):
        # pega os valores de cada slots
        nome = tracker.get_slot('nome')
        tipo_imovel = tracker.get_slot('tipo_imovel')
        num_quartos = tracker.get_slot('num_quartos')
        bairro = tracker.get_slot('bairro')
        contato = tracker.get_slot('contato')
        
        # constroi a msg 
        response = """ Custom Action:\n
            Dados pegos na conversa: \n
            nome: '{}'\n
            procura imovel do tipo: '{}' \n
            com {} quartos\n
            no bairro: '{}',\n
            e forneceu '{}' como contato,\n""".format(nome, tipo_imovel,bairro, num_quartos, contato)
        try:
            dispatcher.utter_message(response)
        except ValueError:
            dispatcher.utter_message(ValueError)


class ActionCRUD(Action):
    def name(self):
        return "crud_action"
            
    def run(self, dispatcher, tracker, domain):
        response = """Resultado da busca por uma custom action.....\n
                      Imoveis retornados: \n
                      - \n
                      - \n
                      - \n """

        try:
            dispatcher.utter_message(response)
        except ValueError:
            dispatcher.utter_message(ValueError)



class UsuarioForm(FormAction):
    """Exemplo de um form action"""

    def name(self) -> Text:
        """nome unico para identificar o form"""

        return "usuario_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """uma lista de slots a serem preenchidos"""

        return ["nome", "tipo_imovel", "num_quartos", "bairro", "contato"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
         - an extracted entity
         - intent: value pairs
         - a whole message
         or a list of them, where a first match will be picked"""

        return {
            "nome": [self.from_entity(entity="nome"), self.from_text()],
            "tipo_imovel": [self.from_entity(entity="tipo_imovel"), self.from_text()],
            "num_quartos": [self.from_entity(entity="num_quartos"), self.from_text()],
            "bairro": [self.from_entity(entity="bairro"), self.from_text()],
            "contato": [self.from_entity(entity="contato"), self.from_text()],
        }

    
    @staticmethod
    def bairro_db() -> List[Text]:
       #Database de bairros suportados

        return [
            "13 de julho",
            "17 de março",
            "aeroporto",
            "américa",
            "atalaia",
            "bugio",
            "capucho",
            "centro",
            "cidade nova",
            "cirurgia",
            "coroa do meio",
            "dezoito do forte",
            "dom luciano",
            "farolândia",
            "getúlio vargas",
            "grageru",
            "inácio barbosa",
            "industrial",
            "jabotiana",
            "japãozinho",
            "jardim centenário",
            "jardins",
            "josé conrado de araújo",
            "lamarão",
            "luzia",
            "marivan",
            "novo paraíso",
            "olaria",
            "palestina",
            "pereira lobo",
            "ponto novo",
            "porto dantas",
            "salgado filho",
            "santa maria",
            "santo antônio",
            "santos dumont",
            "são conrado",
            "são José",
            "siqueira campos",
            "soledade",
            "suíssa",
            "zona de expansão",    
        ]
   
    # USED FOR DOCS: do not rename without updating in docs
    def validate_bairro(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Optional[Text]:
        """valida valor bairro."""

        if value.lower() in self.bairro_db():
            # validado com sucesso, seta o valor no slot 'bairro'
            return {"bairro": value}
        else:
            dispatcher.utter_template("utter_wrong_bairro", tracker)
            # validacao falhou, seta o slot para 'none'
            # pede que o usuario insira um bairro correto
            return {"bairro": None}


    @staticmethod
    def tipo_imovel_db() -> List[Text]:
       #Database de bairros suportados

        return [
            "casa",
            "ap",
            "apartamento",
            "ksa",
        ]
   
    # USED FOR DOCS: do not rename without updating in docs
    def validate_tipo_imovel(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Optional[Text]:
        """valida valor tipo_imovel."""

        if value.lower() in self.tipo_imovel_db():
            # validado com sucesso, seta o valor no slot 'tipo_imovel'
            return {"tipo_imovel": value}
        else:
            dispatcher.utter_template("utter_wrong_tipo_imovel", tracker)
            # validacao falhou, seta o slot para 'none'
            # pede que o usuario insira um tipo_imovel correto
            return {"tipo_imovel": None}
    @staticmethod
    def is_int(string: Text) -> bool:
        """Checa se a string e um inteiro"""
    
        try:
            int(string)
            return True
        except ValueError:
                return False
    
    def validate_num_quartos(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Optional[Text]:
        """validar o valor de num_quartos"""

        if self.is_int(value) and int(value) > 0:
            return {"num_quartos": value}
        else:
            dispatcher.utter_template("utter_wrong_num_quartos", tracker)
            # validation failed, set slot to None
            return {"num_quartos": None}


    
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_template("action_test", tracker)
        return []

