from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.core import serializers
from django.utils.timezone import now
from django.contrib import auth
from django.http import HttpResponseRedirect
import sqlite3
import os
from django.http import HttpResponse
import json
from .form import *
from .models import *
# Create your views here.
def login(request):
    loginFail=''
    if (request.method == 'POST'):
        if request.user.is_authenticated:
            return render(request, 'search.html',{})
        form = loginForm(request.POST)
        print(make_password(request.POST['password']))
        user = auth.authenticate(username=request.POST['user_name'], password=request.POST['password'])
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect('/search/')
        else:
            return render(request, 'login.html', {'form': form, 'loginFailMessage': loginFail})
    else:
        print("else")
        form = loginForm()
        # clear user data
        request.session.flush()
    return render(request, 'login.html', {'form': form, 'loginFailMessage': loginFail})

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')   
def main(request):
    return render(request, 'search.html', {})

def guide_generateData(request):
    print(guide_generateData)
    return render(request, 'guide_generateData.html', {})

def project(request):
    print(project)
    return render(request, 'project.html', {})

def search(request):
    return render(request, 'search.html', {})
def combineSQL(search_idList,operatorsList,keyWordList,condition,tableName,othertableSearchList):
    sql = "SELECT * FROM "
    factor = ""
    OnAppend=[]
    if(len(othertableSearchList) == 0):
        sql+= str(tableName) + "  WHERE "

    for combineTableIndex in range(len(othertableSearchList)):
        if(combineTableIndex == 0):
            sql += "(SELECT * FROM " + str(tableName) + " INNER JOIN " + str(othertableSearchList[combineTableIndex])
        else:
            sql += ", " + str(othertableSearchList[combineTableIndex])
    for combineTableIndex in range(len(othertableSearchList)):
        if(combineTableIndex == 0):
            sql += " ON "+str(othertableSearchList[combineTableIndex])+".GUID == user.GUID AND "
        else:
            sql += str(othertableSearchList[combineTableIndex])+".GUID == user.GUID AND "
        if(combineTableIndex == len(othertableSearchList)-1):
            sql +="user.GUID == user.GUID"
            sql = sql  + ") WHERE "
    print(sql)
    for index in range(len(search_idList)):
        if (search_idList[index] == '開立日'):
            keyWordList[index]=keyWordList[index].split('/')[2]+keyWordList[index].split('/')[0]+keyWordList[index].split('/')[1]
        if(search_idList[index] == 'datatime'):
                keyWordList[index]=keyWordList[index].split('/')[2]+"-"+keyWordList[index].split('/')[0]+"-"+keyWordList[index].split('/')[1]
                operatorsList[index] = 'LIKE'
        if(operatorsList[index] != "LIKE"):
            factor += '{} {} (\'{}\') {} '.format(search_idList[index],operatorsList[index],keyWordList[index],condition)
        else:    
            factor += '{} {} \'%{}%\' {} '.format(search_idList[index],operatorsList[index],keyWordList[index],condition)
        
    return sql + factor[:factor.rfind('AND ')][:factor[:factor.rfind('AND ')].rfind('OR ')]

