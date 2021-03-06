import wolframalpha
from configuration import config


def calc(update, context):
    """Calculate anything using wolframalpha"""
    message = update.message
    query = ' '.join(context.args)

    if not query:
        text = "*Usage:* `/calc {QUERY}`\n"\
               "*Example:* `/calc 1 cherry to grams`"
    else:
        client = wolframalpha.Client(config["WOLFRAM_APP_ID"])
        result = client.query(query)

        if result.success == 'true':
            text = next(result.results).text
        else:
            text = "Invalid query"

    message.reply_text(text=text)
