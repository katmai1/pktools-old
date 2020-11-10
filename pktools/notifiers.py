import requests
import json
from discord_webhook import DiscordEmbed, DiscordWebhook


# ────────────────────────────────────────────────────────────────────────────────


def sendDiscordWebhook(url, title, message, color='default'):
    """Send messages to discord using webhook

    Args:
        url (str): Webhook URL
        title (str): Title of message
        message (str): Content of message
        color (str, optional): Color of message, list: 'red', 'green' or 'default'. Defaults to 'default'.

    Returns:
        list: Webhook response
    """
    color_list = {'green': 89092, 'red': 8394756, 'default': 242424}
    webhook = DiscordWebhook(url=url)
    embed = DiscordEmbed(title=title, description=message, color=color_list[color])
    webhook.add_embed(embed)
    return webhook.execute()

# ────────────────────────────────────────────────────────────────────────────────


def sendPushbullet(private_key, title, message):
    msg = {"type": "note", "title": title, "body": message}
    TOKEN = private_key
    resp = requests.post('https://api.pushbullet.com/v2/pushes',
                         data=json.dumps(msg),
                         headers={'Authorization': 'Bearer ' + TOKEN,
                                  'Content-Type': 'application/json'})
    if resp.status_code != 200:
        raise Exception('Error', resp.status_code)
    else:
        print('Message sent')

# ────────────────────────────────────────────────────────────────────────────────
