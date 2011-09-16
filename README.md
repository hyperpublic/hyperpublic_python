H#The Hyperpublic Ruby Gem
======================

A Python wrapper for the Hyperpublic REST API


#Installation
----------------
    cd hyperpublic_python/
    python setup.py install


#Sample Usage
----------------
###Working with Places
    from hyperpublic import *
    hp=Hyperpublic("YOUR_CLIENT_ID","YOUR_CLIENT_SECRET")
    #find a single place by ID
    place = hp.places.find("4dd53bffe2f2d70816000001")

    #find places by a query
    places = hp.places.find(q="chicken")

    #find places by a location
    places = hp.places.find(address="416 w 13th st, New York")

    #find places by multiple criteria
    places = hp.places.find(category ="food", postal_code= 10012)

    #create a place
    place=hp.places.create(display_name = "Hyperpublic HQ",                                                           
                tags =["place_tag1", "place_tag2"],                                                                   
                image_url="http://s3.amazonaws.com/prestigedevelopment/beta/image_photos/4dd535cab47dfd026c000002/square.png?1296938636",
                phone_number = "2124857375",                                                                          
                website = "www.hyperpublic.com",                                                                      
                category_id = "4e274d89bd0286830f000170",                                                             
                address = "416 w 13th st, New York, NY 10012",                                                        
                lat = 40.7405, 
                lon = -74.007)         

###Working with Categories
      #get a list of categories
      hp=Hyperpublic("YOUR_CLIENT_ID","YOUR_CLIENT_SECRET")
      categories=hp.categories.find()
      


#Documentation
---------------
visit our [developer site](http://developer.hyperpublic.com) for more information.