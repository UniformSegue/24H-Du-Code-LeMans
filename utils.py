##########################################################
#                                                        #
#          CODE BY PAIN DE MIE AND MOYASU                #
#                                                        #
##########################################################

import re
import requests
import json

#url use with https://github.com/LeMans-SchoolofAI/24hcode2025

def info_resto(name):
    r = requests.get("https://app-584240518682.europe-west9.run.app/api/restaurants",headers={"Authorization": "Token umTAIDGq3gUWlFODZZLF9jnnbQddBbYp"})
    rdico = json.loads(r.text)["results"]

    for dico in rdico:
        if dico['name'] == name:
            dicofinal = dico
            break
    result = ""
    for keys, values in dicofinal.items():
        if keys == "id":
            continue
        result += str(values) + " "
        result += ","

    return result



def resto_list_name():
    r = requests.get("https://app-584240518682.europe-west9.run.app/api/restaurants",headers={"Authorization": "Token umTAIDGq3gUWlFODZZLF9jnnbQddBbYp"})
    rdico = json.loads(r.text)["results"]
    result = ""
    for resto in rdico:
        result += resto["name"] + ", "
    return result



def spa_list():
  headers = {"Authorization": "Token	umTAIDGq3gUWlFODZZLF9jnnbQddBbYp"}
  url = 'https://app-584240518682.europe-west9.run.app/api/spas'
  r = requests.get(url, headers=headers)
  rdico = json.loads(r.text)
  result = ""
  for spa in rdico:
    result += spa['name'] + ", "
  return result



def info_spa(name):
    rdico = None
    headers = {"Authorization": "Token	umTAIDGq3gUWlFODZZLF9jnnbQddBbYp"}
    url = 'https://app-584240518682.europe-west9.run.app/api/spas'
    r = requests.get(url, headers=headers)
    for dico in json.loads(r.text):
      if dico['name'] == name:
        rdico = dico
        break
    result = ""
    for keys,values in rdico.items():
      if keys == "id":
        continue
      result += str(values) + " "
      result += ","

    return result


def get_weather_utils(city: str) -> str:
    api_key = 'fa53311b01388ef218f26a9bd0ed1e3d'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        return f"La température actuelle à {city} est de {data['main']['temp']}°C."
    else:
        return "Désolé, je n'ai pas pu récupérer la météo."


def meals_list():
    headers={"Authorization":"Token	umTAIDGq3gUWlFODZZLF9jnnbQddBbYp"}
    url = 'https://app-584240518682.europe-west9.run.app/api/meals'
    r = requests.get(url ,headers=headers)
    rdico = json.loads(r.text)
    meals = rdico["results"]
    result = ""
    for meal in meals:
        result += meal["name"] + ", "
    return result


def get_id_by_name(name):  #secteur in ['meals', 'clients', 'reservation']
    headers={"Authorization":"Token	umTAIDGq3gUWlFODZZLF9jnnbQddBbYp"}
    url = 'https://app-584240518682.europe-west9.run.app/api/clients/?search={}'.format(name)
    r = requests.get(url ,headers=headers)
    try:
        rdico = json.loads(r.text)
        result = rdico["results"][0]["id"]
        return result
    except:
        return -1

def search_info_by_name(name):  #secteur in ['meals', 'clients', 'reservation']
    headers={"Authorization":"Token	umTAIDGq3gUWlFODZZLF9jnnbQddBbYp"}
    url = 'https://app-584240518682.europe-west9.run.app/api/clients/?search={}'.format(name)
    r = requests.get(url ,headers=headers)

    try:
        rdico = json.loads(r.text)
        dico = rdico["results"][0]
        result = ""

        for key,value in dico.items():
            if key == "id":
                continue
            result +=str(key) + " : " + str(value) + ", "
        return result
    except:
        return "Pas de client a se nom"



