import emoji

# Loop for the correct answer
while True:

        # Avoid errors
        try:

            text = input("Input: ")
            e = emoji.emojize(text, language='alias')

            # Avoid wrong input
            if e != text:
                 print(e)
                 break



        except Exception:
            print("its not true")
