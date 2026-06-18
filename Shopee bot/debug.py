import hashlib
import time
import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()
APP_ID = os.getenv("APP_ID")
SECRET = os.getenv("SECRET")

BASE_URL = "https://open-api.affiliate.shopee.com.br/graphql"

query = '{ productOfferV2(keyword: "roupa", listType: 1, sortType: 5, limit: 3) { nodes { productName } } }'
payload = {"query": query}

timestamp = str(int(time.time()))
body_str  = json.dumps(payload, separators=(',', ':'), ensure_ascii=False)
raw       = APP_ID + timestamp + body_str + SECRET
signature = hashlib.sha256(raw.encode('utf-8')).hexdigest()

headers = {
    "Content-Type": "application/json",
    "Authorization": f"SHA256 Credential={APP_ID}, Timestamp={timestamp}, Signature={signature}"
}

# Envia o body como string, não como dict
response = requests.post(BASE_URL, data=body_str.encode('utf-8'), headers=headers)
print(response.json())