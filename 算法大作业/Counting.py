
from bs4 import BeautifulSoup
from collections import Counter

url_list=[]

next_page=""
tag_list=[]
comment_people=[]
comment_url_list=[]
numbers=0

soup=BeautifulSoup("taglist.html")

for i in range(7):

    all_a=soup.findAll('a', class_="nbg")
    for i in all_a:
        url_list.append(i['href'])
    try:
        tem=soup.find('span',class_='next')
        next_page=or_page+tem.find('a')['href']
        r=requests.get(next_page)
        soup=BeautifulSoup(r.text,"html.parser")
    except:
        break
print(url_list)
for i in url_list:



    soup=BeautifulSoup(r.text,"html.parser")

    try:
        tag=soup.find('div',class_="tags-body")

        tags=tag.findAll('a')
        for j in tags:
            tag_list.append(j.text)
            numbers+=1

        tmp = soup.find('div',class_="tab")
        print(i+tmp.findAll('a')[-1]['href'])
        comment_url_list.append(i+tmp.findAll('a')[-1]['href'])



    except:
       continue
tag=Counter(tag_list).most_common(9)#统计标签频率 最多的9个

with open('comment_url_list','w') as f:
    for i in comment_url_list:
        f.write(i+'\n')


for i in tag:
    print(i[0]+'\t'+str(i[1])+'\n')

print(numbers)


