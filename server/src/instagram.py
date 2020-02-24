import sys
import os
import json

import instaloader

# Get instance
L = instaloader.Instaloader()
L.save_metadata = True
L.download_videos = False
L.download_pictures = False
L.compress_json = False

L.login('*****', '*****')

stories = L.get_stories('16094543855')

for i in stories:
    for item in i.get_items():
        L.download_storyitem(item, ':stories')


# for story in L.get_stories('thedrinkuptown'):
#     # story is a Story object
#     for item in story.get_items():
#         # item is a StoryItem object
#         print(item)
#         # L.download_storyitem(item, ':stories')


#from igramscraper.instagram import Instagram

#instagram = Instagram()

# instagram.login()

# account = instagram.get_account('thedrinkuptown')
# stories = instagram.get_stories(account.identifier)

# print(stories)

# print(account.identifier)


# with open('thedrinkuptown/thedrinkuptown.json') as json_file:
#     json_data = json.load(json_file)

# print(json_data)
