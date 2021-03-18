import os
import requests

# default_url = "https://jackblk.github.io/my_cv"
response_tunnel = requests.get("http://localhost:4040/api/tunnels").json()
url_tunnel = response_tunnel["tunnels"][0]["public_url"]
url = (
    "https://www.web2pdfconvert.com/convert/web/to/pdf?storefile=true&"
    "filename=LeThienTrung_CV"
    f"&url={url_tunnel}"
    "&Zoom=1&FixedElements=absolute&ViewportWidth=1366&ViewportHeight=800&PageOrientation=portrait&PageSize=a4&MarginLeft=0&MarginRight=0"
)
response = requests.get(url).json()
pdf_link = response["Files"][0]["Url"]
print(pdf_link)
print(f"URL Tunnel is: {url_tunnel}")
os.system(f"wget {pdf_link} -c")
