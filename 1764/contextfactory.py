from OpenSSL import SSL
from scrapy.core.downloader.contextfactory import ScrapyClientContextFactory


class TLSFlexibleContextFactory(ScrapyClientContextFactory):
    """A more protocol flexible TLS/SSL context factory.

    A TLS/SSL connection established with these methods may understand
    the SSLv3, TLSv1, TLSv1.1 and TLSv1.2 protocols.
    See https://www.openssl.org/docs/manmaster/ssl/SSL_CTX_new.html
    """

    def __init__(self):
        self.method = SSL.SSLv23_METHOD


class SSLv3ContextFactory(ScrapyClientContextFactory):
    def __init__(self):
        self.method = SSL.SSLv3_METHOD


class SSLv2ContextFactory(ScrapyClientContextFactory):
    def __init__(self):
        self.method = SSL.SSLv2_METHOD

class TLSv1ContextFactory(ScrapyClientContextFactory):
    def __init__(self):
        self.method = SSL.TLSv1_METHOD

class TLSv11ContextFactory(ScrapyClientContextFactory):
    def __init__(self):
        self.method = SSL.TLSv1_1_METHOD

class TLSv12ContextFactory(ScrapyClientContextFactory):
    def __init__(self):
        self.method = SSL.TLSv1_2_METHOD
