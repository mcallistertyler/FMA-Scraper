#!/bin/sh
read -p "Choose Genre": genre
read -p "Choose number of pages": pages
echo "Finding $genre with $pages pages"
python fma-scrape.py $genre $pages 
echo "Scraped selected pages."
python2 extract.py -u $genre
echo "Extracted all links from pages."
sed '/mp3/!d' ${genre}-url.csv >> ${genre}.txt
echo "Filtered out non mp3 download links."
wget -i ${genre}.txt
echo "Downloads finished."
