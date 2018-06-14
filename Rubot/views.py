# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import requests
# Create your views here.


#
# def getJiraList():
#     pass
#
# def getConfluenceList():
#     pass
#
# def getGoogleDriveList():
#     pass


def manageSearch(request):
    # jiralist = get_jira_result('Bodega')
    # confluencelist = get_confluence_result('Bodega')
    #googleList = getGoogleDriveList()
    # slacklist = get_slack_result('Bodega')
    # return render(request, 'search.html', {'jira': jiralist, 'confluence': confluencelist, 'slack':slacklist})
    return render(request, 'Rubot/search.html')

#get info from confluence
# def get_confluence_result(query):
#    headers = {
#        'Accept': 'application/json',
#    }
#
#    params = (
#        ('queryString', query),
#        ('where', 'EN'),
#        ('type', 'page'),
#    )
#
#    response = requests.get('https://rubrik.atlassian.net/wiki/rest/searchv3/1.0/search', headers=headers,
#                            params=params, auth=('su.pu@rubrik.com', 'DKkNoDGe4oyoVAaHAxssC85A')).json()
#    print response['results'][0]['id']
#    print response['results'][0]['title']
#    print response['results'][0]['bodyTextHighlights']
#
# def get_jira_result(query):
#    headers = {
#        'Content-Type': 'application/json',
#    }
#    params = (
#        ('q', query),
#    )
#    response = requests.get('https://rubrik.atlassian.net/rest/internal/2/productsearch/search', headers=headers,
#                            params=params, auth=('su.pu@rubrik.com', 'DKkNoDGe4oyoVAaHAxssC85A')).json()
#    print response[0]['items'][0]['title']
#    print response[0]['items'][0]['url']
#
# def get_slack_result(query):
#    headers = {
#        'Authorization': 'Bearer xoxp-3289038622-17534363783-17535191392-c15cef9256',
#        'Content-Type': 'application/x-www-form-urlencoded',
#    }
#    params = (
#        ('query', query),
#        ('count', '10'),
#        ('pretty', '1')
#    )
#    response = requests.get('https://slack.com/api/search.messages?', headers=headers, params=params).json()
#    print(response)
#    print response['messages']['matches'][0]['permalink']
#    print response['messages']['matches'][0]['text']


