from GoogleNews import GoogleNews
class NewsAgent:
    def search_by_title(self, title) :
        # list of local news sites
        local_news_sites = [
            'Herald',
            'Newsday',
            'H-Metro',
            'Sunday Mail ',
            'Bulawayo 24 '
            'Kwayedza'
        ]
        # initialize google news object
        googlenews = GoogleNews()

        # initialise list that will store all news objects
        all_articles = []
        
        # run a search based on each news site and given search title
        for site in local_news_sites:
            googlenews.search(site + ' ' + str(title))

            # list with articles based on given title and site
            news = googlenews.result()

            # add article list from site to final list
            all_articles = all_articles + news

            # clear result list before doing another search with the same object
            googlenews.clear()


        # list contains objects with field matching keys expected by client i.e title, desc, link , keys are already as required
        # therefore return list as is

        return all_articles

    def search_by_category(self, cat) :
        # list of local news sites
        local_news_sites = [
            'Herald',
            'Newsday',
            'H-Metro',
            'Sunday Mail',
            'Bulawayo 24'
            'wayedza'
        ]
        # initialize google news object
        googlenews = GoogleNews()

        # initialise list that will store all news objects
        all_articles = []

        # run a search based on each news site and given search category
        for site in local_news_sites:
            googlenews.search(site + ' ' + str(cat))

            # list with articles based on given category and site
            news = googlenews.result()

            # add article list from site to final list
            all_articles = all_articles + news

            # clear result list before doing another search with the same object
            googlenews.clear()

        # list contains objects with field matching keys expected by client i.e title, desc, link , keys are already as required
        # therefore return list as is

        return all_articles
