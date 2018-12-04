from bs4 import BeautifulSoup
import requests,csv
from urllib.parse import urlparse

#url="https://www.nationalcentrefordiversity.com/home/national-patrons-network"
url2="https://www.hrdsummit.com/speaker-partners"
url3="https://www.hrdsummit.com/speaker-partners/10"

outfile = open('speaker-data.csv','w', newline='')
writer = csv.writer(outfile)
writer.writerow(["name", "job_title","company"])

def getLinks(link):
    req=requests.get(link).text
    soup=BeautifulSoup(req,'lxml')
    tmp=""
    my_list=[]
    my_list.append(url2)
    page=soup.find_all('a',class_='page-numbers')
    for sz in page:
        if sz.text!="Next »":tmp=sz.text
    #print(tmp)
    for x in range(2,int(tmp)+1):
        new_url=url3.replace("10",str(x))
        #print(new_url)
        my_list.append(new_url)
    return my_list
            

def kangkung(link):
    req=requests.get(link).text
    soup=BeautifulSoup(req,'lxml')
    div=soup.find_all('div',class_='speaker-column')
    for d in div:
        try:
            name1=d.find('div',class_='speaker-column__container')
            name2=name1.find('h2')
            title=name1.find('h3')
            cmp1=d.find('img').get('src')
            cmp2=cmp1.split('/')[-1]
            cmp3=cmp2.replace(".png","").replace(".jpg","")
            if cmp1 and name1:
                print(name2.text+", "+title.text+", "+cmp3)
                writer.writerow([name2.text, title.text, cmp3])
        except:
            #print("something wrong:",sys.exc_info()[0])
            pass

def kuskus():
    myList=getLinks(url2)
    for m in myList:
        kangkung(m)


print("Getting data from "+url2)
print()


kuskus()
outfile.close()
