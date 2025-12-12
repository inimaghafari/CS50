import re

def main():
    ip = input("IPv4 Address: ")
    if validate(ip):
        print("True")
    else:
        print("False")

# Check the ip
def validate(ip):

    pattern = r"^(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})\." \
              r"(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})\." \
              r"(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})\." \
              r"(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})$"

    return bool(re.match(pattern, ip))


if __name__ == "__main__":
    main()
