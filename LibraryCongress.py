import requests

# Endpoint URL for searching books by title
start = "https://www.loc.gov/search/?q="
endpoint = "&fo=json&at=facets"
def search_books_by_title(title):
    # Query parameters
    params = {
        "q": title,
        "fo": "json",
        "at": "results,bibframe",
        "c": 1  # Maximum number of results to retrieve (adjust as needed)
    }


    try:
        response = requests.get(start, params=params)
        response.raise_for_status()
        data = response.json()
        print(data)
        table_data = []
        #print(data)
        # Prepare table data
        table_data = []
        # Display table
        bibframe_data = []
        for result in data["results"]:
            if "bibframe" in result:
                bibframe_data.append(result["bibframe"])

        return bibframe_data
    except requests.exceptions.RequestException as e:

      print(e)

    # Example usage
book_title = "A Critical Study of Self-Help and Self-Improvement Practices: Textual, Discursive, and Ethnographic Perspectives	"
bibframe_results = search_books_by_title(book_title)
print(bibframe_results)
for bibframe_data in bibframe_results:
        # Extract desired information from the BIBFRAME data
        # and perform further processing or analysis
    print(bibframe_data)



# Example usage
