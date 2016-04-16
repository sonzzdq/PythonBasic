# -*- coding: utf-8 -*-
import os
import win32com.client
import shutil
import time
import datetime
from docx import Document


# thêm số 0, ví dụ như 01, 02
def addZero(intNumber):
    if str(intNumber).isnumeric() == True and 0 < int(intNumber) < 10:
        return str("{0}{1}".format("0", intNumber))
    else:
        return intNumber


dNow = datetime.datetime.now()
nD = addZero(dNow.day)
nM = addZero(dNow.month)
nY = addZero(dNow.year)

# ngày báo cáo hôm trước
dOld = dNow - datetime.timedelta(days=1)
oD = addZero(dOld.day)
oM = addZero(dOld.month)
oY = addZero(dOld.year)

new_F = ('BÁO CÁO NGÀY %s.%s.%s ĐLĐQ.docx' % (nD, nM, nY))
old_F = ('BÁO CÁO NGÀY %s.%s.%s ĐLĐQ.docx' % (oD, oM, oY))

ph = '//10.173.88.16/Public/4. P.KH-KT/PHO PHONG (PT DIEU DO)/Phat hanh/BAO CAO NGAY/Nam 2016/TH %s/' % (oM)
dd = 'e:/BAO CAO C.TY - 2016/Dien luc Dinh Quan/01. Bao Cao Ngay/BAO CAO NGAY THANG %s-2016/' % (nM)

# flv = dd + new_F
# # copy new file
# os.chdir(dd)
shutil.copy2(src="{0}{1}".format(ph, old_F),
             dst="{0}{1}".format(dd, new_F))

#
# def tim_thaythe_all(Word_file, find_str, replace_str):
#     wdFindContinue = 1
#     wdReplaceAll = 2
#     app = win32com.client.DispatchEx("Word.Application")
#     app.Visible = 0
#     app.DisplayAlerts = 0
#     app.Documents.Open(Word_file)
#     app.Selection.Find.Execute(find_str, False, False, False, False, False, True, wdFindContinue, False, replace_str,
#                                wdReplaceAll)
#     app.ActiveDocument.Close(SaveChanges=True)
#     app.Quit()
#
#
# def search_replace_all(word_file, find_str, replace_str):
#     ''' replace all occurrences of `find_str` w/ `replace_str` in `word_file` '''
#     wdFindContinue = 1
#     wdReplaceAll = 2
#
#     # Dispatch() attempts to do a GetObject() before creating a new one.
#     # DispatchEx() just creates a new one.
#     app = win32com.client.DispatchEx("Word.Application")
#     app.Visible = 0
#     app.DisplayAlerts = 0
#     app.Documents.Open(word_file)
#
#     # expression.Execute(FindText, MatchCase, MatchWholeWord,
#     #   MatchWildcards, MatchSoundsLike, MatchAllWordForms, Forward,
#     #   Wrap, Format, ReplaceWith, Replace)
#     app.Selection.Find.Execute(find_str, False, False, False, False, False, \
#                                True, wdFindContinue, False, replace_str, wdReplaceAll)
#     app.ActiveDocument.Close(SaveChanges=True)
#     app.Quit()
#
#
# # f = 'c:/path/to/my/word.doc'
# # search_replace_all(f, 'string_to_be_replaced', 'replacement_str')
#
#
# tim = ['ngày 16 tháng 04 năm 2016', 'NGÀY 15/04/2016']
# thaythe = ['ngày 17 tháng 04 năm 2016', 'NGÀY 16/04/2016']
#
# for x in range(len(tim)):
#     search_replace_all(flv, find_str=tim[x], replace_str=thaythe[x])
