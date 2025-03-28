import random

import soundfile as sf
from IPython.display import display, Audio
from kokoro import KPipeline
from langchain_core.tools import tool, Tool
import utils
import utils as ut


first_page = "Fais un phrase avec ces mots clé : "

@tool
def personnaliter():
    """
    Presente toi avec ces mots clé
    :return:
    """
    return first_page+"Nom : FrancisIa, Réceptionniste Hôtel California, hôtel légendaire, cadre paradisiaque, atmosphère unique, service impeccable, aide clients, informations, questions, services, enregistrements, départs, chambres, équipements, activités locales, courtois, respectueux, efficace."


@tool
def get_weather(city: str) -> str:
    """
    :param city:
    :return:
    """
    return utils.get_weather_utils(city)




@tool
def list_restaurant() -> str:
    """
    :return:
    """
    return first_page+ut.resto_list_name()

@tool
def info_restaurant(name:str) -> str:
    """
    Donne des infos sur le restaurant. Donne une belle forme a la phrase pour presenter le restaurant.
    :param name:
    :return:
    """
    return first_page+ utils.info_resto(name)

@tool
def list_spa() -> str:
    """
    :return:
    """
    return first_page+ut.spa_list()

@tool
def info_spa(name:str) -> str:
    """
    Donne des infos sur le spa. Donne une belle forme a la phrase pour presenter le spa.
    :param name:
    :return:
    """
    name = utils.extract_value_one_force(name)
    return first_page+utils.info_spa(name)
@tool
def info_meal() -> str:
    """
    Donne des infos sur les repas. Donne une belle forme a la phrase pour presenter le spa.
    :return:
    """
    return first_page+utils.meals_list()

@tool
def info_name(client_name:str) -> str:
    """
    Donne des infos sur le client. Donne une belle forme a la phrase pour presenter le client.
    :param client_name:
    :return:
    """
    client_name = utils.extract_value_one_force(client_name)
    return first_page+utils.search_info_by_name(client_name)

@tool
def id_name(client_name:str) -> str:
    """
    Donne id du client. Donne une belle forme a la phrase pour presenter le client.
    :param client_name:
    :return:
    """
    return utils.get_id_by_name(client_name)

@tool
def add_clients(data:str) -> str:
    """
    Donne id du client. Donne une belle forme a la phrase pour presenter le client.
    :param data:
    :return:
    """
    if utils.extract_values_four_force(data) == 3:
        result = utils.extract_values_three_force(data)
        client_name = result[0]
        phone_numbers = result[1]
        room_numbers = random.randint(1,300)
        special_requests = result[2]
    else:
        result = utils.extract_values_four_force(data)
        client_name = result[0]
        phone_numbers = result[1]
        room_numbers = result[2]
        special_requests = result[3]


    return first_page+utils.add_clients(client_name,phone_numbers,room_numbers,special_requests)

@tool
def search_client_by_id(id:str) -> str:
    """
        Donne les info du client par son id. Donne une belle forme a la phrase pour presenter le client.
        :param id:
        :return:
        """
    return first_page + utils.search_client_by_id(id)

@tool
def modif_client_name(data:str) -> str:
    """
    modifie un client. Donne une belle forme a la phrase pour presenter le client.
    :param data:
    :return:
    """
    results = utils.extract_values_two_force(data)

    client_name = results[0]
    name = results[1]

    id = utils.get_id_by_name(client_name)
    client = utils.search_client_by_id_dico(id)

    return first_page+utils.modif_client(str(id),name,client["phone_number"],client["room_number"],client["special_requests"])
@tool
def modif_client_phone_numbers(data:str) -> str:
    """
    modifie un client. Donne une belle forme a la phrase pour presenter le client.
    :param data:
    :return:
    """
    results = utils.extract_values_two_force(data)
    client_name = results[0]
    phone_numbers = results[1]

    id = utils.get_id_by_name(client_name)
    client = utils.search_client_by_id_dico(id)

    return first_page+utils.modif_client(id,client_name,phone_numbers,client["room_number"],client["special_requests"])

@tool
def modif_client_room_numbers(data:str) -> str:
    """
    modifie un client. Donne une belle forme a la phrase pour presenter le client.
    :param data:
    :return:
    """
    results = utils.extract_values_two_force(data)

    client_name = results[0]
    room_numbers = results[1]

    id = utils.get_id_by_name(client_name)
    if id == -1:
        return first_page+"Client inexistant"
    client = utils.search_client_by_id_dico(id)

    return first_page+utils.modif_client(str(id),client_name,client["phone_number"],str(room_numbers),client["special_requests"])

@tool
def modif_client_special_requests(data:str) -> str:
    """
    modifie un client. Donne une belle forme a la phrase pour presenter le client.
    :param data:
    :return:
    """

    results = utils.extract_values_two_force(data)

    client_name = results[0]
    special_requests = results[1]


    id = utils.get_id_by_name(client_name)
    client = utils.search_client_by_id_dico(id)

    return first_page+utils.modif_client(id,client_name,client["phone_number"],client["room_number"],special_requests)
@tool
def del_client_by_id(id:str) -> str:
    """
    supprime un client. Donne une belle forme a la phrase pour presenter le client.
    :param id:
    :return:
    """

    id = utils.extract_value_one_force(id)
    return first_page+utils.del_user(id)
@tool
def del_client_by_name(client_name:str) -> str:
    """
    supprime un client. Donne une belle forme a la phrase pour presenter le client.
    :param client_name:
    :return:
    """
    client_name = utils.extract_value_one_force(client_name)
    id = utils.get_id_by_name(client_name)
    return first_page+utils.del_user(id)

