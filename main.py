import discord, asyncio

token = '' # https://www.youtube.com/watch?v=YEgFvgg7ZPI
reply_message = 'Join discord.gg/ to buy limiteds!' # Message to reply with when somebody DMs the token.
main_message = 'DM if you want to buy limiteds.' # Message to send in the channel.
channel_id = 0000000000000000000 # Channel ID to send the message in.
delay = 300 # In seconds.

dmed_list = []

class Main(discord.Client):
    async def on_ready(self):
        print('Logged in as %s.' % self.user)
        while True:
            channel = self.get_channel(channel_id)
            await channel.send(main_message)
            print('Sent message in #%s.' % channel.name)
            await asyncio.sleep(delay)

    async def on_message(self, message):
        if isinstance(message.channel, discord.DMChannel):
            if message.author.id != self.user.id:
                if message.author.id not in dmed_list:
                    await message.reply(reply_message)
                    print('Replied to %s.' % message.author.name)
                    dmed_list.append(message.author.id)

Main().run(token, bot = False)
