import requests

app_id = "c4dedddb"
app_key = "e7675dc435b1e7ee12030a14d3f1f9c6"
language = "en-gb"

def get_definition(word_id):
    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
    response = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
    response = response.json()
    if 'error' in response.keys():
        return False

    output = {}
    senses = response['results'][0]['lexicalEntries'][0]['entries'][0]['senses']
    definitions = []
    for sense in senses:
        #sensess = senses['definitions'][0]
        #print(sensess)
        definitions.append(f"✔️ {sense['definitions'][0]}")
    output['definitions'] = '\n'.join(definitions)

    if response['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0].get('audioFile'):
        output['audio'] = response['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']

    return output

    
if __name__ == '__main__':
    print(get_definition('kjegrhl'))