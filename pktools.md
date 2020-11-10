# Table of Contents

* [pktools](#pktools)
* [pktools.generic](#pktools.generic)
  * [simpleCountdown](#pktools.generic.simpleCountdown)
  * [getPriceCryptoCurrency](#pktools.generic.getPriceCryptoCurrency)
* [pktools.notifiers](#pktools.notifiers)
  * [discordWebhook](#pktools.notifiers.discordWebhook)

<a name="pktools"></a>
# pktools

<a name="pktools.generic"></a>
# pktools.generic

<a name="pktools.generic.simpleCountdown"></a>
#### simpleCountdown

```python
simpleCountdown(seconds, message="Waiting...")
```

Simple countdown with message

**Arguments**:

- `seconds` _int_ - Duration of countdown in seconds
- `message` _str, optional_ - Message of countdown. Defaults to "Waiting...".

<a name="pktools.generic.getPriceCryptoCurrency"></a>
#### getPriceCryptoCurrency

```python
getPriceCryptoCurrency(pair, exchange="binance", price="last")
```

Return price of a cryptocurrency

**Arguments**:

- `pair` _str_ - Pair to use. Example: 'BTC/USDT'
- `exchange` _str, optional_ - Name of exchange. Defaults to "binance".
- `price` _str, optional_ - Price returned (last, bid or ask). Defaults to "last".
  

**Returns**:

- `float` - Price returned

<a name="pktools.notifiers"></a>
# pktools.notifiers

<a name="pktools.notifiers.discordWebhook"></a>
#### discordWebhook

```python
discordWebhook(url, title, message, color='default')
```

Send messages to discord using webhook

**Arguments**:

- `url` _str_ - Webhook URL
- `title` _str_ - Title of message
- `message` _str_ - Content of message
- `color` _str, optional_ - Color of message, list: 'red', 'green' or 'default'. Defaults to 'default'.
  

**Returns**:

- `list` - Webhook response

