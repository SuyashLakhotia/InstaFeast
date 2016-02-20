# InstaFeast
Created for and during NUS Hack&amp;Roll 2016.

InstaFeast is a simple web app that shows you the top Instagram photos taken of food & drinks at your favourite restaurant or café. Confused about what you want to order? Or what actually looks good? Just show the waiter a photo of what you want with **InstaFeast**!

InstaFeast allows you to select a location using the Google Maps API, which is then converted to a Facebook Graph Place, and subsequently, an Instagram Location. Then, by parsing the caption of the Instagram post & by using an external [face detection API](https://market.mashape.com/apicloud/facerect#!documentation) on the photo, the recent Instagram posts from the selected location are filtered through to scout for the top posts of food and/or drinks, which are displayed according to the number of likes the post received on Instagram.

### Screenshot:
![Screenshot](/Screenshots/InstaFeast1.JPG)

### Team:
1. [Suyash Lakhotia](https://github.com/SuyashLakhotia)
2. [Nikhil Venkatesh](https://github.com/nikv96)

### Running *InstaFeast*:
1. Run `pip install -r requirements.txt` to install the Python dependencies.
2. Create a file called `OAuthKeys.py` inside the *[MainApp](/MainApp/)* directory with the following format:
```
facebookAccess = <Facebook Graph API Access Token>
instagramAccess = <Instagram API Access Token>
mashapeAccess = <Mashape API Key>
```
