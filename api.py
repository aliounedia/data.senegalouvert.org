# -*- coding: latin-1 -*-
"""
This module try to get some informations for ansd by using the
exellent ckanapi. some useful methods are implemented
here like ansd_dataset_search which search data for ansd .Also
The ckanclient  package_entity_get method are used to
retreveive some useful informations  like --url page --and the --
url_downloaded page which will be used for others things.
For exemple into some apps (ansd_mobil_app)
For exemple the  ansd_package_entity_get will ouput something
like That.

entity https://commondatastorage.googleapis.com/ckannet-storage/2011-11-24T11202
5/AfTerFibre_21nov2011.csv
ansd_test
entity https://commondatastorage.googleapis.com/ckannet-storage/2011-11-24T11202
5/AfTerFibre_21nov2011.csv
ansd_test_csv
entity [u'http://ckannet-storage.commondatastorage.googleapis.com/storage/f/2013
-04-09T152249\\my_data.csv', u'']
ansd_test2
entity http://www.ansd.sn/intitutionnel/SDS_senegal_2008_2013.pdf
...
...

And The ansd_package_entity_get_tojson  method will store results of search
into The jsonfiles
Free for you to add others methods
"""
import ckanclient, sys, codecs,re, json
data_link_desc = "datas/descriptions"
class CkanPost(ckanclient.CkanClient):
    def __init__(self, base_location=None, api_key=None, is_verbose=False,
                 http_user=None, http_pass=None, **kwargs):
        ckanclient.CkanClient.__init__(
           self, 
           base_location = base_location,
           api_key=api_key,
           is_verbose = is_verbose,
           http_user = http_user,
           http_pass  = http_pass)

    def ansd_dataset_ihpc(self):
        """ return the set of datasets for ansd """
        i = 0
        list =[]
        for package in  self.package_list():
            if re.match("ihpc", package, re.IGNORECASE):
                list.append(package)
        return list

    def ansd_dataset_search(self):
        """ return the set of datasets for ansd """
        i = 0
        list =[]
        q    ="ansd"
        count, results = rs["count"], rs["results"]
        print results
        for package in  iter(results):
            list.append(package)
        return list

    def ansd_package_entity_get(self):
        """ Get the ansd pakage entity"""
        list = []
        for package in self.ansd_dataset_search():
            print package
            e = self.package_entity_get(package)
            try:print "entity", e["url"] 
            except:
                pass
            list.append(e)
        return list

    def ansd_dataset_search_tojson(self):
        """ return the set of datasets for ansd """
        i = 0
        list = []
        q    ="ansd"
        rs = self.package_search(q= q ,
                search_options ={"groups":'country-sn'})
        count, results = rs["count"], rs["results"]
        print results
        it =iter(results)
        while True:
            try:
                package  =next(it)
                print package
                list.append(package)
            except StopIteration, e:
                break
            except:
                continue
        json.dump(list, open(
                'ansd_dataset_search_tojson.json', 'wb'),
                indent=4, sort_keys=True)
    
    def ansd_package_entity_get_tojson(self):
        """ Put the ansd pakage entity to json file """
        list = []
        for package in json.load(
            open("ansd_dataset_search_tojson.json")):
            print package
            try:
                e = self.package_entity_get(package)
                list.append(e)
            except:
                pass
        json.dump(list, open(
                'ansd_package_entity_get_tojson.json', 'wb'),
                indent=4, sort_keys=True)


    def __repr__(self):
        """ return the set of datasets for ckan """
        i = 0
        for package in  self.package_list():
            print package
            i +=1
        print 'len :', i

ckan_post  = CkanPost("http://datahub.io/api",
                      
        "a3c845db-f5f8-44af-a493-5ca5f6eccd93",
        True,
        "aliounedia",
        "aliounedia")

ansd_dataset_ihpc     =     ckan_post.ansd_dataset_ihpc
if __name__ == '__main__':
    ckan_post  = CkanPost("http://datahub.io/api",
        "b3c845db-f5f8-44af-a493-5ca5f6eccd94",
        True,
        "xxx",
        "xxx")
    
    #ckan_post.ansd_dataset_search_tojson()
    ckan_post.ansd_package_entity_get_tojson()
           
           


         



          
          
