# TPMI_searchManagement

![](https://img.shields.io/static/v1?label=python&message=3.7&color=yellow)
![](https://img.shields.io/static/v1?label=mysql&message=8.X&color=red)
![](https://img.shields.io/static/v1?label=Django&message=3.0.3&color=green)
![](https://img.shields.io/static/v1?label=Docker&message=3.0.3&color=blue)

***This system can supply for search database***
***The following example uses case search as an example***


<a href=""><img src="img/main.png" title="FVCproductions" alt="FVCproductions"></a>



## Table of Contents

- [Introduction](#introduction)
- [Install](#install)
- [function](#connection-options)
  - [create Admin account](#createAdmin-options)
  - [update FilterList](#updateFilterList-flags)
- [Todo](#todo)




## Introduction

* 123


## Install



Before installing, download and install [docker](https://www.docker.com) , docker-compose and Django [sqlite3 file](https://drive.google.com/file/d/1ySg70xu_Xnq1cadPS6LRw51GAa8B0NS4/view?usp=sharing).


```sh
$ git clone https://github.com/skysora/TPMI_searchManagement
$ cd ./TPMI_searchManagement
$ docker-compose up --build
```
You cane access http://ip address:7777
  
<a href=""><img src="img/login.png" title="FVCproductions" alt="FVCproductions"></a>
## createAdmin-options

```sh
$ cd ./TPMI_searchManagement
$ python3 manage.py createsuperuser
```

## updateFilterList-flags

After you import table on database add your item and if you want more can reference [here](https://querybuilder.js.org)

$ vim ./TPMI_searchManagement/blog/templates/element/fliterList.html

```

Example:
```
{
  id: '疾病',
  label: '疾病',
  type: 'string',
  values: {
        <‘DatabasTableName’ : ‘欲顯示欄位名稱’>
  }
  operators: ['equal', 'not_equal', 'in']
 }
```
- [Todo](#todo)