def add_clients(name, phone_number, room_number, special_request):
    headers={"Authorization":"Token	umTAIDGq3gUWlFODZZLF9jnnbQddBbYp", 'Content-type': 'application/json'}
    url = 'https://app-584240518682.europe-west9.run.app/api/clients/'
    r = requests.post(url , json = {"name": name, "phone_number": phone_number, "room_number": room_number, "special_requests": special_request} ,headers=headers)
    if r.status_code == 201:
        return "ajoute client reussi"
    else:
        return "ajoute client echouer"

def search_client_by_id(id):
    headers={"Authorization":"Token	umTAIDGq3gUWlFODZZLF9jnnbQddBbYp"}
    url = 'https://app-584240518682.europe-west9.run.app/api/clients/' + str(id)
    r = requests.get(url ,headers=headers)
    rdico = json.loads(r.text)
    result = ""
    for key, value in rdico.items():
        if key == "id":
            continue
        result += str(key) + " : " + str(value) + ", "

    return result

def search_client_by_id_dico(id):
    headers={"Authorization":"Token	umTAIDGq3gUWlFODZZLF9jnnbQddBbYp"}
    url = 'https://app-584240518682.europe-west9.run.app/api/clients/' + str(id)
    r = requests.get(url ,headers=headers)
    rdico = json.loads(r.text)
    return rdico

def modif_client(id,name,num,numero_chambre,request):
    headers={"Authorization":"Token	umTAIDGq3gUWlFODZZLF9jnnbQddBbYp"}
    url = 'https://app-584240518682.europe-west9.run.app/api/clients/' + str(id) +"/"
    r = requests.put(url ,{"name":name ,"phone_number": num ,"room_number": numero_chambre,"special_requests": request} ,headers=headers)
    if r.status_code == 200:
        return "modif client reussi"
    else:
        return "modif client echouer"

def del_user(id):
    headers={"Authorization":"Token	umTAIDGq3gUWlFODZZLF9jnnbQddBbYp"}
    url = "https://app-584240518682.europe-west9.run.app/api/clients/"+str(id)+"/"
    r = requests.delete(url ,headers=headers)
    if r.status_code == 204:
        return "suppression client reussi"
    else:
        return "suppression client echouer"

def extract_values_two_force(input_string):
    try:
        # Parse la chaîne JSON
        data = json.loads(input_string)

        # Retourne la liste des valeurs
        return list(data.values())

    except json.JSONDecodeError:
        try:
            match = re.match(r"(.*?)[\|,.;:\/](.*)", input_string)

            if match:
                return [match.group(1), match.group(2)]
            else:
                print("Erreur : La chaîne ne correspond pas au format attendu.")
                return []
        except TypeError:
            return "Client inexistant"

def extract_value_one_force(input_string):
    match = re.match(r'[a-zA-Z0-9]+', input_string)
    if match:
        return match.group(0)
    else:
        # Regex pour capturer la valeur dans {"key":"value"}
        match = re.match(r'{"[^"]*":"([^"]*)"}', input_string)

        if match:
            return match.group(1)
        else:
            match = re.match(r'[^,]+([^\w\s]+)(.*)', input_string)

            if match:
                return match.group(2)
            else:

                    return "Client inexistant"



def extract_values_four_force(input_string):
    try:
        # Parse le string JSON
        data = json.loads(input_string)

        # Vérifie qu'il y a au moins 4 paires clé-valeur et retourne les valeurs
        if len(data) >= 4:
            return list(data.values())[:4]  # Retourne les 4 premières valeurs
        else:
            return len(data)

    except json.JSONDecodeError:
        # Regex pour capturer 4 valeurs séparées par un séparateur quelconque
        match = re.match(r'([^,]+)[^\w\s]+([^,]+)[^\w\s]+([^,]+)[^\w\s]+([^,]+)', input_string)

        if match:
            return [match.group(1), match.group(2), match.group(3), match.group(4)]  # Retourne les 4 valeurs
        else:
            match = re.match(r'{"[^"]*":"([^"]*)",\s*"[^"]*":"([^"]*)",\s*"[^"]*":"([^"]*)",\s*"[^"]*":"([^"]*)"}',
                             input_string)

            if match:
                return [match.group(1), match.group(2), match.group(3), match.group(4)]  # Retourne les 4 valeurs
            else:
                return "Client inexistant"

