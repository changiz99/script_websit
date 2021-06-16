from bs4 import BeautifulSoup
from numpy import fabs
import requests
from openpyxl import Workbook
import datetime


wb = Workbook()

# grab the active worksheet
ws = wb.active
end_of_game= []

last_list_of_publishers = []
url_publishers_page = []
url_nasheran_pages = []
lstfunc = []
rows = 0
count_generat_page = 0 
while ( count_generat_page <= 5) :
#THIS while loop  get number page we need to script
  count_generat_page = count_generat_page+1
  url_nasheran_pages.append( 'http://www.nashreiran.ir/publishers/list/'+ str(count_generat_page))  

for url_nasheran_page in url_nasheran_pages :
      #This loop takes the  link of publishers on the page
  response = requests.get(url_nasheran_page)
  html2 = response.content
  soup = BeautifulSoup(html2, "html.parser")
  for link in soup.findAll('a'):
    #This loop separates the links from the rest of the page   
    lstfunc.append(link.get('href'))
    
    
    for get_page in lstfunc[43:119:1] :
      #Take the publishers' dedicated page and separate the information
      response_page = requests.get(get_page)
      html = response_page.content
      soup = BeautifulSoup(html, "html.parser")
      table_func = soup.find('div',id = 'content')
      funclists = table_func.find_all('tr')
      coulms = 0
      
      rows = rows + 1
      coulms = coulms + 1
      for function in funclists:
        #Separate the list items from each other and sort them into another list    
        father = []
        father.clear()
        last_list_of_publishers.clear()
        tds = function.find_all('td' , class_ = 'data-cols')
        if tds:
          for td in tds:
            father.append(td.text.strip())                
            last_list_of_publishers.append(father)
        for count in last_list_of_publishers :
            coulms = coulms + 1
            ws.cell(row= rows   , column = coulms).value = count[0]
            
        wb.save('kkkjh.xlsx')
  






   
        
        
    
        
    
    








