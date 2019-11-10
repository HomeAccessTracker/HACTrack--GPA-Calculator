import requests

def connect(user_name, pass_word):
    header = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    }
    
    login_data = {
        'SCKTY00328510CustomEnabled' : 'False',
        'Database' : '10',
        'LogOnDetails.UserName' : user_name,
        'LogOnDetails.Password' : pass_word
    }

    with requests.Session() as c:
        url = 'https://lis-hac.eschoolplus.powerschool.com/HomeAccess/Account/LogOn?ReturnUrl=%2fHomeAccess'
        c.get(url)
        c.post(url, data = login_data, headers = header)
        page = c.get('https://lis-hac.eschoolplus.powerschool.com/HomeAccess/Home/WeekView')
        return page
