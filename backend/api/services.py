import re
import random
import string
import logging
from datetime import datetime, timedelta
from dataclasses import dataclass
from api.quotes import QUOTES, TRIGGER_WORDS

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# timeout (in seconds) before re-using the same quote
QUOTE_REUSE_TIMEOUT = 15


@dataclass
class TokenizeTextService:
    """Given a string "text" tokenize it and make it lower case so it's easier to search for trigger words"""

    text: str = ""

    def call(self):
        regex = re.compile("[%s]" % re.escape(string.punctuation))
        text = regex.sub("", self.text)
        tokens = [t.strip().lower() for t in text.split()]
        return list(filter(None, tokens))


@dataclass
class GetQuoteService:
    text: str = ""

    def call(self):
        if not self.text:
            return ""

        tokenized_text = TokenizeTextService(self.text).call()
        intersection = set(TRIGGER_WORDS).intersection(tokenized_text)
        if not intersection:
            logger.info(f'No quote found for "{self.text}"')
            return ""

        word = random.choice(list(intersection))
        trigger_word = TRIGGER_WORDS.get(word)

        quote_id = random.choice(trigger_word.get("quotes"))
        quote = QUOTES.get(quote_id)
        last_used_at = trigger_word.get("last_used_at")
        if last_used_at + timedelta(seconds=QUOTE_REUSE_TIMEOUT) > datetime.now():
            logger.info(
                f'⚠️  Skipping quote for "{word}", last used {last_used_at}. It will be '
                f'available in around {QUOTE_REUSE_TIMEOUT} seconds.'
            )
            return ""

        trigger_word.update({"last_used_at": datetime.now()})
        logger.info(f'✅ Found quote for "{word}" = "{quote}"')
        return quote
