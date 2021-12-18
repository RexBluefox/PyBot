async def on_message_delete(self, message):
        await message.channel.send("Why was '" + message.content + "' deleted? What was wrong with that message?")
        print(message.content + " was deleted!")
