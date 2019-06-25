# target = "https://ticket2.usj.co.jp/t/tkt/ei.do?t=3743|4157|3823|3840|3760|4182|3902|3913|3814&p=20|20|20|20|20|20|20|20|20&m=2"
target = "https://ticket2.usj.co.jp/t/tkt/ei.do?t=3743|4157|3823|3840|3760|4182|3902|3913&p=20|20|20|20|20|20|20|20&m=2"
new_target = "https://ticket2.usj.co.jp/t/tkt/ei.do?t=4648|4663|4655|4671|4628|4583|4614|4640|4716&p=20|20|20|20|20|20|20|20|20&m=2"
prdUrl = "https://ticket2.usj.co.jp/t/tkt/cartinput.do?t="
apiUrl = "https://ticket2.usj.co.jp/api/ticketinfo.do?ticketcode="


productTitle = {
	"3743":"USJ7 - 스탠다드",	#0
	"4157":"USJ7 - 싱온투어",	#1
	"3823":"USJ7 - 플라잉공룡",	#2
	"3840":"USJ7 - 백드롭",		#3
	"3760":"USJ4 - 스탠다드",	#4
	"4182":"USJ4 - 싱온투어",	#5
	"3902":"USJ4 - 플라잉공룡",	#6
	"3913":"USJ4 - 미니언라이드",	#7
	# "3814":"USJ3 - 스탠다드",	#8
				   }

prdData = {
	'item_0' : {
		'code' : '3743',
		'tct_type' : 'USJ7',
		'prd_type' : '스탠다드',
		'title' : 'USJ7-스탠다드'
	},
	'item_1' : {
		'code' : '4157',
		'code2' : '4628',
		'tct_type' : 'USJ7',
		'prd_type' : '싱온투어',
		'title' : 'USJ7-싱온투어',
	},
	'item_2' : {
		'code' : '3823',
		'code2' : '4583',
		'tct_type' : 'USJ7',
		'prd_type' : '플라잉 공룡',
		'title' : 'USJ7-플라잉 공룡',
	},
	'item_3' : {
		'code' : '3840',
		'code2' : '4614',
		'tct_type' : 'USJ7',
		'prd_type' : '백드롭',
		'title' : 'USJ7-백드롭',
	},
	'item_4' : {
		'code' : '3760',
		'tct_type' : 'USJ4',
		'prd_type' : '스탠다드',
		'title' : 'USJ4-스탠다드',
	},
	'item_5' : {
		'code' : '4182',
		'code2' : '4663',
		'tct_type' : 'USJ4',
		'prd_type' : '싱온투어',
		'title' : 'USJ4-싱온투어',
	},
	'item_6' : {
		'code' : '3902',
		'code2' : '4648',
		'tct_type' : 'USJ4',
		'prd_type' : '플라잉 공룡',
		'title' : 'USJ4-플라잉 공룡',
	},
	'item_7' :{
		'code' : '3913',
		'code2' : '4655',
		'tct_type' : 'USJ4',
		'prd_type' : '미니언라이드',
		'title' : 'USJ4-미니언라이드',
	},
	'item_8':{
		'code' : 'null',
		'code2' : '4671',
		'tct_type' : 'USJ4',
		'prd_type' : '스페이스 판타지 더 라이드',
		'title' : 'USJ4-스페이스 판타지 더 라이드',
	},
	'item_9':{
		'code' : 'null',
		'code2' : '4640',
		'tct_type' : 'USJ7',
		'prd_type' : '스페이스 판타지 더 라이드',
		'title' : 'USJ7-스페이스 판타지 더 라이드',
	}
	#code2 4640 = usj7, 스페이스 판타지 더 라이드
	#code2 4716 = usj3, 스페이스 판타지 더 라이드
}

prdUrl = "https://ticket2.usj.co.jp/t/tkt/cartinput.do?t="




from urllib.request import urlopen, Request
from urllib.error import HTTPError
import urllib.robotparser
import urllib.parse
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
