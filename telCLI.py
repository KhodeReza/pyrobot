from pyrogram import Client, Filters
app = Client(
                       "Alireza_Robix",
                       api_id=835783,
                       api_hash="9e4227377ab40e080740e59eb48d6a12"
                              )
@app.on_message(Filters.group)
def wlc(client, message):
    message.reply_text("Salam {} 😃".format(message.from_user.first_name))


app.run()