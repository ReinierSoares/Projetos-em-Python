import requests


def ability(poke):
    print(f"As Habilidades do {pokemon.title()} são: ")

    for i in poke['abilities']:
        print(i['ability']['name'])


def main():
    global pokemon
    pokemon = input('Digite o nome do pokemon: ').lower()
    api = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    res = requests.get(api)

    poke = res.json()
    print(poke)
    # ability(poke)


if __name__ == "__main__":

    main()