@tool
def find_reservation_by_id(id:str):
    """
        trouve la reservation par son id. Donne une belle forme a la phrase pour presenter le client.
        :param id:
        :return:
        """
    print(id)
    id = utils.extract_value_one_force(id)
    print(id)

    return first_page+utils.find_reservation_id(int(id))

@tool
def del_reservation_by_id(id:str) -> str:
    """
    supprime une reservation. Donne une belle forme a la phrase pour presenter le client.
    :param id:
    :return:
    """

    id = utils.extract_value_one_force(id)
    return first_page+utils.del_reservations(id)

@tool
def add_reservation_by_name(data:str) -> str:
    """
    supprime une reservation. Donne une belle forme a la phrase pour presenter le client.
    :param data:
    :return:
    """
    result = utils.extract_values_six_force(data)
    print(result)
    id = utils.get_id_by_name(result[0])
    if result[1] == 1:
        restaurant_id = 19
    elif result[1] == 2:
        restaurant_id = 20
    else:
        restaurant_id = 21
    date = result[2]
    if result[3] == "Breakfast":
        meal = 19
    elif result[3] == "Dinner":
        meal = 21
    else:
        meal = 20
    number_of_guest = result[4]
    special_requests = result[5]

    return first_page+utils.add_reservations(id,restaurant_id,date,meal,number_of_guest,special_requests)

@tool
def add_reservation_by_id(data:str) -> str:
    """
    supprime une reservation. Donne une belle forme a la phrase pour presenter le client.
    :param data:
    :return:
    """
    result = utils.extract_values_six_force(data)
    print(result)
    id = result[0]
    if result[1] == 1:
        restaurant_id = 19
    elif result[1] == 2:
        restaurant_id = 20
    else:
        restaurant_id = 21
    date = result[2]
    if result[3] == "Breakfast":
        meal = 19
    elif result[3] == "Dinner":
        meal = 21
    else:
        meal = 20
    number_of_guest = result[4]
    special_requests = result[5]

    return first_page+utils.add_reservations(id,restaurant_id,date,meal,number_of_guest,special_requests,)

tools = [
    Tool(
        name="Personnaliter",
        func=personnaliter,
        description="Donne la personnaliter de l'ia"
    ),
    Tool(
        name="GetWeather",
        func=get_weather,
        description="Un outil qui récupère la météo d'une ville donnée."
    ),
    Tool(
        name="ListRestaurants",
        func=list_restaurant,
        description="Un outil qui liste les restaurants."
    ),
    Tool(
        name="InfoRestaurant",
        func=info_restaurant,
        description="Un outil qui information du restaurant."
    ),
    Tool(
        name="ListSpa",
        func=list_spa,
        description="Un outil qui liste les spas."
    ),
    Tool(
        name="InfoSpa",
        func=info_spa,
        description="Un outil qui information du spa."
    ),
    Tool(
        name="InfoRepa",
        func=info_meal,
        description="Un outil qui donne la liste des repas."
    ),Tool(
        name="InfoClient",
        func=info_name,
        description="Un outil qui donne des info sur le client par son nom"
    ),
    Tool(
        name="IdClient",
        func=id_name,
        description="Un outil qui donne l'id du client par son nom"
    ),
    Tool(
        name="AddClient",
        func=add_clients,
        description="Un outil qui ajoute un client"
    ),
    Tool(
        name="SearchClientById",
        func=search_client_by_id,
        description="Un outil qui cherche un client par son id"
    ),
    Tool(
        name="ChangeClientName",
        func=modif_client_name,
        description="Un outil qui modifie le nom d'un client"
    ),
    Tool(
        name="ChangeClientPhoneNumber",
        func=modif_client_phone_numbers,
        description="Un outil qui modifie le numero de telephone d'un client"
    ),
    Tool(
        name="ChangeClientRoomNumber",
        func=modif_client_room_numbers,
        description="Un outil qui modifie le numero de chambre d'un client"
    ),
    Tool(
        name="ChangeClientSpecialRequests",
        func=modif_client_special_requests,
        description="Un outil qui modifie la requetes special d'un client"
    ),
    Tool(
        name="DeleteClientById",
        func=del_client_by_id,
        description="Un outil qui supprime un client"
    ),
    Tool(
        name="DeleteClientByName",
        func=del_client_by_name,
        description="Un outil qui supprime un client"
    ),
    Tool(
        name="FindReservationsById",
        func=find_reservation_by_id,
        description="Un outil qui trouve une reservation par son id"
    ),
    Tool(
        name="DeleteReservationById",
        func=del_reservation_by_id,
        description="Un outil qui supprime une reservation par son id"
    ),
    Tool(
        name="AddReservationByName",
        func=add_reservation_by_name,
        description="Un outil qui ajoute une reservation avec son name"
    ),
    Tool(
        name="AddReservationById",
        func=add_reservation_by_id,
        description="Un outil qui ajoute une reservation avec son id"
    ),




]



#Not use but can create .waw vocal in french for IA
def create_voice(text_speech):

    pipeline = KPipeline(lang_code='f')
    generator = pipeline(text_speech, voice='ff_siwis')
    for i, (gs, ps, audio) in enumerate(generator):
        print(i, gs, ps)
        display(Audio(data=audio, rate=24000, autoplay=i == 0))
        sf.write('voice.wav', audio, 24000)

