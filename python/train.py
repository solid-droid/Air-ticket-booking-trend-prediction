import pandas as pd
import pickle
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split


def custom_round(x, base=2):
    return int(base * round(float(x)/base))


df = pd.read_csv("C:/Files/ML-Dataset/enter the travel verse/python/normalisedData.csv")


# print('ceating input/output')

# df.drop(df[df['DURATION'] < 0].index, inplace = True)
# df['DURATION'] = df['DURATION'].apply(lambda x: custom_round(x))

# df['MONTH'] = df['MONTH']/12
# df['DAY'] = df['DAY']/6
# df['WEEK'] = df['WEEK']/5
# df['TRIP_TYPE'] = df['TRIP_TYPE']/2

# df['START_LAT'] = df['START_LAT']/180
# df['START_LONG'] = df['START_LONG']/90
# df['END_LAT'] = df['END_LAT']/180
# df['END_LONG'] = df['END_LONG']/90


# df.rename(columns={
#     "START_LAT" : "START_LON",
#     "START_LONG" : "START_LAT",
#     "END_LAT" : "END_LON",
#     "END_LONG" : "END_LAT",
#     }, inplace=True)

# df.to_csv('normalisedData.csv', index=False)

X = df.drop(['DURATION'], axis=1)
y = df['DURATION']

print(X.head())

X = X.to_numpy()
y = y.to_numpy()


print('splitting')

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=10, random_state=1515)

print('training')

model = KNeighborsClassifier()
model.fit(X_train, y_train)

print('saving')

accuracy = model.score(X_test, y_test)
print(f'accuracy= {accuracy}')

pickle.dump(model, open('duration_model.sav', 'wb'))

    

   