# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask import request
import json


f = open("dic.json", 'r')
json_data1 = json.load(f) #JSON形式で読み込む
f = open("dic2.json", 'r')
json_data2 = json.load(f) #JSON形式で読み込む


def maketextlist(key,text):
    
    textlist=[]
    a=0

    for N in range(6):
        n=6-N
        if a==3:
            break
        for i in json_data2:
            if a==3:
                break
            if len(key)<len(i):  
                for j in range(len(key)-n-1):
                    k2=key[:n+j+1].replace("-","")
                    i2=i[-(j+1+n):].replace("-","")
                    if i2 == k2:
                        i3=i+key[n+1:]+" "+json_data2[i][0]+"   "+text
                        textlist.append(i3)
                        a=a+1
                        break
            else:
                for j in range(len(i)-n-1):
                    k2=key[:n+j+1].replace("-","")
                    i2=i[-(j+1+n):].replace("-","")
                    if i2 == k2:
                        i3=i[:len(i)-n]+key+" "+json_data2[i][0]+"   "+text  
                        textlist.append(i3)
                        a=a+1
                        break  
            
    if a != 0 :
        return    textlist 
    else :
        return      a



def maketextlist2(key2,text2):
    a=0
    textlist2=[]
    for N in range(6):
        n=6-N
        if a==3:
            break
        for i in json_data2:
            if a==3:
                break
            if len(key2)<len(i):  
                for j in range(len(key2)-n-1):
                    i2=i[-(j+1+n):].replace("-","")
                    k2=key2[:j+n+1].replace("-","")
                    if i2 == k2:
                        i3=i+key2[n+1:]+" "+json_data2[i][0]+"   "+text2
                        textlist2.append(i3)
                        a=a+1
                        break
            else:
                for j in range(len(i)-n-1):
                    i2=i[-(n+j+1):].replace("-","")
                    k2= key2[:n+j+1].replace("-","")
                    if i2 ==k2:
                        i3=i[:len(i)-n]+key2+" "+json_data2[i][0]+"   "+text2  
                        textlist2.append(i3)
                        a=a+1
                        break  

    if a != 0 :
        return    textlist2 
    else :
        return   a 