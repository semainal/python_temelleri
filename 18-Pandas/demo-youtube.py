from numpy import split
import pandas as pd

df = pd.read_csv("youtube-ing.csv")
result = df

# 1- İlk 10 kaydı getiriniz.

result = df.head(10)
# 2- İkinci 5 kaydı getiriniz.

result = df[5:10].head()
# 3- Dataset' de bulunan kolon isimleri ve sayısını bulunuz.

result = df.columns
result = len(df.columns)

# 4- Aşağıda bulunan bazı kolonları silin ve kalan kolonları listeleyiniz.
# (thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed,description)

result = df.drop(["thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description"], axis= 1)


# 5- Beğenme (like) ve beğenmeme (dislike) sayılarının ortalamasını bulunuz.

result = df["likes"].mean()
result = df["dislikes"].mean()

# 6- ilk 50 videonun like ve dislike kolonlarını getiriniz.

result = df[["likes","dislikes","title"]].head(50)

# 7- En çok görüntülenen video hangisidir ?

result = df[df["views"] == df["views"].max()][["title","video_id","views"]]

# 8- En düşük görüntülenen video hangisidir?

result = df[df["views"] == df["views"].min()][["title","video_id","views"]]

# 9- En fazla görüntülenen ilk 10 video hangisidir ?

result = df.sort_values("views", ascending=False).head(10)[["video_id","title","views"]]

# 10- Kategoriye göre beğeni ortalamalarını sıralı şekilde getiriniz.

result = df.groupby("category_id").mean().sort_values("likes")["likes"]

# 11- Kategoriye göre yorum sayılarını yukarıdan aşağıya sıralayınız.

result = df.sort_values("comment_count", ascending=False)[["comment_count","title"]]

# 12- Her kategoride kaç video vardır ?

result = df["category_id"].value_counts()

# 13- Her videonun title uzunluğu bilgisini yeni bir kolonda gösteriniz.

new_column = df["title"].apply(len)
df["New_Column"] = new_column
result = df

# 14- Her video için kullanılan tag sayısını yeni kolonda gösteriniz.

new_column = df["tags"].str.split("|").apply(len)
df["New_Column"] = new_column
result = df

# farklı bir şekli:
# df["tag_count"] = df["tags"].apply(lambda x: len(x.split("|")))


# başka alternatifi:
# def tagCount(tag):
#     return len (tag.split("|"))

# df["tag_count"] = df["tags"].apply(tagCount)

# 15- En popüler videoları listeleyiniz.(like/dislike oranına göre)




def likeDislikeOranHesapla(dataset):
    likesList = list(dataset["likes"])
    dislikesList = list(dataset["dislikes"])

    liste = list(zip(likesList,dislikesList))


    oranListesi = []

    for like , dislike in liste:
        if (like + dislike) == 0:
            oranListesi.append(0)

        else:
            oranListesi.append(like/(like+dislike))

    return oranListesi



df["beğeni_orani"] = likeDislikeOranHesapla(df)
print(df.sort_values("beğeni_orani", ascending=False)[["title","likes","dislikes","beğeni_orani"]])


