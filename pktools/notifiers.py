from discord_webhook import DiscordEmbed, DiscordWebhook


def discordWebhook(url, title, message, color='default'):
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
