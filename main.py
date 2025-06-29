import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


def scrape_books_toscrape():
    """
    Scrapes book titles, prices, ratings, and availability from books.toscrape.com,
    including pagination.

    Returns:
        pandas.DataFrame: A DataFrame containing the scraped book data,
                          or None if an error occurred.
    """
    base_url = "http://books.toscrape.com/catalogue/page-{}.html"
    page_num = 1
    all_books_data = []

    print("Starting scraping process from Books to Scrape...")

    while True:
        url = base_url.format(page_num)
        print(f"Fetching page: {url}")

        headers = {
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            html_content = response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching page {page_num}: {e}")

            if response.status_code == 404:
                print("Reached the end of pagination (404 Not Found).")
            break

        soup = BeautifulSoup(html_content, 'html.parser')

        products = soup.find_all('article', class_='product_pod')
        if not products:
            print(
                f"No products found on page {page_num}. Assuming end of pagination."
            )
            break

        for product in products:
            try:

                title_tag = product.find('h3').find('a')
                title = title_tag['title'].strip()

                price_tag = product.find('p', class_='price_color')
                price = price_tag.get_text(strip=True).replace('Â£', '£')

                rating_tag = product.find(
                    'p', class_=lambda c: c and 'star-rating' in c)
                rating = rating_tag['class'][1] if rating_tag else 'N/A'

                availability_tag = product.find('p',
                                                class_='instock availability')
                availability = availability_tag.get_text(
                    strip=True) if availability_tag else 'N/A'

                all_books_data.append({
                    'Title': title,
                    'Price': price,
                    'Rating': rating,
                    'Availability': availability
                })
            except AttributeError as e:
                print(f"Skipping a product due to missing element: {e}")
                continue

        page_num += 1
        time.sleep(1)

    if not all_books_data:
        print("No book data was extracted.")
        return None

    df = pd.DataFrame(all_books_data)

    rating_map = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
    df['Rating_Numeric'] = df['Rating'].map(rating_map).fillna(0).astype(int)

    print("\n--- Scraped Data Preview ---")
    print(df.head())
    print(f"\nTotal books scraped: {len(df)}")

    return df


if __name__ == "__main__":
    scraped_books_df = scrape_books_toscrape()

    if scraped_books_df is not None:
        output_csv_filename = "books_data.csv"
        try:
            scraped_books_df.to_csv(output_csv_filename,
                                    index=False,
                                    encoding='utf-8')
            print(f"\nSuccessfully saved data to '{output_csv_filename}'")
        except IOError as e:
            print(f"Error saving file: {e}")
    else:
        print("\nScraping failed or no data was extracted.")
