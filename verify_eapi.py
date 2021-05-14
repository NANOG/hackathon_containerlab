import json

import pyeapi


conn = pyeapi.connect(
    host="127.0.0.1", port="8443", transport="https", username="admin", password="admin"
)

print(json.dumps(conn.execute(["show version"]), indent=4))
