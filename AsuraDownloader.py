import os , requests , time
from tqdm import tqdm as tq
from  requests_html import HTMLSession
from bs4 import BeautifulSoup
import warnings 
warnings.filterwarnings ("ignore", category=UserWarning, module='bs4') 
from zipfile import ZipFile


def request(url):
    
 Session = HTMLSession()
 
 user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
 headers = {'User-Agent':user_agent}
 
 temp1 = Session.get(url,headers=headers).content
 temp2 = BeautifulSoup(temp1 , 'html.parser')
 return temp1 , temp2

def Comic_List():
    url = 'http://www.asurascans.com/manga/list-mode/'   
    none , soup = request(url)
    comiclist = soup.find(class_="soralist").findAll(class_="series")#(class_="soralist")
    comicnames = []
    link = {}
    for comic in comiclist  :
      if '\n ' != comic.text:
        comicnames.append(comic.text)
        link.update({comic.text:comic['href']})
        print(comic.text)  
    return comicnames , link

def Chapter(url):
    none , soup = request(url)    
    title = []
    chapter = {}
    chapterslist = soup.findAll(class_= "eph-num")   
    for chapters in chapterslist:
        title.append(chapters.find(class_="chapternum").text)
        chapter.update({chapters.find(class_="chapternum").text:chapters.find('a', href=True)['href']})
    return  title , chapter
   
def Image_URL(title , url):
    none , soup = request(url[title])  
    urls = []
    if(True): 
        images = soup.find(class_="entry-content entry-content-single maincontent")
        images = images.findAll('p')
        urllist = []
        for image in range(1 , len(images))  :
          urls.append(images[image].find('img')['src'])    

    return urls

def save_image(urls , path , skip):
    temp = []
    for i in range(len(urls)):
        temp.append(i)
    res = [i for i in temp if i not in skip]   
    temp = res      
    print(temp)
    
    for i in range(0,len(temp)):  
       Session = HTMLSession()
       page = Session.get(urls[temp[i]])
       saveiamge = open( path +'/page'+ str(temp[i]) +'.png', 'wb') 
       saveiamge.write(page.content)

def ZIP(path):
    temp = ZipFile(path + ".cbz" , "w")
    
    lastpath = os.getcwd()
    os.chdir(path)
    newpath = os.getcwd()
    
    for file in os.listdir(newpath):
        temp.write(file)
    for file in os.listdir(newpath):
        os.remove(file)
        
    os.chdir(lastpath)   
    os.removedirs(path)

def Folder(path):
    try:
      os.mkdir(path)
    except:
        pass
  
def show(data , mode):
     if mode == 'ps':
      for i in data:
          print( i)
     elif mode == 'pd':
      for i in data:
        print( i +' = '+data[i])
     elif mode == 'n':
         print(data)
     else:
         print( '=====================================================================')
         return
     print( '=====================================================================')
 
#==============================================================================

comicname , link = Comic_List()

DownloadingList = ['Villain To Kill' , 'Worn and Torn Newbie']

show(DownloadingList ,  'ps')
for name in DownloadingList:
    csurl = link[name]
    chapters , clinks = Chapter(csurl)
    chapters = list(reversed(chapters))
    print('Name = ' ,name, ' || URL = ' , csurl ,  '|| Chapter = ' , len(chapters))
    
    show('','')
    Folder(name)
 
    for num in tq(range(0,len(chapters)) , desc=name):
      tq._instances.clear()
      path = './' + name +'/' + chapters[num]
      Folder(path)
      save_image(Image_URL(chapters[num] , clinks) , path , [])
      ZIP(path)
    print("finshed")
    
    
    