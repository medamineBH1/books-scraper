<<<<<<< HEAD
# books-scraper
=======
# 📚 Books to Scrape Web Scraper 🤖

A Python web scraper that extracts book data from [Books to Scrape](http://books.toscrape.com), a demo website designed for web scraping practice.

## ✨ Features

- Scrapes all books across multiple pages automatically
- Extracts book title, price, rating, and availability
- Converts star ratings to numeric values (1-5)
- Exports data to CSV format
- Includes error handling and rate limiting

## 📦 Data Extracted

The scraper collects the following information for each book:
- **Title**: Book title
- **Price**: Price in British Pounds (£)
- **Rating**: Star rating (One, Two, Three, Four, Five)
- **Availability**: Stock status
- **Rating_Numeric**: Numeric conversion of star rating (1-5)

## 📝 Output

The script generates a `books_data.csv` file containing all scraped book data, ready for analysis or further processing.

## 🛠️ Requirements

- Python 3.11+
- beautifulsoup4
- pandas
- requests

## 🚀 Usage

Run the scraper:
```bash
python main.py
```

The script will automatically:
1. Scrape all available pages
2. Extract book information
3. Save data to `books_data.csv`
4. Display progress and summary statistics

## ⚙️ Technical Details

- Uses respectful scraping practices with 1-second delays between requests
- Handles pagination automatically
- Includes proper error handling for network issues
- Uses browser-like headers to avoid blocking

## 📊 Sample Output

The CSV file contains approximately 1000 books with columns:
```
Title,Price,Rating,Availability,Rating_Numeric
"A Light in the Attic","£51.77","Three","In stock",3
"Tipping the Velvet","£53.74","One","In stock",1
...
```
>>>>>>> a032494 (Add Web Scraper Script)
