import csv
import requests
from urllib.parse import urlparse
from itertools import islice

filename = "csv_files/passed_company_names.csv"
output   = "csv_files/url_filter.csv"
N = None

def with_scheme(u: str) -> str:
    u = (u or "").strip()
    if not u:
        return ""
    return u if urlparse(u).scheme else "http://" + u

with open(filename, "r", encoding="utf-8", newline="") as fin, \
     open(output,  "w", encoding="utf-8", newline="") as fout:

    reader = csv.DictReader(fin)
    fieldnames = reader.fieldnames + ["http_status", "reachable"]
    writer = csv.DictWriter(fout, fieldnames=fieldnames)
    writer.writeheader()

    it = reader if N is None else islice(reader, N)

    for row in it:
        url = row.get("website_url") or row.get("website_domain") or ""
        url = with_scheme(url)

        ok = False
        status = ""
        if url:
            try:
                resp = requests.head(url, timeout=5, allow_redirects=True)
                status = resp.status_code
                ok = 200 <= status < 400
                if not ok:
                    resp = requests.get(url, timeout=5, allow_redirects=True)
                    status = resp.status_code
                    ok = 200 <= status < 400
            except requests.RequestException:
                ok = False
                status = ""


        row["http_status"] = status
        row["reachable"]   = ok
        if ok:
            writer.writerow(row)
