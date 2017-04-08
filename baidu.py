# _*_ coding:utf-8 _*_
import webbrowser
import pyperclip

kw = pyperclip.paste()
target_url = []

# baidu
target_url_baidu = ('https://www.baidu.com/s?ie=utf-8&wd=' + kw)
target_url.append(target_url_baidu)

# #Google
# target_url_google = ('https://www.google.com.hk/search?newwindow=1&safe=strict&q=' + kw)
# target_url.append(target_url_google)

for url in target_url:
    webbrowser.open_new_tab(url)