# HTML

### Flask Block

請在一開始輸入↓，除非不需要簡單模板ˊ ˇ ˋ

{% extends "base.html" %}

- style
你需要的Style通過這個Block放進來，CSS放入static中的css料夾中，例：

```<link href="{{url_for('static', filename='css/courseSelect.css')}}" rel="stylesheet">```

- title
你希望這一頁叫做甚麼名字請放入這個Block

- content
這一頁中的所有內容，請放入這個Block

## base

頁面的簡單模板，Header的部分也寫在這裡

## recommendation

主要的頁面，根據提交的內容，如科系，課程，序號...等，來判斷有沒有機率選上以及，
會根據你輸入的課程顯示出這堂課有誰選、有沒有上...的資料。
