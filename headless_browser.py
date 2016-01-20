import mechanize
from mechanize import Browser


HEADERS = [('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:18.0) Gecko/20100101 Firefox/18.0'),
           ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
           ('Accept-Language', 'en-US,en;q=0.5'),
           ('Accept-Encoding', 'gzip, deflate'),
           ('Connection', 'keep-alive'),
           ('Cache-Control', 'max-age=0'), ]


def create_browser(debug=False):
    browser = Browser(factory=mechanize.RobustFactory())
    if debug:
        # Maybe enable this if you want even more spam...
        # logger = logging.getLogger("mechanize")
        # logger.addHandler(logging.StreamHandler(sys.stdout))
        # logger.setLevel(logging.DEBUG)
        browser.set_debug_http(True)
        browser.set_debug_responses(True)
        browser.set_debug_redirects(True)
    browser.set_handle_equiv(True)
    browser.set_handle_gzip(True)
    browser.set_handle_redirect(True)
    browser.set_handle_referer(True)
    browser.set_handle_robots(False)
    browser.addheaders = HEADERS
    return browser