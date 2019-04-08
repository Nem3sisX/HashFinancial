# importing requests package
import requests
import time


print(" ********************* Today's Market News *********************")

def NewsFromBBC():
    # BBC news api
    main_url = " https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=cbf1294b5a50472c9145bc11df3932cb "

    # fetching data in json format
    open_bbc_page = requests.get(main_url).json()

    # getting all articles in a string article
    article = open_bbc_page["articles"]

    # empty list which will
    # contain all trending news
    results = []

    for ar in article:
        results.append(ar["title"])

    while True:
        for i in range(len(results)):
            # printing all trending news
            print()
            time.sleep(0.9)
            print(results[i])

    # Driver Code


if __name__ == '__main__':
    # function call
    NewsFromBBC()
