# _*_ coding:utf-8 _*_
import webbrowser
import pyperclip

kw = pyperclip.paste()
target_url = ('https://www.baidu.com/s?ie=utf-8&wd=' + kw)
webbrowser.open_new_tab(target_url)