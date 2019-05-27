# http://quotes.toscrape.com
import requests
from bs4 import BeautifulSoup
from random import choice

response = requests.get("http://quotes.toscrape.com")
soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all(class_="quote")
data = []
for quote in quotes:
	q = quote.find(class_="text").get_text()
	author = quote.find(class_="author").get_text()
	link = quote.find("a")["href"]
	# print(link)
	data.append([q, author, link])

# print(data)

curr_quote = choice(data)
guesses = 4
print(f"Here's a quote: \n\n{curr_quote[0]}")
user = input(f"\nWho said this? Guesses remaining: {guesses}. ")
play = ""
while True:
	if user == curr_quote[1]:
		print("You guessed correctly! Congratulations!")
		play = input("\nWould you like to play again (y/n)? ")
	else:
		res2 = requests.get(f"http://quotes.toscrape.com{curr_quote[2]}")
		soup = BeautifulSoup(res2.text, "html.parser")
		guesses -= 1
		if guesses == 3:
			hint = soup.select(".author-born-date")[0].get_text() + " " + soup.select(".author-born-location")[0].get_text()
			print(f"Here's a hint: The author was born in {hint}")
			user = input(f"\nWho said this? Guesses remaining: {guesses}. ")
		elif guesses == 2:
			hint = curr_quote[1][0]
			print(f"Here's a hint: The author's first name starts with {hint}")
			user = input(f"\nWho said this? Guesses remaining: {guesses}. ")
		elif guesses == 1:
			hint = curr_quote[1].split(" ")[1][0]
			print(f"Here's a hint: The author's last name starts with {hint}")
			user = input(f"\nWho said this? Guesses remaining: {guesses}. ")
		else:
			print(f"Sorry, you've run out of guesses. The answer was {curr_quote[1]}")
			play = input("\nWould you like to play again (y/n)? ")
	if play == "y":
		play = ""
		new_quote = choice(data)
		while new_quote == curr_quote: new_quote = choice(data)
		curr_quote = new_quote
		guesses = 4
		print("Great! Here we go again...\n")
		print(f"Here's a quote: \n\n{curr_quote[0]}")
		user = input(f"\nWho said this? Guesses remaining: {guesses}. ")
	elif play == "n":
		print("Ok! See you next time!")
		break