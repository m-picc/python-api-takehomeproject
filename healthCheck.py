# healthcheck script to verify api is responding.

import sys
import http.client

try:
    conn = http.client.HTTPConnection("localhost", 8000)
    conn.request("GET", "/")
    response = conn.getresponse()
    if response.status != 200:
        sys.exit(1)  # Unhealthy
    sys.exit(0)      # Healthy
except Exception:
    sys.exit(1)  # Unhealthy