def searchTable(request):
    try:
        if request.method == "POST":
            length = len(request.POST)
            dataList = []
            search_idList=[]
            operatorsList=[]
            keyWordList=[]
            othertableSearchList=[]
            for count in range(0,int((length-3)/6)):
                if(dict(request.POST)["data[rules]["+str(count)+"][id]"][0] == '疾病'):
                    othertableSearchList.append(dict(request.POST)["data[rules]["+str(count)+"][value]"][0])
                    search_idList.append(dict(request.POST)["data[rules]["+str(count)+"][value]"][0]+"_result")
                    if(dict(request.POST)["data[rules]["+str(count)+"][operator]"][0] == "equal"):
                        keyWordList.append('1')
                    else:
                        keyWordList.append('0')
                    operatorsList.append("IN")
                else:
                    search_idList.append(dict(request.POST)["data[rules]["+str(count)+"][id]"][0])
                    keyWordList.append(dict(request.POST)["data[rules]["+str(count)+"][value]"][0])
                    operatorsList.append(dict(request.POST)["data[rules]["+str(count)+"][operator]"][0].replace("equal","IN").replace("in","LIKE").replace("not_","NOT "))
                condition = dict(request.POST)['data[condition]'][0]
            sqlInstruction = combineSQL(search_idList,operatorsList,keyWordList,condition,"user",othertableSearchList)
            #get data
            dbPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/db.sqlite3"
            conn = sqlite3.connect(dbPath)
            print(sqlInstruction)
            cursor = conn.execute(sqlInstruction)
            for row in cursor:
                dataList.append({
                    "來源":row[1],"開立日":row[2],"開立者":row[3],"科別":row[4],"就診號":row[5],"身份證":row[6],"索引號":row[7],"姓名":row[8],"GUID":row[9],"拒絕註記":row[10],"工作號":row[11],"工作號_new":row[12],"DNA管號":row[13],"檢體編號_x":row[14],"樣本代碼":row[15],"all_comment":row[16]
                    })
            # get user name
            user= conn.execute("SELECT username FROM auth_user WHERE id == " + str(request.session['_auth_user_id']))
            for row in user:
                user = row[0]
            conn.close()
            Action.objects.create(user=user, action="SearchTable" + str(keyWordList) + str(operatorsList) + str(search_idList) + str(condition))
        return HttpResponse(json.dumps(dataList), content_type="application/json")
    except Exception as e:
        print(e.args)
        return HttpResponse(e.args)
def searchActionTable(request):
    print('searchActionTable')
    dataList=[]
    try:
        if request.method == "POST":
            length = len(request.POST)
            dataList = []
            search_idList=[]
            operatorsList=[]
            keyWordList=[]
            for count in range(0,int((length-3)/6)):
                condition = dict(request.POST)['data[condition]'][0]
                search_idList.append(dict(request.POST)["data[rules]["+str(count)+"][id]"][0])
                operatorsList.append(dict(request.POST)["data[rules]["+str(count)+"][operator]"][0].replace("equal","IN").replace("in","LIKE").replace("not_","NOT "))
                keyWordList.append(dict(request.POST)["data[rules]["+str(count)+"][value]"][0])
            sqlInstruction = combineSQL(search_idList,operatorsList,keyWordList,condition,"blog_action",[])
            print(sqlInstruction)
            #get data
            dbPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/db.sqlite3"
            conn = sqlite3.connect(dbPath)
            cursor = conn.execute(sqlInstruction)
            for row in cursor:
                dataList.append({
                    "datatime":row[1],"action":row[2],"user":row[3], 
                })
            # get user name
            user= conn.execute("SELECT username FROM auth_user WHERE id == " + str(request.session['_auth_user_id']))
            for row in user:
                user = row[0]
            conn.close()
            Action.objects.create(user=user, action="SearchActionLogTable" + str(keyWordList) + str(operatorsList) + str(search_idList) + str(condition))
        return HttpResponse(json.dumps(dataList), content_type="application/json")
    except Exception as e:
        print(e.args)
        return HttpResponse(e.args)

def updateData(request):
    print("updateData")
    try:
        if request.method == "POST":
            print(request.POST)
            
        return HttpResponseRedirect('/search/')
    except Exception as e:
        print(e.args)
        return HttpResponseRedirect('/search/')

# import generateData.py
def uploadData(request):
    try:
        if request.method == "POST":
            print(request.POST)
            
        return HttpResponseRedirect('/search/')
    except Exception as e:
        print(e.args)
        return HttpResponseRedirect('/search/')
def actionLog(request):
    try:
        actionList = Action.objects.all()
        return render(request, 'actionLog.html', {'actionList':actionList})
    except:
        return render(request, 'actionLog.html', {})


