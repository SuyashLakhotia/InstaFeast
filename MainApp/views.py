from django.shortcuts import render
import requests, json, urllib
import collections
from django.contrib.staticfiles.templatetags.staticfiles import static
from . import OAuthKeys

def IndexView(request):
	context = {}
	if request.method == 'POST':
		name = request.POST.get('placeName')
		lat = request.POST.get('placeLat')
		lng = request.POST.get('placeLng')
		context = Google_to_FB_to_Insta(name, lat, lng)
		context['name'] = name
		context['first'] = False
		return render(request,'index.html', context) 
	return render(request,'index.html', {'first':True}) 

def Google_to_FB_to_Insta(name, lat, lng):
	# OAuthKeys.py should store the OAuth Access Tokens for FB & Instagram:
	fb_access = OAuthKeys.facebookAccess
	insta_access = OAuthKeys.instagramAccess
	mashape_access = OAuthKeys.mashapeAccess

	goog_lat = lat
	goog_lng = lng
	goog_name = name

	limit = 0

	fb_places_names = []
	fb_places_id = []

	termsCheck = ['breakfast', 'brunch', 'lunch', 'dinner', 'food', 'dessert', 'delicious', 'tasty', 'yum']
	insta_pic_urls = []
	insta_pic_likes = []

	fb_resp = requests.get('https://graph.facebook.com/v2.5/search?fields=id%2Cname&limit=1000&offset=0&type=place&center=' + str(goog_lat) + '%2C' + str(goog_lng) + '&distance=100&access_token=' + fb_access)

	if fb_resp.status_code != 200:
	    print('GET Graph API {}'.format(fb_resp.status_code))	# Return empty list and display 'No Matches' label.
	else:
		fb_parsed = json.loads(json.dumps(fb_resp.json()))

		for x in range(0, len(fb_parsed['data'])):
			fb_places_names.append(fb_parsed['data'][x]['name'])
			fb_places_id.append(fb_parsed['data'][x]['id'])

		for x in fb_places_names:
			if goog_name in x:
				fb_place_id = fb_places_id[fb_places_names.index(x)]
				print(x + ", " + fb_place_id)

				insta_resp = requests.get('https://api.instagram.com/v1/locations/search?access_token=' + insta_access + "&facebook_places_id=" + str(fb_place_id))

				if insta_resp.status_code != 200:
				    print('GET Instagram API {}'.format(insta_resp.status_code))	# Return empty list and display 'No Matches' label.
				else:
					insta_parsed = json.loads(json.dumps(insta_resp.json()))

					if len(insta_parsed['data']) != 0:
						insta_place_id = insta_parsed['data'][0]['id']
						print(insta_parsed['data'][0]['name'] + ", " + insta_place_id)

						insta_resp = requests.get('https://api.instagram.com/v1/locations/' + insta_place_id + '/media/recent?access_token=' + insta_access)
						
						if insta_resp.status_code != 200:
							print('GET Instagram API {}'.format(insta_resp.status_code))	# Return empty list and display 'No Matches' label.
						else:
							insta_search_next = "XXX"
							
							while insta_search_next != "None":
								if limit > 100:
									break

								insta_parsed = json.loads(json.dumps(insta_resp.json()))

								for y in range(0, len(insta_parsed['data'])):
									if insta_parsed['data'][y]['type'] == 'image':
										if insta_parsed['data'][y]['caption'] != None:
											insta_caption = insta_parsed['data'][y]['caption']['text'].lower()
											if any(term in insta_caption for term in termsCheck):
												face_response_url = "https://apicloud-facerect.p.mashape.com/process-url.json?url="+urllib.parse.quote_plus(insta_parsed['data'][y]['images']['standard_resolution']['url'])
												face_response_headers = {'X-Mashape-Key': mashape_access, 'Accept': 'application/json'}
												face_response = requests.get(face_response_url, headers=face_response_headers)
												face_response_parsed = json.loads(json.dumps(face_response.json()))
												
												if len(face_response_parsed['faces']) == 0:
													insta_pic_urls.append(insta_parsed['data'][y]['images']['standard_resolution']['url'])
													insta_pic_likes.append(insta_parsed['data'][y]['likes']['count'])
													print(insta_parsed['data'][y]['images']['standard_resolution']['url'] + ", " + str(insta_parsed['data'][y]['likes']['count']))

										limit = limit + 1

								if 'next_url' in insta_parsed['pagination']:
									insta_search_next = insta_parsed['pagination']['next_url']
									insta_resp = requests.get(insta_search_next)
								else:
									insta_search_next = "None"
					else:
						print("No matching location found on Instagram.")	# Return empty list and display 'No Matches' label.


	print("\n\n------ DONE WITH HTTP REQUESTS ------\n")

	insta_pics_sorted_urls = [x for (y,x) in sorted(zip(insta_pic_likes,insta_pic_urls), reverse=True)]
	insta_pics_sorted_likes = [y for (y,x) in sorted(zip(insta_pic_likes,insta_pic_urls), reverse=True)]
	print(insta_pics_sorted_likes)

	return {'urls': insta_pics_sorted_urls, 'likes':insta_pics_sorted_likes}


	# Pretty Prints JSON:
	# print json.dumps(resp.json(), sort_keys=True, indent=4, separators=(',', ': '))