#! /usr/bin/env python3
# -*- coding: utf-8 -*-

#=== libraries import. =================================================================================================

# from gi.repository import Gtk
# import re
# import sys
# import urllib

#=== functions. ========================================================================================================

# def FileFilter (Btn) :
#   FltPtn = Bdr.get_object('Ety_FltPtn').get_text()
#   IvtFlt = Bdr.get_object('CckBtn_IvtFlt').get_active() # 'IvtFlt' = Inverted Filter.
#   IsOrg = Bdr.get_object('RdoBtn_Org').get_active()  # 'IsOrg' = Is Original.

#   if not FltPtn :
#     Alert('請輸入過濾條件。')

#     return -1

#   for i in range(len(LstSt_FlNm) - 1, -1, -1) :
#     Tgt = LstSt_FlNm[i][0] if IsOrg else LstSt_FlNm[i][1] # 'Tgt' = Target.

#     if (IvtFlt and re.search(FltPtn, Tgt) is None) or (not IvtFlt and re.search(FltPtn, Tgt) is not None):
#         LstSt_FlNm.remove(LstSt_FlNm[i].iter)

# def NameSerialize (Btn) :
#   SttNbr = Bdr.get_object('SpnBtn_SttNbr').get_value_as_int() # 'SttNbr' = Start Number.
#   PdNbr = Bdr.get_object('SpnBtn_PdNbr').get_value_as_int() # 'PdNbr' = Padding Number.
#   IsExtKp = Bdr.get_object('CckBtn_KpExt').get_active() # 'IsExtKp' = Is Extend name Kept.

#   for Idx, FlNm in enumerate(LstSt_FlNm) :
#     if not IsExtKp :
#       FlNm[1] = str(Idx + SttNbr).zfill(PdNbr)

#       continue;

#     StrPt = os.path.splitext(FlNm[1]) # 'StrPt' = String Parts
#     FlNm[1] = str(Idx + SttNbr).zfill(PdNbr) + StrPt[1]

# def StringReplace (Btn) :
#   TgtStr = Bdr.get_object('Ety_TgtStr').get_text()
#   RplcStr = Bdr.get_object('Ety_RplcStr').get_text()

#   if TgtStr is '' :
#     Alert('請輸入目標字串。')
#     return -1

#   for FlNm in LstSt_FlNm :
#     if TgtStr in FlNm[1] :
#       FlNm[1] = FlNm[1].replace(TgtStr, RplcStr)

# def StringPend (Btn) :
#   PndStr = Bdr.get_object('Ety_PndStr').get_text()
#   IsBfr = Bdr.get_object('RdoBtn_Bfr').get_active()
#   IsExtKp = Bdr.get_object('CckBtn_ExtKp').get_active()

#   if PndStr is '' :
#     Alert('請輸入字串。')
#     return -1

#   for FlNm in LstSt_FlNm :
#     if IsBfr :
#       FlNm[1] = PndStr + FlNm[1]
#     elif not IsExtKp :
#       FlNm[1] = FlNm[1] + PndStr
#     else :
#       StrPt = os.path.splitext(FlNm[1]) # 'StrPt' = String Parts
#       FlNm[1] = StrPt[0] + PndStr + StrPt[1]

# def FileRelist (Btn) :
#   TrVw_FlNmLst = Bdr.get_object('TrVw_FlNmLst')

#   for FlNm in LstSt_FlNm :
#     FlNm[1] = FlNm[0]

# def Apply (Btn) :
#   Btn_DirExpd = Bdr.get_object('Btn_DirExpd')
#   NtBk_TbBx = Bdr.get_object('NtBk_TbBx')
#   Btn_Rst = Bdr.get_object('Btn_Rst')
#   Btn_Apl = Bdr.get_object('Btn_Apl')

#   Btn_DirExpd.set_sensitive(False)
#   NtBk_TbBx.set_sensitive(False)
#   Btn_Rst.set_sensitive(False)
#   Btn_Apl.set_sensitive(False)

#   for FlNm in LstSt_FlNm :
#     if FlNm[1] == FlNm[0] :
#       FlNm[2] = '忽略。'
#     elif not os.path.isfile(WkPth + FlNm[0]) :
#       FlNm[2] = '原始檔案不存在。'
#     elif os.path.isfile(WkPth + FlNm[1]) :
#       FlNm[2] = '將更換成的檔案已經存在。'
#     else :
#       os.rename(WkPth + FlNm[0], WkPth + FlNm[1])

#       FlNm[2] = '成功！'

#   Btn_DirExpd.set_sensitive(True)
#   NtBk_TbBx.set_sensitive(True)
#   Btn_Rst.set_sensitive(True)
#   Btn_Apl.set_sensitive(True)

#=== main process. =====================================================================================================

# PgmPth = os.path.dirname(__file__)
# Bdr = Gtk.Builder()

# Bdr.add_from_file(PgmPth + '/../DSN/gui.glade')

