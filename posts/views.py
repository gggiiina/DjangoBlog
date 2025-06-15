from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post
from datetime import datetime


# Vies：查詢資料去做畫面的呈現(渲染)，回傳至url
# Create your views here.


# Python 把文章資料一筆一筆撈出來，自己用 .format() 拼接 HTML 字串（像是 #1: 標題<br><hr>），最後用 HttpResponse() 把字串塞給使用者。
# 缺點：所有 HTML 寫在 Python 裡，很亂、很難維護。

def index(request):  # request來自於Django框架的結果
    # 查詢資料與資料庫操作
    article_records = Post.objects.all()  # 撈出所有Post的資料。objects是繼承Model的方法

    # 處理結果查詢
    article_list = list()
    for count, article in enumerate(article_records):
        article_list.append("#{}: {}<br><hr>".format(str(count), str(article.title)))  # 印出文章標題；<br>：Enter <hr>：分隔線
        article_list.append("<small>{}</small><hr>".format(article.content))   # 在Post模型裡定義了title,content，Django幫你把資料表的每一列轉成 Post 物件，所以每個 Post 物件都可以用 .title 存取標題這個欄位。
    return HttpResponse(article_list)


def about(requset):
    return HttpResponse("hello world")


#  不在 view 裡寫 HTML，直接用 render()，請 Django 幫你去找 index.html 的模板檔，HTML 長怎樣，就交給模板決定。


def index_use_template(requests):
    article_records = Post.objects.all()
    now = datetime.now()
    return render(requests, "index.html", locals())  # locals()會把view function 使用過的變數變成字典檔存起來