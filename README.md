# Google Scholar API

This repository contains a simple Flask-based API that allows users to retrieve article data from Google Scholar based on a search query.

## Features

- **Simple API Endpoint**: The API provides a single GET endpoint `/get_articles` which accepts a search query and returns a list of articles.
- **Hosted API Endpoint**: The API is hosted and can be accessed remotely at `https://wmohamed.pythonanywhere.com/get_articles?search_query=search%20query`. Replace `search%20query` with your desired search term, URL encoded.
- **Web Scraping**: Utilizes `requests` and `BeautifulSoup` to scrape Google Scholar search results.

## How to Use

To use the hosted API, simply make a GET request to the following URL with your search query:
- https://wmohamed.pythonanywhere.com/get_articles?search_query=your_search_term
Replace `your_search_term` with the search term you wish to query, ensuring it is URL encoded.

For local development:

1. Clone the repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Run `app.py` to start the Flask server.
4. Make a GET request to the local endpoint with the search query, for example: `http://localhost:8080/get_articles?search_query=your_search_term`.

## Endpoints

- `GET /get_articles`: Accepts a `search_query` parameter and returns a JSON array of articles.

## Local Development

To set up the API for local development:

1. Ensure you have Python 3.6+ installed on your system.
2. Install Flask and other required libraries using the provided `requirements.txt`.
3. Run the Flask application with `python app.py`.

## Dependencies

- Flask
- BeautifulSoup
- requests

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your proposed changes.

## License

This project is open-sourced under the MIT License. See the LICENSE file for more information.

## Disclaimer

This API is for educational purposes only. Scraping Google Scholar may be against their terms of service. Use this API at your own risk.

## Contact

If you have any questions or comments about this API, please open an issue in this repository.

