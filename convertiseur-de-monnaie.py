import json

# Chargement de l'historique des conversions depuis un fichier JSON
def load_conversion_history():
    try:
        with open('conversion_history.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Enregistrement de l'historique des conversions dans un fichier JSON
def save_conversion_history(history):
    with open('conversion_history.json', 'w') as file:
        json.dump(history, file, indent=4)

# Fonction pour effectuer la conversion de devise
def convert_currency(amount, from_currency, to_currency, rates, history):
    if from_currency in rates and to_currency in rates:
        converted_amount = amount * rates[from_currency] / rates[to_currency]
        history[f"{amount} {from_currency} to {to_currency}"] = f"{amount} {from_currency} = {converted_amount} {to_currency}"
        return converted_amount
    else:
        print("La conversion n'est pas possible. Vérifiez les devises saisies.")
        return None

def main():
    conversion_history = load_conversion_history()

    # Taux de conversion
    rates = {
        'USD': 1.0,
        'EUR': 0.85,    # 1 USD = 0.85 EUR
        'GBP': 0.75,    # 1 USD = 0.75 GBP
        'JPY': 110.25,  # 1 USD = 110.25 JPY
        'AUD': 1.35     # 1 USD = 1.35 AUD
    }

    while True:
        print("\n===== Convertisseur de Devises =====")
        print("1. Convertir une somme")
        print("2. Quitter")

        choice = input("Faites votre choix: ")

        if choice == '1':
            amount = float(input("Entrez le montant à convertir: "))
            from_currency = input("Entrez la devise d'origine (par ex. USD, EUR, etc.): ").upper()
            to_currency = input("Entrez la devise cible (par ex. USD, EUR, etc.): ").upper()

            result = convert_currency(amount, from_currency, to_currency, rates, conversion_history)
            if result is not None:
                print(f"{amount} {from_currency} = {result} {to_currency}")
                save_conversion_history(conversion_history)

        elif choice == '2':
            print("Merci d'avoir utilisé le convertisseur de devises.")
            break

        else:
            print("Choix invalide. Veuillez choisir une option valide.")

if __name__ == "__main__":
    main()
