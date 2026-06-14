import numpy as np
import pandas as pd
movies=pd.read_csv("tmdb_5000_movies.csv.zip")
credits=pd.read_csv("tmdb_5000_credits.csv.zip")
movies.head()
credits.head()
movies=movies.merge(credits,on='title')
movies.head(1)
#genre
#keywords
#id
#title
#crew
#cast
#overview
movies=movies[['id','title','crew','cast','overview','keywords','genres']]
print(movies)
movies.info()
movies.isnull().sum()
movies.dropna(inplace=True)
movies.duplicated().sum()
movies.iloc[0].genres
def convert(obj):
    L=[]
    for i in ast.literal_eval(obj):
        L.append(i['name'])
    return L
import ast
ast.literal_eval
convert('[{"id": 28, "name": "Action"}, {"id": 12, "name": "Adventure"}, {"id": 14, "name": "Fantasy"}, {"id": 878, "name": "Science Fiction"}]')
movies['genres']=movies['genres'].apply(convert)
movies['keywords']=movies['keywords'].apply(convert)
movies['keywords']
movies['genres']
movies['cast'][0]
import ast

def convert3(obj):
    L = []
    counter = 0

    for i in ast.literal_eval(obj):
        if counter != 3:
            L.append(i['name'])
            counter += 1
        else:
            break

    return L
movies['cast'] = movies['cast'].apply(convert3)
movies['cast']
def fetchdirector(obj):
    L=[]
    for i in ast.literal_eval(obj):
        if i['job']=='Director':
            L.append(i['name'])
    return L
movies['crew']=movies['crew'].apply(fetchdirector)
movies['crew'][0]
movies.head()
type(movies['overview'][0])
movies['overview']=movies['overview'].apply(lambda x:x.split())
movies['genres']=movies['genres'].apply(lambda x:[i.replace(" ","") for i in x])
movies['overview']=movies['overview'].apply(lambda x:[i.replace(" ","") for i in x])
movies['keywords']=movies['keywords'].apply(lambda x:[i.replace(" ","") for i in x])
movies['cast']=movies['cast'].apply(lambda x:[i.replace(" ","") for i in x])
movies['crew']=movies['crew'].apply(lambda x:[i.replace(" ","") for i in x])
movies['tags']=movies['overview']+movies['keywords']+movies['crew']+movies['cast']+movies['genres']
movies['tags'][0]
new_df=movies[['tags','id','title']]
new_df.head()
new_df['tags']=new_df['tags'].apply(lambda x:" ".join(x))
new_df['tags']=new_df['tags'].apply(lambda x:x.lower())
import nltk
from nltk.stem.porter import PorterStemmer
ps=PorterStemmer()
def stem(text):
    y=[]
    for i in text.split():
        y.append(ps.stem(i))
    return " ".join(y)
new_df['tags']=new_df['tags'].apply(stem)
new_df['tags'][0]
 ## Text Vectorization

#### BAG OF WORDS
##### STEPS
#1. make every movie a vector and when we ask for recommendation we return the closest vectors
#2. making vectors out of words/overview of the movie which icludes all the characteristics
#3. extracting most common words / tags using frequency of their used.Ex-5000
#4. making a table of most common words with the that word used in that movie


#5. sabse pehle sare tags ko add krdia
#6. woh large text se 5000 most common words nikallo
#7. using their frequency
#8. fir har movie ke tag ko firse uthana fir dekho us 5000 main se words kistni bar us ek movie ke tag m aye
#   w1 w2 w3..............w5000
#m1 5 10   2              56
#m2 1 2    3               4
#m3 2 4    56              32
#m5000 1 2 3                3
#table of 5000(movies),5000(no of common words)
#this every row is a vector of that partiulcar movie
#* can take any amount of common words
from sklearn.feature_extraction.text import CountVectorizer
print(type(new_df['tags'].iloc[0]))
print(new_df['tags'].iloc[0])
cv=CountVectorizer(max_features=5000,stop_words='english')
vectors= cv.fit_transform(new_df['tags']).toarray()
vectors
vectors[0]
len(cv.get_feature_names_out())
cv.get_feature_names_out()
stem('in the 22nd century, a paraplegic marine is dispatched to the moon pandora on a unique mission, but becomes torn between following orders and protecting an alien civilization. cultureclash future spacewar spacecolony society spacetravel futuristic romance space alien tribe alienplanet cgi marine soldier battle loveaffair antiwar powerrelations mindandsoul 3d jamescameron samworthington zoesaldana sigourneyweaver action adventure fantasy sciencefiction')
# we will calculate the cosine distance btw vectors and not the euclidian distance
#distance is inversely to similarity
from sklearn.metrics.pairwise import cosine_similarity
print(vectors.shape)
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

similarity = cosine_similarity(vectors).astype(np.float32)

print(similarity.shape)
sorted(
    list(enumerate(similarity[0])),
    reverse=True,
    key=lambda x: x[1]
)[1:6]
def recommend(movie):
    movie_index=new_df[new_df['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(
    list(enumerate(distances)),
    reverse=True,
    key=lambda x: x[1]
)[1:6]
    for i in movies_list:
        print(new_df.iloc[i[0]].title)
#print(i[0])
    return
recommend('Batman Begins')
import pickle
pickle.dump(new_df.to_dict(),open('movie_dict.pkl','wb'))
new_df['title'].values
pickle.dump(similarity,open('similarity.pkl','wb'))
print("movie_dict.pkl created")
print("similarity.pkl created")
