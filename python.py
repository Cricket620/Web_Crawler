#THIS IS A WORK IN PROGRESS - NOT FUNCTIONAL
#This script pulls all URLs in HTML and prints them.

page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')
url, endpos = get_next_target(page)

def get_next_target(s): url, end_quote
    start_link = s.find('<a href=')
    if start_link == -1:
        return None, 0
    else:
        start_quote = s.find('"', start_link)
        end_quote = s.find('"', start_quote+1)
        url = s[start_quote+1:end_quote]
        return url, end_quote

def print_all_links(page):
    while True:
        url, endpos = get_next_target(page)
        if url:
            print url
            page = page[endpos:]
        else:
            break
