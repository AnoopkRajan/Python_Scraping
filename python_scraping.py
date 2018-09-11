from requests import get 


from bs4 import BeautifulSoup


url = "https://google.com/search?q=foss@amrita"

response = get(url=url)


extract = BeautifulSoup(response.text,'lxml')


titles = extract.find_all('h3')



for title in titles:
	print(title.get_text())
