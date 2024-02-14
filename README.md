In this project, I will be following the [ScrapeOps](https://scrapeops.io/python-scrapy-playbook/scrapy-beginners-guide/#step-1---setup-your-python-environment) `scrapy` tutorial however adapting it to this web app. This app aims to take an input of multiple grocery products and scan a variety of grocery websites to find the shop that allows you to get the ingredients for the lowest price.


## First Problem:
The first problem encountered was trying to set up a spider to scrape Asda. The URL design for asda uses the format: groceries.asda.com/search/[item]. So if I was to get the information regarding apples i would use the URL groceries.asda.com/search/apples. However to properly set up the spider I must first inspect the URL and inspect the data retrieved from teh scrapy fetch command.

To fetch the web data and store it into a local file I ran the following:
```bash
scrapy fetch https://groceries.asda.com/search/apples --nolog  > response.html
```
After opening `response.html` the following page was displayed:
![Screenshot 2024-02-13 at 18 59 11](https://github.com/hahaharry10/GroceryShopComparer/assets/118996632/1c8d919b-f596-4253-8a0f-ca380d1947d8)

Showing that scraping Asda will be less simple as the tutorial describes as i will first have to get past this page.
