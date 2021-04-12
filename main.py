'''Stack overflow scrapper'''

import requests
from bs4 import beautifulsoup
import json

'''fetching host site information'''
response = requests.get('https://stackoverflow.com/')                   

'''parsing and extracting information'''
if response.status_code == 200:
    content = BeautifulSoup(response.content, 'html.parser')
    questions = content.select('.question-summary')
    result = []

    for question in questions:
        topic = question.select('.question-hyperlink')[0].get_text()
        url   = question.select('.question-hyperlink')[0].get('href')
        views = question.select('.views .mini-counts span')[0].get_text()
        answers = question.select('.status .mini-counts span')[0].get_text()
        votes = question.select('.votes .mini-counts span')[0].get_text()

'''saving the information'''
        single = {'toipc': topic, 'url': url, 'views': views, 'answers': answers, 'votes': votes}  
        result.append(single)
        with open('stackoverflow.json','w') as f:
            json.dumps(result,f)

else:
    print(response.status_code)