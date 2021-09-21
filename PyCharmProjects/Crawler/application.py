import csv
from crawler import ArticleFetcher, CrawledArticle


#class Application:

url = "http://python.beispiel.programmierenlernen.io/index.php"
output_file = "data\crawler_output.csv"

fetcher = ArticleFetcher(url)
with open(output_file, 'w', newline='', encoding='utf-8') as csv_file:
    article_writer = csv.writer(csv_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    article_writer.writerow(CrawledArticle.csv_header())

    for article in fetcher.fetch(limit_entries=15):
        article_writer.writerow(article.to_csv())
