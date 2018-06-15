# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

from django.shortcuts import render
import requests

from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools


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

# get info from google drive
def get_googleDrive_result(query):
    # jiralist = get_jira_result('Bodega')
    # confluencelist = get_confluence_result('Bodega')
    # googleList = getGoogleDriveList()
    # slacklist = get_slack_result('Bodega')
    # return render(request, 'search.html', {'jira': jiralist, 'confluence': confluencelist, 'slack':slacklist})

    SCOPES = 'https://www.googleapis.com/auth/drive.metadata.readonly'
    store = file.Storage('credentials.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('drive', 'v3', http=creds.authorize(Http()))

    # Call the Drive v3 API
    results = service.files().list(
        q="fullText contains '{}'".format(query), pageSize=10, fields="nextPageToken, files(webViewLink, name)").execute()
    items = results.get('files', [])
    list = []
    for f in items:
        myDict = {"name": f['name'], "link": f['webViewLink']}
        list.append(myDict)
    # if not items:
    #    	print('No files found.')
    # else:
    #    	print('Files:')
    #    for item in items:
    #        print('{0} ({1})'.format(item['name'], item['webViewLink']))

    return list


# get info from confluence
def get_confluence_result(query):
    headers = {
        'Accept': 'application/json',
    }

    params = (
        ('queryString', query),
        ('where', 'EN'),
        ('type', 'page'),
    )

    response = requests.get('https://rubrik.atlassian.net/wiki/rest/searchv3/1.0/search', headers=headers,
                            params=params, auth=('su.pu@rubrik.com', 'DKkNoDGe4oyoVAaHAxssC85A')).json()
    list = []
    for f in response['results']:
        myDict = {"name": f['title'].replace("@@@hl@@@", "").replace("@@@endhl@@@",""), "link": 'https://rubrik.atlassian.net/wiki' + f['url']}
        list.append(myDict)
    return list


# get info from jira
def get_jira_result(query):
    headers = {
        'Content-Type': 'application/json',
    }

    params = (
        ('q', query),
    )
    response = requests.get('https://rubrik.atlassian.net/rest/internal/2/productsearch/search', headers=headers,
                        params=params, auth=('su.pu@rubrik.com', 'DKkNoDGe4oyoVAaHAxssC85A')).json()
    list = []
    for f in response[0]['items']:
        myDict = {"name": f['title'], "link": f['url']}
        list.append(myDict)
    return list


# get info from slack
def get_slack_result():
    headers = {
        'Authorization': 'Bearer xoxp-3289038622-17534363783-17535191392-c15cef9256',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    params = (
        ('query', "bodega"),
        ('count', '10'),
        ('pretty', '1')
    )
    response = requests.get('https://slack.com/api/search.messages?', headers=headers, params=params).json()
    list = []
    for f in response['messages'.encode()].encode()['matches'].encode():
        myDict = {"name": f['text'].encode(), "link": f['permalink']}
        list.append(myDict)
    return list


def search_result(request):
    query ="query"
    if request.method=="POST":
        query=request.POST.get("query",None)
    google=get_googleDrive_result(query)
    # myDict = {"name": query, "link": "www.google.com"}
    # google.append(myDict)
    con=get_confluence_result(query)
    jira=get_jira_result(query)
    #slack=get_slack_result()

    print('confluence result: ', con)

    return render(request, 'Rubot/search.html', {"drive_data": google,"con_data": con,"jira_data": jira})

    #,"slack_data": slack