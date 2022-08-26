
from curses import keyname
from html import entities


def get_last_message_text(resp):
    text = resp['text']
    return text

def get_last_message_intent(resp):
    intent = resp['intents'][0]['name']
    return intent

def get_last_message_entities(resp, intent):
    entity_list = resp['entities']

    entities = {}
    key_dict = ''
    value_dict= ''
    for key in entity_list:
        if key == 'program:program':
            key_dict = 'program'

        else:
            key_dict = 'query'

        value_dict = entity_list[key][0]['value']
        if intent == 'weather_search' and key_dict == 'query':
            value_dict = entity_list[key][1]['value']
        
        entities[key_dict] = value_dict


    return entities

def get_last_message_info(resp):
    text = get_last_message_text(resp)
    intent = get_last_message_intent(resp)
    entities = get_last_message_entities(resp, intent)

    info = {}
    info['text'] = text
    info['intent'] = intent
    info['entities'] = entities
    return info
