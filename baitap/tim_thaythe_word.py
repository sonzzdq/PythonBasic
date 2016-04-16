import win32com.client
import os
from docx import Document
import time

f = 'BÁO CÁO NGÀY 13.04.2016 ĐLĐQ.docx'
dd = 'e:/BAO CAO C.TY - 2016/Dien luc Dinh Quan/01. Bao Cao Ngay/BAO CAO NGAY THANG 04-2016/'

# -*- coding: utf-8 -*-
os.chdir(dd)

import os
import win32com.client

app = win32com.client.Dispatch("Word.Application")
# nếu không muốn word hiển thị thì app.Visible = 0
app.Visible = 1
app.DisplayAlerts = 0

def search_replace(file, find_str, replace_str):
    app.Documents.Open(file)
    app.Selection.Find.Text = find_str
    found = app.Selection.Find.Execute()
    doc = app.ActiveDocument
    # time.sleep(5)
    if found:
        app.Selection.TypeText(replace_str)
        doc.Close(SaveChanges=True)
    else:
        doc.Close(SaveChanges=False)
    return found
# định dạng đường dẫn file \\
flv = os.getcwd() + '\\' + f
# print(f)
tim = ['ngày 10 tháng 04 năm 2016', 'NGÀY 09/04/2016']
thaythe= ['ngày 14 tháng 04 năm 2016','NGÀY 13/04/2016']

for x in range(len(tim)):
    search_replace(flv, find_str=tim[x], replace_str=thaythe[x])


app.Quit()



# # setting up shortcuts
# word = win32com.client.Dispatch("Word.Application")
# word.Visible = False
# word.DisplayAlerts = False
# doc = word.Documents.Open(os.getcwd() + '\\BÁO CÁO NGÀY 09.04.2016 ĐLĐQ.docx')
# w = win32com.client.constants
# # style_names = set(
# #     s.NameLocal for s in doc.Styles)  # because doc.Styles is a container for all the Styles Object Instance
# find = doc.Content.Find
# #
# # # creating the needed styles if not there already
# # if "Italic" not in style_names:
# #     doc.Styles.Add("Italic", w.wdStyleTypeCharacter)
# #     # "ItalicBi" is the same as "Italic", but for languages that go Right to Left.
# #     doc.Styles("Italic").Font.ItalicBi = True
# #     print("Italic style was created")
# # if "Bold" not in style_names:
# #     doc.Styles.Add("Bold", w.wdStyleTypeCharacter)
# #     doc.Styles("Bold").Font.BoldBi = True
# #     print("Bold style was created")
# #
# # style_names = set(
# #     s.NameLocal for s in doc.Styles)  # because doc.Styles is a container for all the Styles Object Instance
#
# find = word.Selection.Find
# find.ClearFormatting()
# find.Replacement.ClearFormatting()
# find.Text = 'ngày 10 tháng 04 năm 2016'
# find.Replacement.Text = 'ngày 13 tháng 04 năm 2016'
# find.Forward = True
# find.Wrap = win32com.client.constants.wdFindContinue
# find.Execute(Replace=win32com.client.constants.wdReplaceAll)
#
# # # Search & Replacing
# # find.ClearFormatting()
# # find.Font.Italic = True # set the style searched
# # find.Format = True # say that the format is the criteria
# # find.Replacement.ClearFormatting()
# # find.Replacement.Style = doc.Styles("Bold")
# # find.Execute(Forward=True, Replace=w.wdReplaceAll, FindText='',
# # ReplaceWith='\emph{^&}')
#
# # Save and Quit
# word.ActiveDocument.SaveAs(os.getcwd() + '\\italic_modified.docx')
# word.Quit()  # releases Word object from memory
# print("We are done.")
