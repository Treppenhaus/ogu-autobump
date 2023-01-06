# ogu-autobump
autobump for ogu.gg using selenium

this is a quick and dirty solution (like using undetected-chromedriver to bypass selenium)

---

## how to set up

0. install libraries
`pip3 install selenium`
`pip3 install undetected-chromedriver`


1. download chromedriver and name file chromedriver.exe (delete the one thats there already)

> download original chromedriver for your chrome version from here:
[https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)



2. open a.py file and make your changes (input account, url, message etc.)
valid config example:
```python
username = "treppi" #ur ogu.gg username
password = "" #ur password
threadurl = "https://ogu.gg/Thread-%E2%80%BC%E2%AD%90CHEAPEST-RANKS-RANKED-READY-ACCOUNTS-NO-SKINS-%E2%AD%90%E2%80%BC" #ur threadurl
message = "dm me on discord: treppi#9999" # message to send
bump_delay = 60 * 31 # 31 minutes
```

3. run a.py file using python `python3 a.py`

4. leave program running in the background, use a server if you want it running all the time


