from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post

# Vies：查詢資料去做畫面的呈現(渲染)，回傳至url
# Create your views here.


def index(request):  # request來自於Django框架的結果
    # 查詢資料與資料庫操作
    article_records = Post.objects.all()  # 撈出所有Post的資料。objects是繼承Model的方法

    # 處理結果查詢
    article_list = list()
    for count, article in enumerate(article_records):
        article_list.append("#{}: {}<br><hr>".format(str(count), str(article.title)))  # 印出文章標題；<br>：Enter <hr>：分隔線
        article_list.append("<small>{}</small><hr>".format(article.content))   # 在Post模型裡定義了title,content，Django幫你把資料表的每一列轉成 Post 物件，所以每個 Post 物件都可以用 .title 存取標題這個欄位。
    return HttpResponse(article_list)
