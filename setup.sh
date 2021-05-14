#!/bin/bash

python3 -m virtualenv env
source env/bin/activate
pip install -r requirements.txt

mkdir -p data/primary data/lists/csv data/lists/pdf data/awards data/paradise_papers

#Downloading white and blacklists
wget 'http://companies.defenceindex.org/docs/Heatmap%20-%202015%20Defence%20Companies%20Anti-Corruption%20Index.csv' -O data/lists/csv/defence_companies_anti_corruption_index.csv
wget 'https://crueltyfree.peta.org/wp-content/uploads/cruelty-free-companies-united-states.pdf' -O data/lists/pdf/cruelty-free-companies-united-states.pdf
wget 'https://crueltyfree.peta.org/wp-content/uploads/companies-working-for-regulatory-change.pdf' -O data/lists/pdf/companies-working-for-regulatory-change.pdf
wget 'https://crueltyfree.peta.org/wp-content/uploads/companies-do-test.pdf' -O data/lists/pdf/companies-do-test.pdf
wget 'https://crueltyfree.peta.org/wp-content/uploads/companies-dont-test.pdf' -O data/lists/pdf/companies-dont-test.pdf
wget 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQ1Rrb2LHfDTZFZ1k8OT2an6j86PhdqCsJM7XnDMwadFpEdhbB6I0Cg1n2opekdFOJh8JyHF43sJgcs/pub?gid=0&single=true&output=csv' -O data/lists/csv/fossil-fuels.csv

#Downloading scrapped data + russel + sp500
wget 'https://spreadsheets.google.com/feeds/download/spreadsheets/Export?key=1sB3rhEAH33KHhEjI0GR89g-0mHmzDAuv2HT2tKKymU8&exportFormat=xlsx' -O data/scrapped_data.xlsx

#Downloading paradise papers
wget 'https://offshoreleaks-data.icij.org/offshoreleaks/csv/csv_bahamas_leaks.2017-12-19.zip#_ga=2.44360550.376239357.1620911106-1321783456.1620911106' -O data/paradise_papers/bahamas_leaks.zip
mkdir data/paradise_papers/bahamas_leaks
unzip data/paradise_papers/bahamas_leaks.zip -d data/paradise_papers/bahamas_leaks/
rm data/paradise_papers/bahamas_leaks.zip

wget 'https://offshoreleaks-data.icij.org/offshoreleaks/csv/csv_offshore_leaks.2018-02-14.zip#_ga=2.215051806.808273460.1620911445-269100556.1620911445' -O data/paradise_papers/offshore_leaks.zip
mkdir data/paradise_papers/offshore_leaks
unzip data/paradise_papers/offshore_leaks.zip -d data/paradise_papers/offshore_leaks/
rm data/paradise_papers/offshore_leaks.zip

wget 'https://offshoreleaks-data.icij.org/offshoreleaks/csv/csv_panama_papers.2018-02-14.zip#_ga=2.176122155.808273460.1620911445-269100556.1620911445' -O data/paradise_papers/panama_papers.zip
mkdir data/paradise_papers/panama_papers
unzip data/paradise_papers/panama_papers.zip -d data/paradise_papers/panama_papers/
rm data/paradise_papers/panama_papers.zip

wget 'https://offshoreleaks-data.icij.org/offshoreleaks/csv/csv_paradise_papers.2018-02-14.zip#_ga=2.176122155.808273460.1620911445-269100556.1620911445' -O data/paradise_papers/paradise_papers.zip
mkdir data/paradise_papers/paradise_papers
unzip data/paradise_papers/paradise_papers.zip -d data/paradise_papers/paradise_papers/
rm data/paradise_papers/paradise_papers.zip


