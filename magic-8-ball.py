import sys, random, time
print("Welcome to Magic 8-ball.")
print("Please say a yes-no question.\n")

result = ["It is certain", "It is decidedly so", "Without a doubt",
          "Yes definitely", "You may rely on it", "As I see it, yes",
          "Most likely", "Outlook good", "Yes", "Signs point to yes",
          "Reply hazy try again", "Ask again later",
          "Better not tell you now", "Cannot predict now",
          "Concentrate and ask again", "Don't count on it",
          "My reply is no", "My sources say no",
          "Outlook not so good", "Very doubtful"]

time.sleep(10)
ready = input('Ready? Y/N ').upper()
if ready == 'Y':
    show = random.randrange(1, len(result))
    print(result[show])
else:
    sys.exit()
