import requests
def connect(user_name, pass_word):
    header = {
        'User-Agent' : 'Chrome/76.0.3809.100'
    }
  with requests.Session() as c:
        url = 'https://lis-hac.eschoolplus.powerschool.com/HomeAccess/Account/LogOn?ReturnUrl=%2fHomeAccess'
        c.get(url)
