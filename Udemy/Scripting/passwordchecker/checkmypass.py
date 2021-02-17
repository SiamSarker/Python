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


# def read_res(response):
#     print(response.text)


def get_password_leaks_count(hashes, hash_to_check):
    hashes =  (line.split(':') for line in hashes.text.splitlines())
    print(hashes)
    for h, count in hashes:
        print(h, count)


def pwned_api_check(password):
    # check password if it exist in API response
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    print(response)
    return get_password_leaks_count(response, tail)


pwned_api_check('123')
