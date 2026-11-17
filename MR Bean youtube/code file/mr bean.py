#import libray conent wit api
import requests
import pandas as pd
#import library to understand youtube time form
import isodate
import matplotlib.pyplot as plt

api_key='################################'

video_ids=['9omW7kXZKAE',"9LbDcWHsKPQ","x5borFM9NjE","P8Enr37Mz8w","AqBS77mEcvA","u5OZIJscZx8","fJa7d_6-0Ng","3VviNr4-iHw",'WJILggMJyqM',"owBBogWC0yM"]
all_videos=[]
for v_id in video_ids:
    url=f'https://www.googleapis.com/youtube/v3/videos?id={v_id}&key={api_key}&part=snippet,contentDetails,statistics'
    print(url)
    response=requests.get(url)
    data=response.json()
    if 'items'in data and len(data["items"])>0:
        video_details=data["items"][0]
        video=data["items"][0]
        tile=video['snippet']['title']
        describtion=video['snippet']['description']
        puplish_date=video['snippet']['publishedAt']
        duration=video["contentDetails"]['duration']
        view=video['statistics']['viewCount']
        like=video['statistics']['likeCount']
        comments=video['statistics']['commentCount']
        video_data={
            "Video_ID":v_id,
            "title":tile,
            "describtion":describtion,
            "puplish":puplish_date,
            "duration":duration,
            "views":view,
            "Likes":like,
            "Comments":comments

        }
        all_videos.append(video_data)
    else:
        print("Error in fetching vedio details")
#creat my table by pandas
videos_table=pd.DataFrame(all_videos)

#show all columns by max option
pd.set_option("display.max.columns",None)

#look at my info
videos_table.info()
print(videos_table.describe())
print(videos_table.shape)
#covert some columns to int and to datetime and to youtube isotime
videos_table["views"]=pd.to_numeric(videos_table["views"])
videos_table['Likes']=pd.to_numeric(videos_table["Likes"])
videos_table["Comments"]=pd.to_numeric(videos_table["Comments"])
videos_table["puplish"]=pd.to_datetime(videos_table["puplish"])
print(videos_table[["views","Likes","Comments","puplish"]].dtypes)
videos_table["duration_second"]=videos_table["duration"].apply(
    lambda x: isodate.parse_duration(x).total_seconds()
)
videos_table["duration_timedelta"]=pd.to_timedelta(videos_table["duration_second"],unit="s")
#check again
videos_table.info()
print(videos_table.head(5))
print(videos_table[['duration_timedelta','duration_second',"duration"]])
#check if something is  missing or repating
print(videos_table.isna().sum())
print(videos_table.duplicated().sum())
print(videos_table['Video_ID'].duplicated().sum())
#check columns
print(videos_table[["views","Likes","Comments","duration_second","duration_timedelta"]].describe())
#sort by value
most_video_viewed=videos_table.sort_values(by="views",ascending=False)
print(most_video_viewed.head(5))
samllest_video_viewed=videos_table.sort_values(by='views',ascending=True)
print(samllest_video_viewed.head(5))
most_video_likes=videos_table.sort_values(by='Likes',ascending=False)
print(most_video_likes.head(5))
most_video_comments=videos_table.sort_values(by="Comments",ascending=False)
print(most_video_comments.head(5))
#count mean/average
average_likes=videos_table["Likes"].mean()
print(f"Average Likes:{average_likes}")
average_comments=videos_table['Comments'].mean()
print(f"Average Comments:{average_comments}")
average_views=videos_table['views'].mean()
print(f"Average Views:{average_views}")
#creat and count like rate
videos_table['like_rate']=(videos_table["Likes"]/videos_table['views'])*100
print(videos_table.head(5))
video_rate_sort=videos_table.sort_values(by="like_rate",ascending=False)
print(video_rate_sort.head(4))
#creat and count comment rate
videos_table['comments_rate']=(videos_table["Comments"]/videos_table['views'])*100
print(videos_table.head(4))
comments_rate_sort=videos_table.sort_values(by='comments_rate',ascending=False)
print(comments_rate_sort.head())
#Check Correlation between columns
correlation_data=videos_table[["views","Likes",'Comments',"like_rate","comments_rate", 'duration_second']].corr()
print(correlation_data)
#pinting the most viewed videos in a bar chart
plt.figure(figsize=(12,6))
viwes_t=plt.barh(most_video_viewed["title"].head(5).str.slice(0,25)+"...",most_video_viewed['views'].head(5))
plt.xlabel("Views")
plt.ylabel("Title")
plt.title("MR Bean most videos views")
plt.tight_layout()
plt.gca().invert_yaxis()
plt.xlim(0,350000)
plt.bar_label(viwes_t)
plt.show()
#pinting Least Viewed Videos in a bar chart
plt.figure(figsize=(12,6))
least_viewed=videos_table.sort_values(by="views",ascending=True)
print("Least Viewed Videos")
print("_"*30)
print(least_viewed.head(5))
least_viewed_bar=plt.bar(least_viewed["title"].head(5).str.slice(7,25)+"...",least_viewed['views'].head(5))
plt.title("MR Bean Least Viewed Videos")
plt.xlabel("Views")
plt.ylabel("Titles")
plt.tight_layout()
plt.bar_label(least_viewed_bar)
plt.show()
#pinting most videos like
plt.figure(figsize=(12,6))
likes_table=plt.bar(most_video_likes["title"].head(5).str.slice(2,25)+"...",most_video_likes["Likes"].head(5))
plt.title("Most vidoes have likes")
plt.xlabel("Title")
plt.ylabel("Likes")
plt.bar_label(likes_table)
plt.show()
#piniting most rate videos table
plt.figure(figsize=(12,6))
most_video_like_rate=videos_table.sort_values(by='like_rate',ascending=False)
videos_rate_table=plt.bar(most_video_like_rate["title"].head(5).str.slice(2,25)+"...",most_video_like_rate["like_rate"].head(5))
plt.title("Top videos like rate")
plt.xlabel("Title")
plt.ylabel("Like Rate")
plt.bar_label(videos_rate_table)
plt.show()
#piniting most video comment table
table_most_coment=plt.bar(most_video_comments['title'].head(5).str.slice(2,25)+"...",most_video_comments["Comments"].head(5))
plt.title("Most video comment")
plt.xlabel("Title")
plt.ylabel("comments")
plt.bar_label(table_most_coment)
plt.show()
#pinting most video comment rate
plt.figure(figsize=(12,6))
comment_rate_table=plt.bar(comments_rate_sort['title'].head(5).str.slice(2,25),comments_rate_sort['comments_rate'].head(5))
plt.title("Most video comment rate")
plt.xlabel("Title")
plt.ylabel("Comment rate")
plt.bar_label(comment_rate_table)
plt.show()
#sort by duration
videos_table["duration_category"]=pd.cut(
    videos_table['duration_second'],
    bins=[60,300,600,float('inf')],
    labels=["short","medium","long"],
    include_lowest=True
)
print(videos_table["duration_category"].value_counts()
)
avr_view_by_duration=videos_table.groupby('duration_category')['views'].mean()
print(avr_view_by_duration)
plt.figure(figsize=(10,5))
avr_view_by_duration_table=plt.bar(avr_view_by_duration.index,avr_view_by_duration.values)
plt.bar_label(avr_view_by_duration_table)
plt.title("Average View by duration")
plt.xlabel("Duration Category")
plt.ylabel("Average view")
plt.show()
