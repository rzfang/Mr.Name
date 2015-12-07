#! /usr/bin/env python
# -*- coding: utf-8 -*-

#==== libraries import. ================================================================================================

from gi.repository import Gtk
import os
import re
import sys

#==== functions. =======================================================================================================

def Alert (Txt) :
  if type(Txt) is not str :
    return

  Dlg = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, 'Alert !!')

  Dlg.format_secondary_text(Txt)
  Dlg.run()
  Dlg.destroy()

def FileList (Btn) :
  DirPth = Ety_DirPth.get_text() # 'DirPth' = Directory Path.

  if not os.path.isdir(DirPth) :
    Alert('目錄位置不存在。')

    return

  if DirPth[-1] is not '/' :
    DirPth += '/';

  FlNmLst = os.listdir(DirPth) # 'FlNmLst' = File Name List.

  LstSt_FlNm.clear()
  FlNmLst.sort()

  for FlNm in FlNmLst :
    if not os.path.isfile(DirPth + FlNm) :
      continue

    Itm = LstSt_FlNm.append([FlNm, FlNm, ''])

def FileFilter (Btn) :
  FltPtn = Bdr.get_object('Ety_FltPtn').get_text()
  IvtFlt = Bdr.get_object('CckBtn_IvtFlt').get_active() # 'IvtFlt' = Inverted Filter.
  IsOrg = Bdr.get_object('RdoBtn_Org').get_active()  # 'IsOrg' = Is Original.

  if not FltPtn :
    Alert('請輸入過濾條件。')

    return -1

  for i in range(len(LstSt_FlNm) - 1, -1, -1) :
    Tgt = LstSt_FlNm[i][0] if IsOrg else LstSt_FlNm[i][1] # 'Tgt' = Target.

    if (IvtFlt and re.search(FltPtn, Tgt) is None) or (not IvtFlt and re.search(FltPtn, Tgt) is not None):
        LstSt_FlNm.remove(LstSt_FlNm[i].iter)

def NameSerialize (Btn) :
  SttNbr = Bdr.get_object('SpnBtn_SttNbr').get_value_as_int() # 'SttNbr' = Start Number.
  PdNbr = Bdr.get_object('SpnBtn_PdNbr').get_value_as_int() # 'PdNbr' = Padding Number.
  IsExtKp = Bdr.get_object('CckBtn_KpExt').get_active() # 'IsExtKp' = Is Extend name Kept.

  for Idx, FlNm in enumerate(LstSt_FlNm) :
    if not IsExtKp :
      FlNm[1] = str(Idx + SttNbr).zfill(PdNbr)

      continue;

    StrPt = os.path.splitext(FlNm[1]) # 'StrPt' = String Parts
    FlNm[1] = str(Idx + SttNbr).zfill(PdNbr) + StrPt[1]

def StringReplace (Btn) :
  TgtStr = Bdr.get_object('Ety_TgtStr').get_text()
  RplcStr = Bdr.get_object('Ety_RplcStr').get_text()

  if TgtStr is '' :
    Alert('請輸入目標字串。')
    return -1

  for FlNm in LstSt_FlNm :
    if TgtStr in FlNm[1] :
      FlNm[1] = FlNm[1].replace(TgtStr, RplcStr)

def StringPend (Btn) :
  PndStr = Bdr.get_object('Ety_PndStr').get_text()
  IsBfr = Bdr.get_object('RdoBtn_Bfr').get_active()
  IsExtKp = Bdr.get_object('CckBtn_ExtKp').get_active()

  if PndStr is '' :
    Alert('請輸入字串。')
    return -1

  for FlNm in LstSt_FlNm :
    if IsBfr :
      FlNm[1] = PndStr + FlNm[1]
    elif not IsExtKp :
      FlNm[1] = FlNm[1] + PndStr
    else :
      StrPt = os.path.splitext(FlNm[1]) # 'StrPt' = String Parts
      FlNm[1] = StrPt[0] + PndStr + StrPt[1]

def FileRelist (Btn) :
  TrVw_FlNmLst = Bdr.get_object('TrVw_FlNmLst')

  for FlNm in LstSt_FlNm :
    FlNm[1] = FlNm[0]

def Apply (Btn) :
  Btn_DirExpd = Bdr.get_object('Btn_DirExpd')
  NtBk_TbBx = Bdr.get_object('NtBk_TbBx')
  Btn_Rst = Bdr.get_object('Btn_Rst')
  Btn_Apl = Bdr.get_object('Btn_Apl')

  Btn_DirExpd.set_sensitive(False)
  NtBk_TbBx.set_sensitive(False)
  Btn_Rst.set_sensitive(False)
  Btn_Apl.set_sensitive(False)

  for FlNm in LstSt_FlNm :
    if FlNm[1] == FlNm[0] :
      FlNm[2] = '忽略。'
    elif not os.path.isfile(WkPth + FlNm[0]) :
      FlNm[2] = '原始檔案不存在。'
    elif os.path.isfile(WkPth + FlNm[1]) :
      FlNm[2] = '將更換成的檔案已經存在。'
    else :
      os.rename(WkPth + FlNm[0], WkPth + FlNm[1])

      FlNm[2] = '成功！'

  Btn_DirExpd.set_sensitive(True)
  NtBk_TbBx.set_sensitive(True)
  Btn_Rst.set_sensitive(True)
  Btn_Apl.set_sensitive(True)

#==== main process. ====================================================================================================

PgmPth = os.path.dirname(__file__)
Bdr = Gtk.Builder()

Bdr.add_from_file(PgmPth + '/../DSN/gui.glade')

Win = Bdr.get_object('Win_MrName')

Win.set_icon_from_file(PgmPth + '/../DSN/icon.ico')

#==== initialize TreeView. ====

ClRdrTxt = Gtk.CellRendererText()
TrVw_FlNmLst = Bdr.get_object('TrVw_FlNmLst')
LstSt_FlNm = Bdr.get_object('LstSt_FlNm')

ClRdrTxt.set_property('editable-set', True)
TrVw_FlNmLst.append_column(Gtk.TreeViewColumn('原始檔名', ClRdrTxt, text=0))
TrVw_FlNmLst.append_column(Gtk.TreeViewColumn('將更換成', ClRdrTxt, text=1))
TrVw_FlNmLst.append_column(Gtk.TreeViewColumn('備註', ClRdrTxt, text=2))

#==== window event bind. ====

Bdr.get_object('Btn_DirExpd').connect('clicked', FileList)
Bdr.get_object('Btn_FlFltPrv').connect('clicked', FileFilter)
Bdr.get_object('Btn_NmSrlzPrv').connect('clicked', NameSerialize)
Bdr.get_object('Btn_StrRplcPrv').connect('clicked', StringReplace)
Bdr.get_object('Btn_StrPndPrv').connect('clicked', StringPend)
Bdr.get_object('Btn_Rst').connect('clicked', FileRelist)
Bdr.get_object('Btn_Apl').connect('clicked', Apply)

Win.connect('delete-event', Gtk.main_quit)

#==== initialize working directory. ====

Ety_DirPth = Bdr.get_object('Ety_DirPth')
WkPth = '' # 'WkPth' = Working Path

if len(sys.argv) > 1 :
  WkPth = os.path.abspath(sys.argv[1])

  if WkPth[-1] and WkPth[-1] is not '/' :
    WkPth +='/'

  if os.path.isdir(WkPth) :
    Ety_DirPth.set_text(WkPth)
    FileList(None)

#====

Win.show_all()
Gtk.main()

#=======================================================================================================================