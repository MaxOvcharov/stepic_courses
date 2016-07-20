""" Login validator """
import re


def check_login(login):
    """ This function checks an login on the following conditions:
        1) Check login using a regular expression;
        2) Check len of login < 1 and login < 21;
        3) Check the prohibited symbol in login;
        4) Check login ends on latin letter or number;
    """

    # Check len of login < 1 or login < 21
    if (len(login) < 1) or (len(login) > 20):
        raise ValueError('Login len out of range (1-20)')

    # Check login using a regular expression
    res = re.match(r'^([a-zA-z0-9.-]+)$', login)

    if not res:
        raise ValueError("Bad syntax of entered login")

    # Check login ends on latin letter or number
    if login.endswith(".") or login.endswith("-"):
        raise ValueError("Login can not ends on '.' or '-'")

    return True

if __name__ == '__main__':
    # Enter your login
    put_login = raw_input('Enter login here -> ')
    # Start checking login
    if check_login(put_login):
        print "This is correct login: ", put_login
