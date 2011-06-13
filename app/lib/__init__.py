import mechanize
import settings

def get_etherpad_url():
    br = mechanize.Browser()
    o = br.open("http://%s/ep/pad/newpad" % settings.ETHERPAD_DOMAIN)
    forms = mechanize.ParseResponse(o, backwards_compat=False)
    data = mechanize.urlopen(forms[0].click()).read()
    return mechanize.urlopen(forms[0].click()).geturl()