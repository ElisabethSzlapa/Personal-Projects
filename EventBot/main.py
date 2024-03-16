import discord
import asyncio

intents = discord.Intents.all()
intents.reactions = True
intents.members = True
intents.guilds = True

client = discord.Client(intents=intents)

# Define the specific game you want to track
TARGET_GAME = "Minecraft"
# Discord specific token
TOKEN = "example"
# Specific client channel
channel = client.get_channel("example")

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    client.loop.create_task(check_member_games())


@client.event
async def on_member_update(before, after):
    if after.activity is not None and after.activity.name == TARGET_GAME:
        # Notify the server that the member is playing the specific game

        await channel.send(f"{after.display_name} is now crabbing") # server is crab themed 


def craft_status(member):
    print(member)
    for activity in member.activities:
        if activity.name == TARGET_GAME:
            return True
    return False


def on_and_active(member):
    return member.status != "offline" and member.activity is not None


async def check_member_games():
    already_on = []
    while True:
        for guild in client.guilds:
            for member in guild.members:

                if on_and_active(member) and (member not in already_on) and craft_status(member):
                    # Notify the server that the member is playing the specific game
                    already_on.append(member)
                    # we know they're online, no more notif
                    print(already_on)
                    await channel.send(f"{member.display_name} is crabbing")

        for member in already_on: # did a member go offline?
            if member.status == "offline" or member.activity is None:
                await channel.send(f"{member.display_name} has exited crab city")
                already_on.remove(member)
            elif not craft_status(member):
                await channel.send(f"{member.display_name} has exited crab city")
                already_on.remove(member)

        # Wait for 60 seconds before checking again
        await asyncio.sleep(60)
client.run(TOKEN)
