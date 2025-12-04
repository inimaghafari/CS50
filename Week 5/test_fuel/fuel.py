def main():
    fraction = input("Give me fuel: ")
    percentage = convert(fraction)
    print(gauge(percentage))



def convert(fraction):

    x, y = fraction.split("/")
    x = int(x)
    y = int(y)

    if y == 0:
        raise ZeroDivisionError("Denominator cannot be zero")
    if x > y:
        raise ValueError("Numerator cannot be greater than denominator")
    if x < 0 or y < 0:
        raise ValueError("Numbers must be non-negative")

    percentage = round(x / y * 100)
    return percentage




def gauge(percentage):
    if percentage <= 1:
        return("E")
    elif percentage >= 99:
       return("F")
    else:
        return(f"{percentage}%")



if __name__ == "__main__":
    main()
