# snoopy

* downloads
	* snoopy.htb/download
	* snoopy.htb/download?file=announcement.pdf (lfs??)
* contact (mail)
	* mail doesn't work at the top
	* failed to load php library when submitting (uploading library for rce??)

## /download?file=<>

### working examples

* /download?file=announcement.pdf
* /download?file=snoopysec_marketing.mp4

zips file into the following hierarchy
## returned (downloaded) zip
press_package 
└── <file>

it doesn't seem to be vulnerable.

## contact

I've found a js validator for the php-email-form library with a link to a setup website.
From it I gathered /forms/contact.php which returns the "Unable to load the "PHP Email Form" Library!" error message

contact.php may contain credentials if smtp was configured meaning that if I can use the `/download?file` to get `contact.php`
I might be able to get credentials that are also used for ssh for example (failed)

After reading contact.php it seems that I can just create the same request I pass to contact.php to php-email-form.php directly
but php-email-form.php doesn't seem to exist.

## options

* upload a file to php-email-form.php's path (win anyways because its a php server)
* download contact.php for stmp credentials

## dns

`/contact.html` has an attention warning at the top stating that mail.snoopy.htb is offline due to DNS records migration to a new domain.

Also nmap shows that the webserver's ip also hosts the dns service:

> 53/tcp open  domain
> | dns-nsid:
> |_  bind.version: 9.18.12-0ubuntu0.22.04.1-Ubuntu

By using `dig @<ip> snoopy.htb any` I get a list of domains and find:

ns1.snoopy.htb
ns2.snoopy.htb

```shell
./get_file.sh /etc/passwd | python3 -c "import sys; li = [x.split(':')[0] for x in sys.stdin.read().splitlines() if 'nologin' not in x and 'false' not in x]; print(li)"
```
