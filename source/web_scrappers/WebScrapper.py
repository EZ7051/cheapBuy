"""
Copyright (c) 2021 Anshul Patel
This code is licensed under MIT license (see LICENSE.MD for details)

@author: cheapBuy
"""

from concurrent.futures import ThreadPoolExecutor, as_completed

from source.web_scrappers.FetchDescription import FetchDescription
from source.web_scrappers.WebScrapper_Amazon import WebScrapper_Amazon
from source.web_scrappers.WebScrapper_Bestbuy import WebScrapper_Bestbuy
from source.web_scrappers.WebScrapper_Bjs import WebScrapper_Bjs
from source.web_scrappers.WebScrapper_Costco import WebScrapper_Costco
from source.web_scrappers.WebScrapper_Ebay import WebScrapper_Ebay
from source.web_scrappers.WebScrapper_TraderJoes import WebScrapper_TraderJoes
from source.web_scrappers.WebScrapper_Walmart import WebScrapper_Walmart
from source.web_scrappers.WebScrapper_Kroger import WebScrapper_Kroger

class WebScrapper:
    """
    Main class used to fetch results by parsing the URL

    ...

    Attributes
    ----------
    product_link : str
        link of the product

    Methods
    -------
    get_driver:
        Returns Chrome Driver
    get_description:
        Fetch description for all websites
    call_scrapper:
        Build Threads and call scrapper for all websites
    """
    """
    Main class used to fetch results by parsing the URL

    ...

    Attributes
    ----------
    product_description : str
        description of the product

    Methods
    -------
    get_driver:
        Returns Chrome Driver
    get_description:
        Fetch description for all websites
    call_scrapper:
        Build Threads and call scrapper for all websites
    """
    #
    # def __init__(self, product_link):
    #     """
    #     Parameters
    #     ----------
    #     product_link : str
    #         link of the product
    #     """
    #     self.product_link = product_link
    #     self.executor = ThreadPoolExecutor(max_workers=10)
    #
    # def get_description(self):
    #     """
    #     Fetch description for all websites
    #     """
    #     # # Check the incoming URL for the website and call function to extract description accordingly
    #     # if 'walmart' in self.product_link:
    #     #     source = 'walmart'
    #     #     fd = FetchDescription(self.product_link)
    #     #     description = fd.fetch_desc_walmart()
    #     # elif 'amazon' in self.product_link:
    #     #     source = 'amazon'
    #     #     fd = FetchDescription(self.product_link)
    #     #     description = fd.fetch_desc_amazon()
    #     # elif 'ebay' in self.product_link:
    #     #     source = 'ebay'
    #     #     fd = FetchDescription(self.product_link)
    #     #     description = fd.fetch_desc_ebay()
    #     # elif 'costco' in self.product_link:
    #     #     source = 'costco'
    #     #     fd = FetchDescription(self.product_link)
    #     #     description = fd.fetch_desc_costco()
    #     # elif 'bjs' in self.product_link:
    #     #     source = 'bjs'
    #     #     fd = FetchDescription(self.product_link)
    #     #     description = fd.fetch_desc_bjs()
    #     #
    #     # elif 'bestbuy' in self.product_link:
    #     #     source = 'bestbuy'
    #     #     fd = FetchDescription(self.product_link)
    #     #     description = fd.fetch_desc_bestbuy()
    #     #
    #     # elif 'traderjoes' in self.product_link:
    #     #     source = 'traderjoes'
    #     #     fd = FetchDescription(self.product_link)
    #     #     description = fd.fetch_desc_traderjoes()
    #     #
    #     # elif 'kroger' in self.product_link:
    #     #     source = 'kroger'
    #     #     fd = FetchDescription(self.product_link)
    #     #     description = fd.fetch_desc_kroger()
    #     #
    #     # else:
    #     #     source = 'N/A'
    #     # if source != 'N/A':
    #     #     return description
    #     website_configs = {
    #         'walmart': 'fetch_desc_walmart',
    #         'amazon': 'fetch_desc_amazon',
    #         'ebay': 'fetch_desc_ebay',
    #         'costco': 'fetch_desc_costco',
    #         'bjs': 'fetch_desc_bjs',
    #         'bestbuy': 'fetch_desc_bestbuy',
    #         'traderjoes': 'fetch_desc_traderjoes',
    #         'kroger': 'fetch_desc_kroger'
    #     }
    #
    #     source = 'N/A'
    #     for website, scraper_method in website_configs.items():
    #         if website in self.product_link:
    #             source = website
    #             fd = FetchDescription(self.product_link)
    #             description = getattr(fd, scraper_method)()
    #             break
    #
    #     if source != 'N/A':
    #         return description
    #
    # def call_scrapper(self):
    #     """
    #     Build Threads and call scrapper for all websites
    #     """
    #     # Get description from incoming URL
    #     product_description = self.get_description()
    #     # print(product_description)
    #
    #     #scrapper = [WebScrapper_Bestbuy] # So slow though only bestbuy, why?
    #     scrapper = [WebScrapper_Amazon, WebScrapper_Walmart, WebScrapper_Ebay,
    #                 WebScrapper_Bjs, WebScrapper_Costco, WebScrapper_TraderJoes, WebScrapper_Kroger]
    #
    #     t_scrapper = [s.__call__(product_description) for s in scrapper]
    #
    #     res = []
    #     futs = [self.executor.submit(s.run) for s in t_scrapper]
    #     for future in as_completed(futs):
    #         try:
    #             res.append(future.result())
    #         except Exception as e:
    #             print('Exception in thread...', e)
    #
    #     return res

    def __init__(self, product_description):
        """
        Parameters
        ----------
        product_description : str
            description of the product
        """
        self.product_description = product_description
        self.executor = ThreadPoolExecutor(max_workers=10)

    def get_description(self, website):
        """
        Fetch description for a specific website
        """
        # Check the incoming website and call the function to extract description accordingly
        website_configs = {
            'walmart': 'fetch_desc_walmart',
            'amazon': 'fetch_desc_amazon',
            'ebay': 'fetch_desc_ebay',
            'costco': 'fetch_desc_costco',
            'bjs': 'fetch_desc_bjs',
            'bestbuy': 'fetch_desc_bestbuy',
            'traderjoes': 'fetch_desc_traderjoes',
            'kroger': 'fetch_desc_kroger'
        }

        if website not in website_configs:
            return 'N/A'

        fd = FetchDescription(self.product_description)
        scraper_method = website_configs[website]
        return getattr(fd, scraper_method)()

    def call_scrapper(self):
        """
        Build Threads and call scrapper for all websites
        """
        #scrapper = [WebScrapper_Bestbuy] # So slow though only bestbuy, why?
        scrapper = [WebScrapper_Amazon, WebScrapper_Walmart, WebScrapper_Ebay,
                    WebScrapper_Bjs, WebScrapper_Costco, WebScrapper_TraderJoes, WebScrapper_Kroger]

        t_scrapper = [s.__call__(self.product_description) for s in scrapper]

        res = []
        futs = [self.executor.submit(s.run) for s in t_scrapper]
        for future in as_completed(futs):
            try:
                res.append(future.result())
            except Exception as e:
                print('Exception in thread...', e)

        return res
