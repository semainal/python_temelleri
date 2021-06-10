import pandas as pd

df = pd.read_csv("youtube-ing.csv")

# 1- İlk 10 kaydı getiriniz.

result = df.head(10)

# 2- İkinci 5 kaydı getiriniz.

result = df[5:10]

# 3- Dataset' de bulunan kolon isimleri ve sayısını bulunuz.

result = df.columns
result = len(df.columns)

# 4- Aşağıda bulunan bazı kolonları silin ve kalan kolonları listeleyiniz.
# (thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed,description)

result = df.drop(["thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description"], axis=1, inplace=True)
result = df

# 5- Beğenme (like) ve beğenmeme (dislike) sayılarının ortalamasını bulunuz.

result = df["likes"].mean()
result = df["dislikes"].mean()

# 6- ilk 50 videonun like ve dislike kolonlarını getiriniz.

result = df.head(50)[["likes","dislikes"]]

# 7- En çok görüntülenen video hangisidir ?

result = df[df["views"].max()==df["views"]][["title", "views"]]

# 8- En düşük görüntülenen video hangisidir?

result = df[df["views"].min() == df["views"]][["title","views"]]

# 9- En fazla görüntülenen ilk 10 video hangisidir ?

result = df.head(10)[["title","views"]].sort_values("views",ascending=False)

# 10- Kategoriye göre beğeni ortalamalarını sıralı şekilde getiriniz.

result = df.groupby("category_id").mean().sort_values("likes", ascending=False)["likes"]

# 11- Kategoriye göre yorum sayılarını yukarıdan aşağıya sıralayınız.

result = df.groupby("category_id").mean().sort_values("comment_count", ascending=False)["comment_count"]

# 12- Her kategoride kaç video vardır ?

result = df.groupby("category_id").count()["video_id"]

# 13- Her videonun title uzunluğu bilgisini yeni bir kolonda gösteriniz.

new_column = df["title"].apply(len)
df["new_column"] = new_column
result = df

# 14- Her video için kullanılan tag sayısını yeni kolonda gösteriniz.

second_column = df["tags"].str.split("|").apply(len)
df["second_column"] = second_column
result = df

# 15- En popüler videoları listeleyiniz.(like/dislike oranına göre)


likedislike = df[["likes","dislikes"]]

result = df["likes"] / df["dislikes"]

print(result)