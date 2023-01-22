from discord_webhook import DiscordWebhook
# from seleniumwire import webdriver
from discord_webhook import DiscordEmbed
import requests
def send_webhook( ):

    # print("debugging victory " + suffix)

    webhook = DiscordWebhook(
        url="https://discord.com/api/webhooks/1061735267129626736/wEx2wkOvqqDl1jJw7vggtSSPbDg_F7tqPx-YxTPBbVdtnrF6cQ6JbcZMvy1TTZSu-qPM")
    embed = DiscordEmbed(title='ChatGPT Amazon Product Sourced!',  color='03b2f8')
    embed.add_embed_field(name='Amazon Link', value='test')
    embed.add_embed_field(name='Product Link', value='test')
    embed.add_embed_field(name= 'Source Store', value = 'test')
    embed.add_embed_field(name='ASIN', value='test')
    embed.add_embed_field(name='Sales Rank', value= 'test')
    embed.add_embed_field(name = 'ROI', value = "100%")


    # add embed object to webhook
    webhook.add_embed(embed)

    response = webhook.execute()



send_webhook()