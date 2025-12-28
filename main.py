import requests

def buscar(url):
    resposta = requests.get(url, timeout=5)
    resposta.raise_for_status()
    return resposta.json()

while True:
    nome = input("Digite um nome (ou 'sair'): ").strip().lower()

    if nome == "sair":
        print("Programa encerrado!")
        break

    try:
        idade_dados = buscar(f"https://api.agify.io/?name={nome}")
        genero_dados = buscar(f"https://api.genderize.io/?name={nome}")
        pais_dados = buscar(f"https://api.nationalize.io/?name={nome}")

        print(f"\n📊 RELATÓRIO DO NOME: {nome.capitalize()}\n")

        # Idade
        if idade_dados["age"] is None:
            print("🔹 Idade estimada: não disponível")
        else:
            print(f"🔹 Idade estimada: {idade_dados['age']} anos")

        # Gênero
        if genero_dados["gender"] is None:
            print("🔹 Gênero provável: não disponível")
        else:
            prob = int(genero_dados["probability"] * 100)
            genero = "Homem" if genero_dados["gender"] == "male" else "Mulher"
            print(f"🔹 Gênero provável: {genero} ({prob}%)")

        # País
        if pais_dados["country"]:
            pais = pais_dados["country"][0]
            print(
                f"🔹 País mais provável: {pais['country_id']} "
                f"({pais['probability']*100:.1f}%)"
            )
        else:
            print("🔹 País mais provável: não disponível")

        print("\nFonte: Agify / Genderize / Nationalize")
        print("-" * 30)

    except requests.exceptions.RequestException as erro:
        print("Erro ao acessar a API:", erro)
        