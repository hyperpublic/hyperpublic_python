#!/usr/bin/env python

import urllib2
try:
    import json
except ImportError:
    try:
        import simplejson as json
    except ImportError:
        raise ImportError, "hyperpublic requires Python >=2.6 or the simplejson module."

from urllib import urlencode


API_ENDPOINT = "https://api.hyperpublic.com/api/v1"


class HyperpublicError(Exception):
    """
    Generic Hyperpublic Exception object.
    """


class HyperpublicBase:
    """
    Abstract Hyperpublic API object. Do not use directly. Rather, use
    the Hyperpublic object and its places, people and things properties.
    """
    
    def __init__(self, client_id, client_secret, point_type):
        self.client_id = client_id
        self.client_secret = client_secret
        self.point_type = point_type
    
    def _filter_params(self, *params):
        """"
        Merges one or more dictionaries of parameters, stripping off all
        items whose value is None. Returns a new dictionary.
        """
        items = []
        for dictionary in params:
            for k,v in dictionary.items():
                if v is not None:
                    items.append((k, v))
        return dict(items)
    
    def _get(self, url, params=dict()):
        try:
            params['client_id'] = self.client_id
            params['client_secret'] = self.client_secret
            real_url = "%s?%s" % (url, urlencode(params))
            result = urllib2.urlopen(real_url)
            return json.load(result)
        except urllib2.URLError, e:
            raise HyperpublicError(e)
    
    def _post(self, url, params=dict()):
        try:
            if 'tags' in params and isinstance(params['tags'], (list, tuple)):
                params['tags'] = ",".join(params['tags'])
            if not params['tags']:
                # possibly empty string
                del params['tags']
            
            query_params = dict(client_id=self.client_id, 
                                client_secret=self.client_secret)
            real_url = "%s?%s" % (url, urlencode(query_params))
            result = urllib2.urlopen(real_url, urlencode(params))
            return json.load(result)
        except urllib2.URLError, e:
            raise HyperpublicError(e)
    
    def create(self, **params):
        url = "%s/%s" % (API_ENDPOINT, self.point_type)
        return self._post(url, params)
    
    def show(self, id):
        url = "%s/%s/%s" % (API_ENDPOINT, self.point_type, id)
	print url
        return self._get(url)
    
    def find(self, lat=None, lon=None, address=None, postal_code=None,
             neighborhood=None, radius=None, q=None, limit=None, 
             page=None, page_size=None, **extra_params):
        params = locals()
        del params['self']
        del params['extra_params']
        params = self._filter_params(params, extra_params)
        return self._get("%s/%s" % (API_ENDPOINT, self.point_type), params)
    

class Hyperpublic:
    """
    A Hyperpublic API object. Requires a client_id and client_secret, 
    which one may obtain at http://hyperpublic.com/oauth_clients.
    """

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
    @property
    def places(self):
        """An object for creating/showing/finding Places."""
        return Places(self.client_id, self.client_secret)
    @property
    def offers(self):
        """An object for creating/showing/finding Offers."""
        return Offers(self.client_id, self.client_secret)
    
    @property
    def people(self):
        """An object for creating/showing/finding People."""
        return People(self.client_id, self.client_secret)
    
    @property
    def things(self):
        """An object for creating/showing/finding Things."""
        return Things(self.client_id, self.client_secret)
    
class Offers(HyperpublicBase):
    def __init__(self, client_id, client_secret):
        HyperpublicBase.__init__(self, client_id, client_secret, "offers")
    
    def find(self, lat=None, lon=None, address=None, source_id=None,
             price=None,price_min=None,price_max=None,offer_type=None, radius=None, q=None, limit=None, 
             page=None, page_size=None):
        
        
	params = locals()
	params['type']=offer_type;
        del params['self']
        return HyperpublicBase.find(self, **params)
    


class Places(HyperpublicBase):
    def __init__(self, client_id, client_secret):
        HyperpublicBase.__init__(self, client_id, client_secret, "places")
    
    def create(self, display_name, phone_number=None, website=None,
               place_type=None, image_url=None, tags=[], address=None,
               postal_code=None, lat=None, lon=None):
        
        params = locals()
        del params['self']
        return HyperpublicBase.create(self, **params)


class People(HyperpublicBase):
    def __init__(self, client_id, client_secret):
        HyperpublicBase.__init__(self, client_id, client_secret, "people")
    
    def find(self, lat=None, lon=None, address=None, postal_code=None,
             neighborhood=None, radius=None, q=None, limit=None, 
             page=None, page_size=None, with_photo=True):
        
        if with_photo is None:
            pass
        elif with_photo:
            with_photo = "true"
        else:
            with_photo = "false"
        
        params = locals()
        del params['self']
        return HyperpublicBase.find(self, **params)
    
    def create(self, email, name=None, display_name=None, password=None,
               image_url=None, tags=[], address=None, postal_code=None, 
               lat=None, lon=None):

        params = locals()
        del params['self']
        return HyperpublicBase.create(self, **params)
    

class Things(HyperpublicBase):
    def __init__(self, client_id, client_secret):
        HyperpublicBase.__init__(self, client_id, client_secret, "things")
    
    def create(self, display_name, price=None, image_url=None, tags=[], 
               address=None, postal_code=None, lat=None, lon=None):

        params = locals()
        del params['self']
        return HyperpublicBase.create(self, **params)

