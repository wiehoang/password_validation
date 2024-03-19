# Implement a URL shortener with the following methods:
# `shorten(url)`, which shortens the url into a six-character alphanumeric string, such as `zLg6wl`.
# `restore(short)`, which expands the shortened string into the original url. If no such shortened string exists, return null.
# Hint: What if we enter the same URL twice?


class URLShortener:
    def __init__(self):
        self.url_mapping = {}  # Store link has been shortened
        self.base62 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        self.uid = 0


    def ShortenLink(self):
        original_url = input('Paste a link: ')
        self.uid = len(self.url_mapping) + 1  # Incrementally increase by 1 to create a unique shorten link
        base_url = 'https://sef.vn/'  # Enter a domain
        shorten_str = self.UIDtoShortenStr()
        shorten_url = base_url + shorten_str
        self.url_mapping[shorten_str] = original_url
        print(f'Your shorten link is: {shorten_url}')


    def RestoreLink(self, shorten_str):
        get_original_url = self.url_mapping.get(shorten_str)
        if get_original_url is not None:
            return print(f'Your original link is: {get_original_url}')
        else:
            return print(f'Can\'t find your original link!')


    def UIDtoShortenStr(self):
        shorten_str = ''

        # Match an uid with base62 index
        while self.uid > 0:
            remain = self.uid % 62
            shorten_str += self.base62[remain]
            self.uid //= 62

        # Limit a shorten string in six-character only
        if len(shorten_str) < 6:  # Add '0' if shorten string < 6
            shorten_str += '0' * (6 - len(shorten_str))
        elif len(shorten_str) > 6:  # Slice if shorten string > 6
            shorten_str = shorten_str[:6]
        return shorten_str


urlshortener = URLShortener()
urlshortener.ShortenLink()
urlshortener.RestoreLink('b00000')
