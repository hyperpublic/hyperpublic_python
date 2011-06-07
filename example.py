from hyperpublic import *

# get these values from http://hyperpublic.com/oauth_clients
CLIENT_ID = "YOUR_ID_HERE"
CLIENT_SECRET = "YOUR_SECRET_HERE"

if __name__ == '__main__':
    hp = Hyperpublic(CLIENT_ID, CLIENT_SECRET)
    items = hp.places.find(lat=40.7, lon=-74)
    print items
