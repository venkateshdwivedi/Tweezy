from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq

def imgsource(username1):
	#fetch url of profile page
	myurl ='https://twitter.com/username1'
	#open the url
	uclient= ureq(myurl)
	#read and store it in pagehtml
	pagehtml = uclient.read()
	uclient.close
	#parsing
	pagesoup= soup(pagehtml,"html.parser")
	#find profilepic from the page
	container = pagesoup.find("div",{"class":"ProfileCanopy-avatar"})
	#location of profile pic
	image1= container.div.img["src"]
	return image1






     

