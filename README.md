# GPcrawler
Google Play Crawler

## Install
```
$ python3 setup.py [develop/install]
```

## WebDriver setting
Download ChoromeDriver from [https://sites.google.com/a/chromium.org/chromedriver/downloads].
- Chrome Version: `Version 91.0.4472.114 (Official Build) (64-bit)`
- Chrome Driver Version `ChromeDriver 91.0.4472.101`

## How to Run
```
# Run get all packages list
$ python3 main.py --list-range all --list-path dataset/all_apps

# Run popular packages list
$ python3 main.py --list-range popular --list-path dataset/popular_apps
```