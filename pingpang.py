import requests
import json
import xlwt
from bs4 import BeautifulSoup
 
def getData(page, news):
    headers = {
        "Host": "interface.sina.cn",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0",
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Referer": r"https://search.sina.com.cn/?q=%E9%87%91%E8%9E%8D%E8%B4%A2%E6%8A%A5&c=news&from=channel&ie=utf-8",
        "Cookie": "ustat=__172.16.93.31_1580710312_0.68442000; genTime=1580710312; vt=99; Apache=9855012519393.69.1585552043971; SINAGLOBAL=9855012519393.69.1585552043971; ULV=1585552043972:1:1:1:9855012519393.69.1585552043971:; historyRecord={'href':'https://news.sina.cn/','refer':'https://sina.cn/'}; SMART=0; dfz_loc=gd-default",
        "TE": "Trailers"
    }
 
    params = {
        "t":"",
        "q":"金融财报",
        "pf":"0",
        "ps":"0",
        "page":"1",
        "stime":"2019-03-30",
        "etime":"2020-03-31",
        "sort":"rel",
        "highlight":page,
        "num":"10",
        "ie":"utf-8"
    }
 
    response = requests.get("https://interface.sina.cn/homepage/search.d.json?", params=params, headers=headers)
    dic = json.loads(response.text)
    news += dic["result"]["list"]
 
    return news
 
 
def writeData(news):
    workbook = xlwt.Workbook(encoding = 'utf-8')
    worksheet = workbook.add_sheet('MySheet')
 
    worksheet.write(0, 0, "标题")
    worksheet.write(0, 1, "时间")
    worksheet.write(0, 2, "媒体")
    worksheet.write(0, 3, "网址")
    worksheet.write(0, 4, "正文")
 
    for i in range(len(news)):
        #print(news[i])
        worksheet.write(i+1, 0, news[i]["origin_title"])
        worksheet.write(i+1, 1, news[i]["datetime"])
        worksheet.write(i+1, 2, news[i]["media"])
        worksheet.write(i+1, 3, news[i]["url"])
        html = requests.get(news[i]["url"]).content
        soup = BeautifulSoup(html,'xlml')
        worksheet.write(i + 1,	4,	soup.text)
 
    workbook.save('D:/test/data.xls')
 
 
def main():
    news = []
    for i in range(1,501):
        news = getData(i, news)
    writeData(news)
 
if __name__ == '__main__':
    main()