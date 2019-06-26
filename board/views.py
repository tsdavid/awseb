from django.shortcuts import render


"""WORKING FUCTION WITH DEF USJ"""
#
# from ..board.dk_function.usj.data.urls import *
# # from ..board.dk_function.usj.data.productTitle import *
# from ..board.dk_function.usj.function.rebuild_fct import *
#
# import datetime,calendar, json
# def usj():
# 	# 7월 12일 이후 상품
#
# 	data = {}
# 	for key in prdData.keys():
# 		st = prdData[key]
# 		if len(st) <= 4: pass
# 		try:
# 			data[st['code2']] = json.loads(download(apiUrl + st['code2']))
# 		except:
# 			pass
#
# 	"""
# 	1. 각 코드(4628..) 별로 moth 데이터를 가지고온다.
# 	2. moth 데이터의 끝 자락까지 늘려서 price_dic에 저장한다.
# 		2-1. 각 month의 마지막 날을 가져와야 함 -> https://stackoverflow.com/questions/42950/get-last-day-of-the-month-in-python
# 	3. dic에 상품코드, 일본 상품명, 그리고 늘린 날짜 정보를 넣는다.
# 	4. 가지고온 가격 정보와 날짜 정보가 맞는 정보 == price data inser / !=  == 매진
# 	"""
# 	send_list = []
# 	now = datetime.datetime.now()
# 	today = dateformatter(now.year, now.month, now.day)
# 	send_dic = {}
# 	"""1. 각 코드별로 month 데이터를 가지고 온다"""
# 	for par_key in data.keys():
# 		japn_name = data[par_key]['name']
# 		ticketcode = data[par_key]['ticketcode']
# 		obj = data[par_key]['calendar']
#
# 		m = []
# 		for o in obj: m.append(o['month'])  # 가격 정보가 올라가 월 정보를 저장
# 		m = list(set(m))
# 		m.sort()
#
# 		"""2. month 데이터의 끝 자락 까지 늘려서 price_dic에 저장한다."""
# 		dic = {}
# 		for i in m:
# 			dic[i] = calendar.monthrange(now.year, int(i))[-1]  # 각 월의 마지막 날을 dic에 저장
#
# 		price_dic = {}
# 		# 날짜를 늘려야지
# 		for key in dic.keys():
# 			for i in range(dic[key]):  # 각 월의 일 수를 늘린다음에
# 				y_m_d = dateformatter(now.year, key, i + 1)  # 날짜 데이터 형식으로 저장하고
# 				price_dic[y_m_d] = '매진'  # 모두 매진이라 표기한 뒤 저장한다.
#
# 		# 가격을 가지고 오자
# 		lastest_day = dateformatter(obj[-1]['year'], obj[-1]['month'], obj[-1]['date'])
#
# 		for o in obj:
# 			ymd = dateformatter(o['year'], o['month'], o['date'])
# 			price = o['price1value']
# 			for key, value in price_dic.items():
# 				if lastest_day < key:
# 					price_dic[key] = "No Given"  # 마지막날 이후 나온 값 없음
# 				elif today > key:
# 					price_dic[key] = "Gone"  # 이전 데이터 없기
# 				elif ymd == key:
# 					price_dic[key] = price  # 가격 정보 넣기
#
# 		send_dic['ProductTitle'] = title_by_code(ticketcode)
# 		send_dic['ProductUrl'] = prdUrl + str(ticketcode)
# 		send_dic['JAPAN'] = japn_name
# 		send_dic['price_data'] = price_dic
#
#
# 		send_data(send_dic, ipack_post=True)
#

# Create your views here.
def index(request):
	return render(request, 'board/index.html')

# from packer.usj.worker import usj

from usj.worker import *
def run(request):
	if request.method == 'POST' and 'run_script' in request.POST:
		usj()
		return render(request, 'board/cool.html')
	else:
		return render(request, 'board/run.html')

def run2(request):
	if request.method == 'POST' and 'run_script' in request.POST:
		from selenium import webdriver
		from pyvirtualdisplay import Display

		with Display():
			bw = webdriver.Firefox()
			try:
				bw.get("http://www.google.com")
				print(bw.title)
			finally:
				bw.quit()
		return request(request, 'board/run2.html')
	else:
		return render(request, 'board/run2.html')