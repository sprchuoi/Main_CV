import requests
import git
from api import HtmlToPdfDotNet

FILENAME = "NguyenQuangBinh_CV.pdf"
FILENAME_LOCAL = "MAIN_CV/build/CV_Local.pdf"

git.Repo.clone_from('https://github.com/sprchuoi/Main_CV.git', 'MAIN_CV')
response_tunnel = requests.get("http://localhost:4040/api/tunnels").json()
url = response_tunnel["tunnels"][0]["public_url"] + "/docs/"
print(f"\nURL Tunnel is: '{url}'.")
url = "https://www.html-to-pdf.net" # debug only
print(f"\nConverting to PDF from: '{url}'.")
pdf_content = HtmlToPdfDotNet().convert_pdf(url)

with open(FILENAME, "wb") as firstfile, open(FILENAME_LOCAL, "rb") as secondfile:
    # read content from second file 
    for line in secondfile: 
        # write content to frst file 
        firstfile.write(line)

print(f"Downloaded PDF file: '{FILENAME}'.")
