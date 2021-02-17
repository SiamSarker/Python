import requests
import hashlib


# url = 'https://api.pwnedpasswords.com/range/' + 'CBFDA'
# res = requests.get(url)
# print(res)   # 400 is not okay

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + 'CBFDA'
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
    return res


def pwned_api_check(password):
    # check password if it exist in API response
    sha1password = hashlib.sha1(password.encode('utf-8'))
    return sha1password


request_api_data('123')
