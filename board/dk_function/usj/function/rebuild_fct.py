from urllib.request import urlopen, Request
from urllib.error import HTTPError
import urllib.robotparser
import urllib.parse
from packer.board.dk_function.usj.data.productTitle import *
from datetime import date
from urllib.parse import urlencode
from urllib.request import Request, urlopen

def download(url, headers=None, user_agent='wswp', proxy=None, num_retries=2):
	print('Downloading: ', url)
	headers = {'User-agent': user_agent}
	request = Request(url, headers=headers)
	opener = urllib.request.build_opener()
	if proxy:
		proxy_params = {urllib.request.urlparse(url).scheme:proxy}
		opener.add_handler(urllib.request.ProxyHandler(proxy_params))
	try:
		html = urlopen(request).read().decode('utf-8')
	except HTTPError as e:
		print("Download error: ", e.reason)
		html = None
		if num_retries >0 :
			if hasattr(e, 'code') and 500 <= e.code < 600:
				# 5XX HTTP 오류 시 재시도
				return download(url, num_retries -1)
	return html

"""Action functions"""
def title_by_code(code, value = 'code2'):
	for key in prdData.keys():
		try:
			if str(code) == prdData[key][value]:
				obj = prdData[key]['title']
		except:pass
	return obj


def dateformatter(year,month,day):
	"""date time formater -> 함수화 진행"""
	date_string = str(year) + "-" + str(month) + "-" + str(day)
	date_time = date(*map(int, date_string.split('-'))).isoformat()
	return date_time

def postData(data):
	""" post section"""
	url = "http://ipacktour.com/test/python"
	post_fields = data  # PARAMS
	request = Request(url, urlencode(post_fields).encode())
	json = urlopen(request).read().decode()
	print(json)


def send_data(target_data, ipack_post, text_data=None, telegram_post=False):
    if ipack_post == False:  # 만약에 ipack_post가 False 라면
        pass  # ipack에 post할 그릇에 저장된 데이터를 ipack에 post 를 안한다
    elif ipack_post == True:
        postData(target_data)  # ipack에 post할 그릇에 저장된 데이터를 ipack에 post 한다

    if telegram_post == True:  # 만역에 telegram_post 가 True라면
        try:
            print(text_data)
            #ge_fc.sendTelegram(text_data)  # telegram에 post한다
        except IndexError as e:
            pass
    elif telegram_post == False:  # 만역에 telegram_post 가 False라면
        pass  # telegram에 post를 안한다.