def extract_values_three_force(input_string):
    try:
        # Parse le string JSON
        data = json.loads(input_string)

        # Vérifie qu'il y a au moins 3 paires clé-valeur et retourne les valeurs
        if len(data) >= 3:
            return list(data.values())[:3]  # Retourne les 3 premières valeurs
        else:
            print("Erreur : Il n'y a pas assez de paires clé-valeur dans le JSON.")
            return None

    except json.JSONDecodeError:
        match = re.match(r'{"[^"]*":"([^"]*)",\s*"[^"]*":"([^"]*)",\s*"[^"]*":"([^"]*)"', input_string)

        if match:
            return [match.group(1), match.group(2), match.group(3)]  # Retourne les 3 premières valeurs
        else:
            match = re.match(r'([^,]+),([^,]+),([^,]+)', input_string)

            if match:
                return [match.group(1), match.group(2), match.group(3)]  # Retourne les 3 valeurs extraites
            else:
                return "Client inexistant"


def find_reservation_id(id):#renvoie les infos de la reservation correspondant a l'id entrée
    dicotemp={}
    for i in range(1,7):
        r = requests.get("https://app-584240518682.europe-west9.run.app/api/reservations/?page="+str(i) ,headers={"Authorization": "Token umTAIDGq3gUWlFODZZLF9jnnbQddBbYp"})
        rdico = json.loads(r.text)["results"]
        for j in range(len(rdico)) :
            num_resa=rdico[j]["id"]
            dicotemp[num_resa]=rdico[j]
        result = ""

        for key,value in dicotemp[id].items():
            result += str(key) + " : " + str(value) + ", "
        return result

def del_reservations(id):
    headers={"Authorization":"Token	umTAIDGq3gUWlFODZZLF9jnnbQddBbYp"}
    url = "https://app-584240518682.europe-west9.run.app/api/reservation/"+id+"/"
    r = requests.delete(url ,headers=headers)
    if r.status_code == 204:
        return "suppression client reussi"
    else:
        return "suppression client echouer"

def add_reservations(client, restaurant, date, meal, number_of_guests, special_requests):
    headers={"Authorization":"Token	umTAIDGq3gUWlFODZZLF9jnnbQddBbYp", 'Content-type': 'application/json'}
    url = 'https://app-584240518682.europe-west9.run.app/api/reservations/'
    r = requests.post(url , json = {'client' : client, 'restaurant' : restaurant, 'date' : date, 'meal': meal, 'number_of_guests' : number_of_guests, 'special_requests' : special_requests} ,headers=headers)
    if r.status_code == 201:
        rdico = json.loads(r.text)
        return "Id reservation : " + str(rdico["id"])
    else:
        return "reservation client echouer"

def extract_values_six_force(input_string):
    try:
        # Parse le string JSON pour vérifier sa validité
        data = json.loads(input_string)

        # Vérifie qu'il y a au moins 6 paires clé-valeur et retourne les 6 premières valeurs
        if len(data) >= 6:
            return list(data.values())[:6]  # Retourne les 6 premières valeurs
        else:
            print("Erreur : Il n'y a pas assez de paires clé-valeur dans le JSON.")
            return None

    except json.JSONDecodeError:


        match = re.match(r'([^,]+),([^,]+),([^,]+),([^,]+),([^,]+),([^,]+)', input_string)

        if match:
            return [match.group(1), match.group(2), match.group(3), match.group(4), match.group(5),
                    match.group(6)]  # Retourne les 6 valeurs extraites
        else:
            match = re.match(
                r'{"[^"]*":"([^"]*)",\s*"[^"]*":"([^"]*)",\s*"[^"]*":"([^"]*)",\s*"[^"]*":"([^"]*)",\s*"[^"]*":"([^"]*)",\s*"[^"]*":"([^"]*)"}',
                input_string)

            if match:
                return [match.group(1), match.group(2), match.group(3), match.group(4), match.group(5),
                        match.group(6)]  # Retourne les 6 premières valeurs
            else:
                return "Reservation impossible"



