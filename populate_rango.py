import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','twdproject.settings')
import random
import django
django.setup()
from rango.models import Category, Page

def populate():
	#1-o create lists  of dictionaries containing the pages we want to add into each category
	#2-0 then create dictionary of dictionaries for our categories
	#pythonpages, djangopages, etc pagine relative a categoria python, django, other
	#poi faccio dizionario in cui chiave primria è categoria, chiave del dizionario dentro 'pages'
	python_pages=[
	{'title':'Official Python Tutorial','url':'http://docs.python.org/3/tutorial/','views':random.randint(1,150)},
	{'title':'How to think like a cs','url':'http://www.greenteapress.com/thinkpython/','views':random.randint(1,150)},
	{'title':'Learn python in <20 minutes','url':'http://www.korokithakis.net/tutorials/python/','views':random.randint(1,150)}
	]

	django_pages=[
	{'title':'Official Django tutorial','url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/','views':random.randint(1,150)},
	{'title':'Django Rocks','url':'http://www.djangorocks.com/','views':random.randint(1,150)},
	{'title':'How to tango with django','url':'http://wwww.tangowithdjango.com/','views':random.randint(1,150)}
	]

	other_pages=[
	{'title':'Bottle','url':'http://bottlepy.org/docs/dev/','views':random.randint(1,150)},
	{'title':'Flask','url':'http://flask.pocoo.org','views':random.randint(1,150)}
	]

	cats ={'Python':{'pages':python_pages,'views':0,'likes':0},
	'Django':{'pages':django_pages,'views':0,'likes':0},
	'Other Frameworks':{'pages':other_pages,'views':0,'likes':0}}

	#going attraverso dizionario cats, aggiunge ogni categoria e poi ogni pagina associata ad essa
	for cat,cat_data in cats.items():
		views=cat_data['views']
		likes=cat_data['likes']
		c=add_cat(cat,views,likes)
		for p in cat_data['pages']:
			add_page(c,p['title'],p['url'],p['views'])

	for c in Category.objects.all():
		for p in Page.objects.filter(category=c):
			print(f'- {c}: {p}')


def add_page(cat, title, url, views=0):
	p=Page.objects.get_or_create(category=cat,title=title)[0]
	p.url=url
	p.views=views
	p.save()
	return p	

def add_cat(name,views,likes):
	c=Category.objects.get_or_create(name=name)[0]
	c.views=views
	c.likes=likes
	c.save() #getorcreate ritorna tupla object created
	return c	

if __name__=='__main__':
	print('Starting Rango population script...')
	populate()

