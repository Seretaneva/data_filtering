import csv
from itertools import islice

filename = "csv_files/url_filter.csv"
output   = "csv_files/primary_email_output.csv"
N = None


with open(filename, "r", encoding="utf-8", newline="") as fin, \
     open(output,  "w", encoding="utf-8", newline="") as fout:

    reader = csv.DictReader(fin)
    fieldnames = reader.fieldnames + ["http_status", "reachable"]
    writer = csv.DictWriter(fout, fieldnames=fieldnames)
    writer.writeheader()

    it = reader if N is None else islice(reader, N)

    for row in it:
        email = row.get("primary_email", "").strip()
        if email:
            writer.writerow(row)

