import requests

# List of URLs in the correct dependency order
urls = [
    "https://code.jquery.com/jquery-2.2.4.min.js",
    "https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.9.1/underscore-min.js",
    "https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.6/d3.min.js",
    "https://cdnjs.cloudflare.com/ajax/libs/d3-legend/1.13.0/d3-legend.min.js",
    "https://raw.githubusercontent.com/looker-open-source/viz-spider-marketplace/master/spider.js"
]

output_filename = "merged_spider.js"

print(f"Downloading and merging {len(urls)} files...")

with open(output_filename, "wb") as outfile:
    for url in urls:
        print(f"Fetching: {url}")
        try:
            response = requests.get(url)
            response.raise_for_status()
            
            # Add a separator comment for clarity
            outfile.write(f"\n/* --- Source: {url} --- */\n".encode('utf-8'))
            outfile.write(response.content)
            outfile.write(b"\n") # Ensure newline between files
        except Exception as e:
            print(f"Error fetching {url}: {e}")

print(f"Success! Created {output_filename}")
