from django.db import models

# Create your models here.
#這個 Post 模型定義了文章的標題、URL 代號、內容、發布時間，並且設定資料預設以發布時間倒序排列，最後用標題當作代表文字。


class Post(models.Model):
    title = models.CharField(max_length=200)  # 文章標題，使用 CharField，代表它是「字串」欄位，max_length=200 表示這個字串最多 200 個字元。
    slug = models.CharField(max_length=200)  # 通常是讓文章有一個簡短又能放網址的識別字串。
    content = models.TextField()  # 文章內容，不限長度，適合存放文章正文
    pub_date = models.DateTimeField(auto_now_add=True)  # 建立時間，用 DateTimeField，表示「日期時間」欄位，auto_now_add=True 表示這個欄位在資料建立時會自動帶上當下時間，不能後改

    class Meta:
        ordering = ['-pub_date']  #這個模型的資料預設會按照 pub_date 欄位做「由新到舊」排序（前面有負號是反向排序）。

    def __str__(self):
        return self.title  # 讓每個物件可以呈現自己的名子
