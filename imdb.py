# -*- coding: utf-8 -*-
"""Script to gather IMDB keywords from 2015's top grossing movies."""
import sys
import requests
from bs4 import BeautifulSoup
import csv

URL = "http://www.imdb.com/search/title?at=0&sort=boxoffice_gross_us,desc&start=1&year=2015,2015"


def get_top_grossing_movie_links(url):
    """Return a list of tuples containing the top grossing movies of 2013 and link to their IMDB
    page."""
    response = requests.get(url)
    movies_list = []
    for each_url in BeautifulSoup(response.text, "html.parser").select('.title a[href*="title"]'):
        movie_title = each_url.text
        if movie_title != 'X':
            movies_list.append((movie_title, each_url['href']))
    return movies_list


def get_keywords_for_movie(url):
    """Return a list of keywords associated with *movie*."""
    keywords = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    tables = soup.find_all('table', class_='dataTable')
    table = tables[0]
    # return [td.text for tr in table.find_all('tr') for td in tr.find_all('td')] 还有太多冗余信息，实际只需要关键词部分
    # return [td['data-item-keyword'] for tr in table.find_all('tr') for td in tr.find_all('td')] 部分td没有该关键词，需要判断一下
    for tr in table.find_all('tr'):
        for td in tr.find_all('td'):
            if td.get('data-item-keyword') != None:
                keywords.append(td['data-item-keyword'])
    return keywords


def main():
    """Main entry point for the script."""
    movies = get_top_grossing_movie_links(URL)
    with open('output.csv', 'w') as output:
        csvwriter = csv.writer(output)
        for title, url in movies:
            keywords = get_keywords_for_movie('http://www.imdb.com{}keywords/'.format(url))
            csvwriter.writerow([title, keywords])


if __name__ == '__main__':
    sys.exit(main())