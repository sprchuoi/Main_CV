import re
import requests


class HtmlToPdfDotNet:
    def __init__(self) -> None:
        self.size = "A4"
        self.orientation = "Portrait"
        self.width = "1024"
        self.conversion_delay = "1"

    def convert_pdf(self, url: str) -> bytes:
        # Getting validation parameters
        res = requests.get("https://www.html-to-pdf.net/free-online-pdf-converter.aspx")
        view_state = re.search(
            r'id="__VIEWSTATE" value="(.*?)"', res.content.decode(), re.S | re.M
        ).group(1)
        event_validation = re.search(
            r'id="__EVENTVALIDATION" value="(.*?)"', res.content.decode(), re.S | re.M
        ).group(1)

        # Converting
        headers = {
            "authority": "www.html-to-pdf.net",
            "cache-control": "max-age=0",
            "sec-ch-ua": '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
            "sec-ch-ua-mobile": "?0",
            "upgrade-insecure-requests": "1",
            "origin": "https://www.html-to-pdf.net",
            "content-type": "application/x-www-form-urlencoded",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "navigate",
            "sec-fetch-user": "?1",
            "sec-fetch-dest": "document",
            "referer": "https://www.html-to-pdf.net/free-online-pdf-converter.aspx",
            "accept-language": "en-US,en;q=0.9,vi;q=0.8",
        }

        data = {
            "__EVENTTARGET": "ctl00$maincontent$BtnExport",
            "__VIEWSTATE": view_state,
            "__EVENTVALIDATION": event_validation,
            "ctl00$maincontent$TxtURL": url,
            "ctl00$maincontent$DdlPageSize": self.size,
            "ctl00$maincontent$DdlPageOrientation": self.orientation,
            "ctl00$maincontent$TxtPageWidth": self.width,
            "ctl00$maincontent$TxtConversionDelay": self.conversion_delay,
        }

        response = requests.post(
            "https://www.html-to-pdf.net/free-online-pdf-converter.aspx",
            headers=headers,
            data=data,
        )

        check = (
            response.status_code == 200
            and response.headers["Content-Type"] == "binary/octet-stream"
        )
        if check:
            return response.content
        else:
            raise Exception(f"Something went wrong. Response: \n{response.text}")
