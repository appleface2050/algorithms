#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import hashlib
import json

api_identifier = "1"
app_key = "165c6bc59e1b10c4fe794ae90fa6bb9f"
data = {"api_identifier": api_identifier,
        "guid":"6EC552171FD5389CE934CE344CCE0323",
        "service":"userData"
        }
params = "|".join(sorted(data.values())) + "|165c6bc59e1b10c4fe794ae90fa6bb9f"

signature = hashlib.md5(params).hexdigest()
data["signature"] = signature

r = requests.post('http://service.bluestacks.cn/user.html',
                 params=data, timeout=3)
content = json.loads(r.content)
print content.get("result").get("userName")
