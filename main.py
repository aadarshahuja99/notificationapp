from plyer import notification
import requests
from bs4 import BeautifulSoup
import time
def notify(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon = r"/Users/apple/Downloads/icon.ico",
        timeout=9
    )

def getData(url):
    r=requests.get(url,verify=False)
    return r.text
if __name__=="__main__":
    while True:
        hData=getData('https://www.mohfw.gov.in/')
        soup=BeautifulSoup(hData,'html.parser')
        for tr in soup.find_all('table'):
            myData=tr.get_text()
        print(myData)
        myData=myData[1:]
        
        states=['Maharashtra','Delhi','Gujarat']
        itemList=myData.split("\n\n")
        print(itemList[3:38],len(itemList)-3) 
        for i in itemList[3:38]:
            dataList=i[:].split("\n")
            print(dataList)
            if dataList[0] in states:
                ntitle="Covid cases"
                ntext=f"State: {dataList[1]}\nActive {dataList[2]}\nCured {dataList[3]}\nDeaths: {dataList[4]}\nTotal: {dataList[5]}"
                notify(ntitle,ntext)
                time.sleep(5)
        time.sleep(5400)    
