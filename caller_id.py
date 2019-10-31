from bs4 import BeautifulSoup as bsoup
from requests import post,get

def main():
    url='https://mbasic.facebook.com/login/identify/?ctx=recover&search_attempts=1'
    data = {'email': input('Enter e-Mail or Phone: ')}
    a = post(url,data = data,headers = {'Cookie':'locale=en_GB'})
    if not a.ok:
        print('Error making connection... Try again')
        return
    r = bsoup(a.content,'lxml')
    temp = r.findAll('strong')
    res = []
    for i in temp:
        c = i.contents[0]
        if c.isnumeric():
                continue
        res.append(c)
    res = '\n'.join(res)
    print(res if res else 'Not Found')

if __name__ == '__main__':
    main()
