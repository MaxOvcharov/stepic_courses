
""" This script gets the currency rate against the ruble """
import re
import requests

def get_currency(lst_currency):
    """ 
        Gets the currency rate against the ruble
        from this URL - http://www.cbr.ru/scripts/XML_daily.asp
    """
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    # Check the len of currency list
    if len(lst_currency) == 0:
        raise ValueError("You haven't entered currency name")
    s = requests.Session()
    r = s.get(url)
    find_str = r.text.encode('utf-8')
    find_str = find_str.strip().split('<Valute ID=')
    find_str = find_str[1:]
    # Gets values of currency
    for curr in lst_currency:
        curr = curr.upper()
        find = False
        for value in find_str:
            if curr in value:
                res = re.findall(r'<Value>[0-9,]+', value)
                out = res[0].split(">")
                find = True
                print "1 %s = %s RUB" % (curr, out[1])
        if not find:
            print "We can't find this currency: %s" % (curr)

    return True

if __name__ == "__main__":
    # Enter name of currency
    currency = raw_input('Enter currency here (like: USD EUR) -> ').split(' ')
    # Remove all empty values
    c = [x for x in currency if len(x) > 0]
    get_currency(c)