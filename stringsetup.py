from telethon.sessions import StringSession
from telethon.sync import TelegramClient

print("""
T E A M    MORPHO B O T   ! !
""")
print("Hello!! Welcome to MorphoBot Session Generator\n")
okvai = input("Enter 47 to continue: ")
if okvai == "47":
	print(
	    "\nPlease go to my.telegram.org and get your API Id and API Hash to proceed.\n"
	)
	APP_ID = int(input("\nEnter APP ID here: "))
	API_HASH = input("\nEnter API HASH here: ")

	with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
		print(
		    "\nYour MorphoBot Session Is sent in your Telegram Saved Messages.")
		client.send_message("me", client.session.save())
		client.send_message(
		    "me",
		    "Above is your #MorphoBOT_SESSION \nPaste this string in Heroku Var.\n\n[Team morphoBot](t.me/morpho_user)"
		)

else:
	print("Bhag jaa Bc = be careful 😂")
