# A ToolKit for pdf

If you use pyinstaller for package, use this command:

pyinstaller --window --name=PDFTools -i y12.ico main.py --paths C:\Windows\System32\downlevel

After the .exe generated, put qt_material folder into the folder, because pyinstaller can not package it.

Add an ico file to avoid some anti-virus' alert, such as 360, Tencent

Add --paths to let your exe file be compatibility with win 7 when you built it on win 10

The icon is from https://sc.chinaz.com/tubiao/210125547220.htm
