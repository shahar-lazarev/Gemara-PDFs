import requests
from PyPDF2 import PdfMerger
import os

# Function to download a PDF from a given URL and save it
def download_pdf(url, filename):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded: {filename}")
    else:
        print(f"Failed to download: {url}")
        print(response.status_code)
        print(response.headers)
        print("\n")

# Function to collate multiple PDFs into a single PDF
def merge_pdfs(pdf_list, output):
    merger = PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    with open(output, 'wb') as f_out:
        merger.write(f_out)
    print(f"Created merged PDF: {output}")

# Main function to download and merge PDFs
def download_and_merge(base_url, page_range, output_pdf):
    # List to store the names of downloaded PDFs
    downloaded_pdfs = []

    for page_number in page_range:
        pdf_url = f"{base_url}{page_number}.pdf"  # Construct the URL
        filename = f"page_{page_number}.pdf"  # Name for the downloaded file
        download_pdf(pdf_url, filename)
        downloaded_pdfs.append(filename)

    # Merge the PDFs into one
    merge_pdfs(downloaded_pdfs, output_pdf)

    # Cleanup: delete downloaded individual PDFs
    for pdf in downloaded_pdfs:
        if os.path.exists(pdf):
            os.remove(pdf)
            print(f"Deleted: {pdf}")
        else:
            print(f"File not found, couldn't delete: {pdf}")

# Example usage:
# base_url = "https://beta.hebrewbooks.org/pagefeed/hebrewbooks_org_36083_"  # Replace with the actual base URL
base_url = "https://daf-yomi.com/Data/UploadedFiles/DY_Page/"  # Replace with the actual base URL
start_page = 2629
final_page = 2790
page_range = range(start_page, final_page+1)  # Download pages 1 to 60
output_pdf = "merged_document.pdf"  # The name of the final merged PDF

masechtot_ranges = [[1, 125], [126, 437], [438, 644], 
[645, 884], [885, 926], [927, 1099], [1100, 1209], 
[1210, 1287], [1288, 1354], [1355, 1413], [1414, 1474], 
[1475, 1529], [1530, 1580], [1581, 1822], [1823, 2044], 
[2045, 2224], [2225, 2354], [2355, 2450], [2451, 2628], 
[2629, 2790], [2791, 3025], [3026, 3261], [3262, 3611], 
[3612, 3835], [3836, 3881], [3882, 3977], [3978, 4127], 
[4128, 4152], [4153, 4390], [4391, 4607], [4608, 4888], 
[4889, 5007], [5008, 5072], [5073, 5137], [5138, 5191], 
[5192, 5232], [5264, 5406]]

names = ["Berakhot", "Shabbat", "Eruvin" "Pesachim", "Shekalim", "Yoma", "Sukkah", "Beitzah", "Rosh Hashanah", 
 "Taanit", "Megillah", "Moed Katan", "Chagigah", "Yevamot", "Ketubot", "Nedarim", "Nazir", "Sotah", 
 "Gittin", "Kiddushin", "Bava Kamma", "Bava Metzia", "Bava Batra", "Sanhedrin", "Makkot", "Shevuot", 
 "Avodah Zarah", "Horayot", "Zevachim", "Menachot", "Chullin", "Bechorot", "Arachin", "Temurah", "Keritot", 
 "Meilah", "Niddah"]

if __name__ == "__main__":
    pdf_name = 1
    index = 0
    for x,y in masechtot_ranges:
        this_range = range(x, y+1)
        download_and_merge(base_url, this_range, f"{names[index]}.pdf")
        pdf_name += 1
        index += 1





