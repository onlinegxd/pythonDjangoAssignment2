from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import json
import pandas as pd


def index(request):
    pages = ["https://etherscan.io/accounts", "https://etherscan.io/accounts/2", "https://etherscan.io/accounts/3",
             "https://etherscan.io/accounts/4"]
    accounts = []

    for page in pages:
        pagescrapped = requests.get(page, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(pagescrapped.content, 'html.parser')
        soup = soup.select("td a")
        for account in soup:
            accounts.append(account.get_text())

    q1 = ""
    q2 = ""
    q3 = ""
    q4 = ""
    q5 = ""

    for x in range(100):
        if x >= 80:
            q5 = q5 + accounts[x] + ','
            continue
        if x >= 60:
            q4 = q4 + accounts[x] + ','
            continue
        if x >= 40:
            q3 = q3 + accounts[x] + ','
            continue
        if x >= 20:
            q2 = q2 + accounts[x] + ','
            continue
        q1 = q1 + accounts[x] + ','

    query1 = {'address': q1}
    query2 = {'address': q2}
    query3 = {'address': q3}
    query4 = {'address': q4}
    query5 = {'address': q5}

    response1 = requests.get(
        "https://api.etherscan.io/api?module=account&action=balancemulti&apikey=2DD3UTR872V5QCTW5HHTCHHNCJFDPP8QIW",
        params=query1)
    response2 = requests.get(
        "https://api.etherscan.io/api?module=account&action=balancemulti&apikey=2DD3UTR872V5QCTW5HHTCHHNCJFDPP8QIW",
        params=query2)
    response3 = requests.get(
        "https://api.etherscan.io/api?module=account&action=balancemulti&apikey=2DD3UTR872V5QCTW5HHTCHHNCJFDPP8QIW",
        params=query3)
    response4 = requests.get(
        "https://api.etherscan.io/api?module=account&action=balancemulti&apikey=2DD3UTR872V5QCTW5HHTCHHNCJFDPP8QIW",
        params=query4)
    response5 = requests.get(
        "https://api.etherscan.io/api?module=account&action=balancemulti&apikey=2DD3UTR872V5QCTW5HHTCHHNCJFDPP8QIW",
        params=query5)

    responses = [response1, response2, response3, response4, response5]

    accnames = []
    accbalances = []

    for response in responses:
        resp = json.dumps(response.json())
        df = pd.read_json(resp)
        for acc in df["result"]:
            accnames.append(acc["account"])
            accbalances.append(int(acc["balance"]))

    context = {
        "accnames": accnames,
        "accbalances": accbalances,
    }

    return render(request, 'tophundredchart/index.html', context)
