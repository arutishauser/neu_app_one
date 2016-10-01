from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

auth = Oauth1Authenticator(
    consumer_key="wxtfC7Mu6QJT_ikVvRlyGg",
    consumer_secret="Y7AMG2sYvYim6FBpgLoi-FgX2w0",
    token="g8ko8ATE6GiZgUQbTsHqjfksdW7XbAY0",
    token_secret="NVM2E762_vl7F1hekhc4xTxncmM"
)

# client = Client(auth)

# params = {
#     'term': 'food',
#     'lang': 'fr'
# }

# response=client.search("San Francisco", **params)

# for business in response.businesses:
# 	print (business.name)

# locatione = "New York City"
# terma='food'

# def chalange(location, term):
# 	params = {'term': term,'lang': 'de'}
# 	response=client.search(location, **params)
# 	for business in response.businesses:
# 		print ("Arthur noch neuer", business.name, business.rating, business.phone)

# chalange('Zürich', 'food')

# for business in response.businesses:
# 	print ("noch neuer", business.name, "Raiting:", business.rating, "Tel:", business.phone)

def get_businesses(location, term):
	auth = Oauth1Authenticator(
    	consumer_key="wxtfC7Mu6QJT_ikVvRlyGg",
    	consumer_secret="Y7AMG2sYvYim6FBpgLoi-FgX2w0",
    	token="g8ko8ATE6GiZgUQbTsHqjfksdW7XbAY0",
    	token_secret="NVM2E762_vl7F1hekhc4xTxncmM"
	)

	client = Client(auth)

	params = {
    	'term': term,
    	'lang': 'en'
		}
	response=client.search(location, **params)
	businesses = []
	for business in response.businesses:
		businesses.append("{} Raiting {}° Tel {}".format(business.name, business.rating, business.phone))
	return '\n'.join(sorted(businesses,reverse=True)[:3])


print (get_businesses('Zürich', 'food'))

# def get_businessesnew(location, term):
# 	auth = Oauth1Authenticator(
#     	consumer_key="wxtfC7Mu6QJT_ikVvRlyGg",
#     	consumer_secret="Y7AMG2sYvYim6FBpgLoi-FgX2w0",
#     	token="g8ko8ATE6GiZgUQbTsHqjfksdW7XbAY0",
#     	token_secret="NVM2E762_vl7F1hekhc4xTxncmM"
# 	)

# 	client = Client(auth)

# 	params = {
#     	'term': term,
#     	'lang': 'en'
# 		}
# 	response=client.search(location, **params)
# 	businesses = []
# 	for business in response.businesses:
# 		#print ("Mattan, noch besser", business.name, "Raiting:", business.rating, "Tel:", business.phone)
# 		businesses.append({"name": business.name, 
#             "rating": business.rating, 
#             "phone": business.phone
#         })
# 	return businesses

# businesses = get_businessesnew('New York City', 'food')

# print(businesses)


import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())



def get_businessesnew(address, term):
	auth = Oauth1Authenticator(
    	consumer_key=os.environ['CONSUMER_KEY'],
    	consumer_secret=os.environ['CONSUMER_SECRET'],
    	token=os.environ['TOKEN'],
    	token_secret=os.environ['TOKEN_SECRET']
	)

	client = Client(auth)

	params = {
    	'term': term,
    	'lang': 'en'
		}
	response=client.search(address, **params)
	businesses = []
	for business in response.businesses:
		#print ("Mattan, noch besser", business.name, "Raiting:", business.rating, "Tel:", business.phone)
		businesses.append({"name": business.name, 
            "rating": business.rating, 
            "phone": business.phone
        })

	return sorted(businesses, key=lambda k: k['rating'], reverse=True)[:3]


print (get_businessesnew('Zürich, Switzerland', 'food'))

#print(businesses[:3])

# newlist = sorted(businesses, key=lambda k: k['rating'], reverse=True)
# print("Das sind die besten Beizen", newlist[:3])
# top_drei=newlist[:3]
# print (top_drei)

# top_drei = []
# for item in top_drei:
# 	top_drei.append(top_drei.item['name'],"Raiting:", top_drei.item['rating'], "Phone:", top_drei.item['phone'])

# print(top_drei)

# def get_businesses(address, term):
# 	auth = Oauth1Authenticator(
#     	consumer_key="wxtfC7Mu6QJT_ikVvRlyGg",
#     	consumer_secret="Y7AMG2sYvYim6FBpgLoi-FgX2w0",
#     	token="g8ko8ATE6GiZgUQbTsHqjfksdW7XbAY0",
#     	token_secret="NVM2E762_vl7F1hekhc4xTxncmM"
# 	)

# 	client = Client(auth)

# 	params = {
#     	'term': term,
#     	'lang': 'en'
# 		}
# 	response=client.search(address, **params)
# 	for business in response.businesses:
# 		return "Mattan, noch besser", business.name, "Raiting:", business.rating, "Tel:", business.phone

#get_businesses('Zürich', 'food')