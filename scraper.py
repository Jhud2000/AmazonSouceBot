from googlesearch import search
class Scraper(object):
    def search(self, query):
        # res = search(term=query, num_results=10,)
        for j in search(query,  advanced=True):

            print(j)



scraper = Scraper()
scraper.search("845423018368")