# Win = Bdr.get_object('Win_MrName')

# Win.set_icon_from_file(PgmPth + '/../DSN/icon.ico')

# #==== initialize TreeView. ====

# ClRdrTxt = Gtk.CellRendererText()
# TrVw_FlNmLst = Bdr.get_object('TrVw_FlNmLst')
# LstSt_FlNm = Bdr.get_object('LstSt_FlNm')

# ClRdrTxt.set_property('editable-set', True)
# TrVw_FlNmLst.append_column(Gtk.TreeViewColumn('原始檔名', ClRdrTxt, text=0))
# TrVw_FlNmLst.append_column(Gtk.TreeViewColumn('將更換成', ClRdrTxt, text=1))
# TrVw_FlNmLst.append_column(Gtk.TreeViewColumn('備註', ClRdrTxt, text=2))

# #==== window event bind. ====

# Bdr.get_object('Btn_DirExpd').connect('clicked', FileList)
# Bdr.get_object('Btn_FlFltPrv').connect('clicked', FileFilter)
# Bdr.get_object('Btn_NmSrlzPrv').connect('clicked', NameSerialize)
# Bdr.get_object('Btn_StrRplcPrv').connect('clicked', StringReplace)
# Bdr.get_object('Btn_StrPndPrv').connect('clicked', StringPend)
# Bdr.get_object('Btn_Rst').connect('clicked', FileRelist)
# Bdr.get_object('Btn_Apl').connect('clicked', Apply)

# Win.connect('delete-event', Gtk.main_quit)

# #=== initialize working directory. ===

# Ety_DirPth = Bdr.get_object('Ety_DirPth')
# WkPth = '' # 'WkPth' = Working Path

# if len(sys.argv) > 1 :
#   WkPth = os.path.abspath(urllib.unquote(sys.argv[1]).replace('file://', ''))

#   if WkPth[-1] and WkPth[-1] is not '/' :
#     WkPth +='/'

#   if os.path.isdir(WkPth) :
#     Ety_DirPth.set_text(WkPth)
#     FileList(None)

#===

# Win.show_all()
# Gtk.main()

#===

# def FileList (Btn) :
#   global WkPth

#   DirPth = Ety_DirPth.get_text() # 'DirPth' = Directory Path.

#   if not os.path.isdir(DirPth) :
#     Alert('目錄位置不存在。')

#     return

#   if DirPth[-1] is not '/' :
#     DirPth += '/';

#   if WkPth is not DirPth :
#     WkPth = DirPth

#     print WkPth

#   FlNmLst = os.listdir(DirPth) # 'FlNmLst' = File Name List.

#   LstSt_FlNm.clear()
#   FlNmLst.sort()

#   for FlNm in FlNmLst :
#     if not os.path.isfile(DirPth + FlNm) :
#       continue

#     Itm = LstSt_FlNm.append([FlNm, FlNm, ''])

# from kivy.core.text import LabelBase
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
import os

class Alert (BoxLayout) :
  text = ObjectProperty('?!')
  popup = ObjectProperty(None)

  def Cancel (self) :
    self.popup.dismiss()

class FolderBrowser (FloatLayout) :
  Load = ObjectProperty(None)
  path = ObjectProperty('./')
  popup = ObjectProperty(None)

  def Cancel(self) :
    self.popup.dismiss()

class MainApp (App) :
  def AlertShowUp (self, Txt) :
    if type(Txt) is not str :
      return

    self.Alrt = Popup(title = 'Oops', size_hint = (.5, .3)) # alert dialog.
    self.Alrt.content = Alert(text = Txt, popup = self.Alrt)
    self.Alrt.open()

  def FolderBrowse (self) :
    self.FldrBrwsr = Popup(title = "Folder Browse", size_hint = (0.9, 0.9) ) # folder browser.
    self.FldrBrwsr.content = FolderBrowser(Load = self.FileList, popup = self.FldrBrwsr)
    self.FldrBrwsr.open()

  def FileList (self, path, filename) :
    self.root.ids['FolderPath'].text = path
    self.FldrBrwsr.dismiss()

    if not os.path.isdir(path) :
      AlertShowUp('Target folder is not existent.')
      return

    if path[-1] is not '/' :
      path += '/';

    MpngTbl = self.root.ids['MappingTable'] # mapping table

    for Wdgt in MpngTbl.children[0:len(MpngTbl.children) - 2] :
      MpngTbl.remove_widget(Wdgt)

    FlNmLst = os.listdir(path) # 'FlNmLst' = File Name List.
    FlNmLst.sort()

    for FlNm in FlNmLst :
      if not os.path.isfile(path + FlNm) :
        continue

      MpngTbl.add_widget(Label(text = FlNm, size = (0, 30), size_hint = (1, None)))
      MpngTbl.add_widget(TextInput(text = FlNm, size = (0, 30), size_hint = (1, None)))

if __name__ == '__main__':
  MainApp().run()

#=======================================================================================================================