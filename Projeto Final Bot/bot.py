import discord
import requests
import io

def get_meme():
    response = requests.get("https://meme-api.com/gimme")

    if response.status_code == 200:
        data = response.json()
        return data["url"]

    return None


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"Bot conectado como {client.user}")


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith("$meme"):

        meme_url = get_meme()

        if meme_url:
            imagem = requests.get(meme_url)

            if imagem.status_code == 200:
                arquivo = discord.File(
                    io.BytesIO(imagem.content),
                    filename="meme.jpg"
                )

                await message.channel.send(file=arquivo)

            else:
                await message.channel.send(
                    "Não consegui baixar o meme 😢"
                )

        else:
            await message.channel.send(
                "Não consegui encontrar um meme 😢"
            )


client.run("MTU0ODM2NDI0NDIzMDM0ODkyMA.GFSVbn.zMxd-Bx_U7NVs-KL-1sDLDdZv9u1Z49y6vcVQk")