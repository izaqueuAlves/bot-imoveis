## path_comprar
* comprar
   - utter_comprar

## tipo_imovel
* tipo_imovel
   - utter_tipo_imovel

## bairro
* bairro
   - utter_bairro
## imovel_de_entrada
* imovel_de_entrada
   - utter_imovel_de_entrada

## valor_imovel_entrada
* valor_imovel_entrada
    - utter_valor_imovel_entrada

## contato
* contato
   - utter_contato



## hist
* cumprimentar_visitante
    - utter_cumprimentar_visitante
* cumprimentar{"nome":"paulo"}
    - utter_cumprimentar
* comprar
    - utter_comprar
* tipo_imovel
    - usuario_form
    - form{"name": "usuario_form"}
    - form{"name":null}
* bairro
    - utter_bairro
    - utter_continuar_conversa
* negar
    - utter_negar
    - utter_buscar_imovel
* pedir_contato
    - utter_pedir_contato
* contato
    - utter_contato
    - utter_despedir



## historia_1
* cumprimentar_visitante
    - utter_cumprimentar_visitante
* cumprimentar{"nome":"paulo"}
    - utter_cumprimentar
* comprar
    - utter_comprar
* tipo_imovel{"tipo_imovel": "casa"}
    - slot{"tipo_imovel": "casa"}
    - utter_tipo_imovel
* bairro
    - utter_bairro
    - utter_continuar_conversa
* negar
    - utter_negar
    - utter_buscar_imovel
* pedir_contato
    - utter_pedir_contato    
* contato
    - utter_contato
    - utter_despedir


## historia_2
* cumprimentar_visitante
    - utter_cumprimentar_visitante
* cumprimentar{"nome":"paulo"}
    - utter_cumprimentar
* comprar
    - utter_comprar
* tipo_imovel
    - utter_tipo_imovel
* bairro
    - utter_bairro
    - utter_continuar_conversa
* imovel_de_entrada
    - utter_imovel_de_entrada
* valor_imovel_entrada
    - utter_valor_imovel_entrada
* pedir_contato
    - utter_pedir_contato    
* contato
    - utter_contato
    - utter_despedir



