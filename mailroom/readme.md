# HTB Mailroom Solution

* Setup mailroom.htb in /etc/hosts
* Browse, try finding domains, inputs features etc.
* No subdomains from htmls, only inputs are in contacts
* SQLI, XSS? XSS on all inputs in the next order `title`, `message`, `email`
* Create a simple framework that generates an xss and uploads it
to get a proper mail [xss.py](xss.py) and open
a simple server `python3 -m http.server & python3 xss.py && fg`
* I get request from `127.0.0.1` from time to time
meaning I can execute js on the host
* Useful information that may change between me and the host is
  * Access to certain paths
  * Cookies
  * index.html may differ based on the client