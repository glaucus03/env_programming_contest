import platform
import webbrowser
import sys
print(sys.version_info)
print(platform.uname().release.lower())

instance = webbrowser.GenericBrowser("explorer.exe")
webbrowser.register("exploler",None,instance,preferred=True)

webbrowser.open_new_tab("https://github.com/online-judge-tools/oj/blob/master/onlinejudge_command/utils.py")
print(webbrowser.get())