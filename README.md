# InstaFeast
Created for and during NUS Hack&amp;Roll 2016.

InstaFeast is a simple web app that gives you the top Instagram photos taken of food & drinks at your favourite restaurant or café. Confused about what you want to order? Or what actually looks good? Just show the waiter a photo of what you want with **InstaFeast**!

InstaFeast allows you to select a place using the Google Maps API, which is then converted to a Facebook Graph Place and subsequently, an Instagram Location. Then, using a search algorithm & an external [face detection API](https://market.mashape.com/apicloud/facerect#!documentation), the recent Instagram posts from that location are filtered through to scout for the top posts of only food and/or drinks, which are displayed according to the number of likes the post received on Instagram.

### Screenshot:
![Screenshot](/Screenshots/InstaFeast1.JPG)

### Team:
1. [Suyash Lakhotia](https://github.com/SuyashLakhotia)
2. [Nikhil Venkatesh](https://github.com/nikv96)

<br><br>
*NOTE:* A file called `OAuthKeys.py` must be present inside the *[MainApp](/MainApp/)* directory with the following format for InstaFeast to work properly:
```
facebookAccess = <Facebook Graph API Access Token>
instagramAccess = <Instagram API Access Token>
mashapeAccess = <Mashape API Key>
```
