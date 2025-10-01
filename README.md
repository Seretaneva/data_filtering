This project is a 3-step Python workflow for cleaning and validating supplier data:

Entity Resolution – Used fuzzy string matching to pick the best candidate company name for each supplier input, removing duplicates and inconsistencies.

Website Validation – Checked supplier websites with requests to confirm they are live and reachable, keeping only real, active companies.

Primary Email Filtering – Extracted suppliers with valid primary email addresses to create a clean, actionable contact list.

