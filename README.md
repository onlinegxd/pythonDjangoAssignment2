# Top 100 Accounts by Ethereum balance from https://etherscan.io/ using Django

### Installation
Copy from source
```bash
git clone https://github.com/onlinegxd/pythonDjangoAssignment2
```

### Usage

```python
# Used for web-scrapping top accounts
from bs4 import BeautifulSoup
import requests
import json
import pandas as pd
# For path
from django.urls import path
```

### Examples

Start an application webserver

After successful run 3 charts would be available

Data observed is in-real time so page might load for 5-7 seconds

No DataBase used

The main model in Database is Task model

Usage examples:

(/index) - The only route available
![image](https://user-images.githubusercontent.com/80266425/153492146-6ddc0b8e-81ad-41c5-ba39-4da1ac07885e.png) - bar chart
![image](https://user-images.githubusercontent.com/80266425/153492274-01e7257b-fd17-4b4d-8e01-854e7692ac15.png) - pie chart
![image](https://user-images.githubusercontent.com/80266425/153492331-f24bdd4d-a812-499a-866c-576d17fd79e8.png) - line chart




