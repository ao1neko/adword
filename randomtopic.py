# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask import request



def makelist(text):
    ramdomlist=[]
    ramdomlist.append("subscribe"+text)
    ramdomlist.append("シェア"+text)
    ramdomlist.append("インスタント"+text)
    ramdomlist.append(text+"選手権")
    ramdomlist.append("動物用"+text)
    ramdomlist.append(text+"体験会")
    ramdomlist.append("街中の"+text)
    ramdomlist.append("インビジブル"+text)
    ramdomlist.append("10分でする"+text)
    ramdomlist.append("大人の"+text)
    ramdomlist.append("日本全国"+text)
    ramdomlist.append("AI"+text)
    ramdomlist.append("VR"+text)
    ramdomlist.append(text+"あるある")
    ramdomlist.append("いきなり"+text)
    ramdomlist.append("無料"+text)
    ramdomlist.append("SNS"+text)
    ramdomlist.append("自動化"+text)

    return ramdomlist