import disnake
from disnake.ext import commands, tasks
from const import user_id, games, log_channel_id, bot_token, guild_id, delay
from funcs import Info, write, change_status

p = Info()
command_sync_flags = commands.CommandSyncFlags.default()
client = commands.Bot(intents=disnake.Intents.all(),
                      command_prefix='/',
                      test_guilds=[guild_id],
                      command_sync_flags=command_sync_flags)


@client.slash_command(name='ping', description='ping')
async def ping(ctx):
    await ctx.send("pong")


@client.slash_command(name='token', description='change auth token')
async def auth_token(inter, token: str):
    if inter.author.id != user_id:
        return
    write('auth_token.txt', token)
    await inter.response.send_message("Done")


@client.slash_command(name='online_status', description='change online status')
async def auth_token(inter, token: str):
    if inter.author.id != user_id:
        return
    write('online_status.txt', token)
    await inter.response.send_message("Done")


@client.slash_command(name='dnd_status', description='change dnd status')
async def auth_token(inter, token: str):
    if inter.author.id != user_id:
        return
    write('dnd_status.txt', token)
    await inter.response.send_message("Done")


@tasks.loop(seconds=delay)
async def main_loop():
    try:
        guild = client.get_guild(guild_id)
        member = guild.get_member(user_id)
        act = member.activities
        try:
            game = act[1].name
            if game in games:
                if p.dnd:
                    if not change_status(0):
                        await client.get_channel(log_channel_id).send('error changing status')
                        return
                    await client.get_channel(log_channel_id).send('dnd successful')
                    p.onl = True
                p.dnd = False
            else:
                if p.onl:
                    if not change_status(1):
                        await client.get_channel(log_channel_id).send('error changing status')
                        return
                    await client.get_channel(log_channel_id).send('online successful')
                    p.dnd = True
                p.onl = False
        except IndexError:
            if p.onl:
                if not change_status(1):
                    await client.get_channel(log_channel_id).send('error changing status')
                    return
                await client.get_channel(log_channel_id).send('online successful')
                p.dnd = True
            p.onl = False
    except Exception as ex:
        await client.get_channel(log_channel_id).send(str(ex))


@main_loop.before_loop
async def before_main_loop():
    await client.wait_until_ready()


@client.event
async def on_ready():
    main_loop.start()


def run():
    client.run(bot_token)


if __name__ == '__main__':
    run()

