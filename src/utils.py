
def get_last_message_text(resp):
    text = resp['text']
    return text

def get_last_message_intent(resp):
    intent = resp['intents'][0]['name']
    return intent

def get_last_message_entity(resp):
    entity = resp['entities']['program:program'][0]['value']
    return entity

def get_last_message_info(resp):
    text = get_last_message_text(resp)
    intent = get_last_message_intent(resp)
    entity = get_last_message_entity(resp)

    info = {}
    info['text'] = text
    info['intent'] = intent
    info['entity'] = entity
    return info
