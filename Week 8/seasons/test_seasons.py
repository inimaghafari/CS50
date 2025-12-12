from datetime import date, datetime
import sys
import inflect

def birth(birthday_inp=None, today=None):
    num2word = inflect.engine()

    if birthday_inp is None:
        birthday_inp = input("Give me your birthday: ")

    try:
        birthday = datetime.strptime(birthday_inp, "%Y-%m-%d").date()
    except Exception:
        sys.exit("Invalid date")

    if today is None:
        today = date.today()

    age = today - birthday
    age_minutes = age.days * 24 * 60

    return num2word.number_to_words(age_minutes, andword="").capitalize()

def main():
    result = birth()
    print(f"{result} minutes")


if __name__ == "__main__":
    main()
