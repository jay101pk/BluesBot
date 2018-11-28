import discord
import asyncio
from spotify_plugin import bot_plugin

song_queue = {}
spotify_object = bot_plugin()
class Event_Message:
    async def message_recieved(self, client, message):
        if message.content.startswith('!hello'):
            await self.message_hello(client, message)

        if message.content.startswith('!play'):
            await self.message_play(client, message)

        if message.content.startswith('!queue'):
            await self.message_queue(client, message)

        if message.content.startswith('!join'):
            await self.join(client, message)
        
        if message.content.startswith('!help'):
            await self.message_help(client, message)

    async def message_hello(self, client, message):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    async def message_play(self, client, message):
        album_artist= message.content.replace("!play ", "")
        album, artist = album_artist.split(",")
        import pdb; pdb.set_trace()
        album = album.strip()
        artist = artist.strip()
        album_info = spotify_object.get_album(album, artist)
        song_queue[message.content[5:]] =  album_info
        msg = '"' + message.content[5:] + '" has been added to the song queue'
        await client.send_message(message.channel, msg)

    async def message_queue(self, client, message):
        index = 1
        msg = 'The current song queue is:'
        for key in song_queue:
            msg += '\n ' + str(index) + '. ' + key
            index += 1

        await client.send_message(message.channel, msg)

    async def join(self, client, message):
        channel = client.get_channel('501955815222149154')
        await client.join_voice_channel(channel)

    async def help(self, client, message):
        message = "!play - plays an album. input is as \"!play album,artist\""
        message = message + "\n!queue - returns the music queue"
        message = message + "\n!join - joins the general channel\n!hello - says hello back"
        await client.send_message(message.channel, message)
