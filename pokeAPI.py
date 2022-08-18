import requests

def get_pokemon(url= 'https://pokeapi.co/api/v2/pokemon-form/', offset = 0):
    args = {'offset':offset} if offset else {}
    #esto sucede siempre que no sea un dic vacio

    response = requests.get(url, params=args)

    if response.status_code == 200:

            payload = response.json()#carga el json
            results = payload.get('results', [])

            if results:
                for pokemon in results:
                    name = pokemon ['name']
                    print(name)  

            next = input("Continuar listando? [Y/n]").lower()
            #opcion por consola para continuar mostrando
            if next == 'y':
                get_pokemon(offset=offset+20)
                #juega con el offset de la url para mostrar 20 mas

if __name__ == '__main__':
    url = 'https://pokeapi.co/api/v2/pokemon-form/'
    get_pokemon()
    