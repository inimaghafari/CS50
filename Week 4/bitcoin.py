import sys
import requests

def main():

    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")


    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")


    try:
        api_key = "8b25adbced1c30a63b662c1bb385246b80ad26692f4bb60668978efa6767e597"
        url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}"
        r = requests.get(url)

        if r.status_code != 200:
            sys.exit("Error: request failed!")

        data = r.json()
        price = float(data["data"]["priceUsd"])

    except Exception:
        sys.exit("Error: request failed!")

    total = n * price

    print(f"${total:,.4f}")


if __name__ == "__main__":
    main()
