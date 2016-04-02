from scikits.crab.models import MatrixPreferenceDataModel
from scikits.crab.metrics import pearson_correlation
from scikits.crab.similarities import UserSimilarity
from scikits.crab.recommenders.knn import UserBasedRecommender
from scikits.crab.recommenders.svd.classes import MatrixFactorBasedRecommender
from scikits.crab.recommenders.knn.item_strategies import ItemsNeighborhoodStrategy

y=input('type 1 for knn(UserBased) or 2 for SVD model: ')
if y == 1:
	f='1.txt'
else:
	f='u5.test'

data={}
i = 1
for d in range(1,1000):
	data[d]={}

with open(f) as file:
	for line in file:
		data[int(line.split()[0])][int(line.split()[1])]=int(line.split()[2])

model = MatrixPreferenceDataModel(data)

if y == 1:
	similarity = UserSimilarity(model, pearson_correlation)
	recommender = UserBasedRecommender(model, similarity, with_preference=True)	
	x=input('type userid(1-25): ')	
	print(recommender.recommend(x))
else:
	items_strategy = ItemsNeighborhoodStrategy()
	recommender = MatrixFactorBasedRecommender(model, items_strategy, 2)
	x=input('type userid: ')	
	print(recommender.recommend(x))

		

