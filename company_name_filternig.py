import csv
from fuzzywuzzy import fuzz

INPUT = "csv_files/presales_data_sample.csv"
OUTPUT = "csv_files/passed_company_names.csv"

with open(INPUT, "r", encoding="utf-8", newline="") as infile, \
     open(OUTPUT, "w", encoding="utf-8", newline="") as outfile:

    reader = csv.DictReader(infile)
    writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
    writer.writeheader()

    current_key = None
    best_row = None
    best_score = -1

    for row in reader:
        key  = (row.get("input_company_name") or "").strip()
        cand = (row.get("company_name") or "").strip()
        if not key or not cand:
            continue

        score = fuzz.ratio(key.lower(), cand.lower())

        if current_key is None:
            current_key, best_row, best_score = key, row, score
        elif key != current_key:

            writer.writerow(best_row)
            current_key, best_row, best_score = key, row, score
        else:
            if score > best_score:
                best_row, best_score = row, score

    if current_key is not None:
        writer.writerow(best_row)

