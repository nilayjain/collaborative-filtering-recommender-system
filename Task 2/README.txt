We've used the crab recommender framework in this assignment.
It provides us with 3 models User-based(knn), Item-based(knn) 
and SVD.We've implemented SVD and User-based Collaborative
Filtering.

The matrix is stored in the form of a dictionary of 
dictionaries.This matrix is passed into the function
MatrixPreferenceDataModel. This class expects a simple
dictionary where each element contains a userID, 
followed by itemID, followed by a rating.

User-based:-
For User-based filtering the model is passed into the
funtion UserSimilarity. Distance function pearson_correlation
is the second parameter .This returns a dictionary of
dictionaries containing User:Similarity pairs for every
user.Similarity values are in the range 0-1.

The model and the similarity data structures are passed into
the recommender class UserBasedRecommender. This calculates
estimated ratings for all the null spaces in the matrix.
The function recommend in the class takes in input user_id
and returns all the recommendations for this user in a sorted
manner.

SVD:-
We use the ItemsNeighborhoodStrategy. It returns all items
that have not been rated by the user and were preferred by
another user that has preferred at least one item that the
current has preferred too. Now,this and the model is passed
into the MatrixFactorBasedRecommender. The recommender uses
a Expectation Maximization algorithm.

The recommend function takes input x(user_id) and returns 
recommendations for user x.


Time Analysis:

We use the time command on linux to find out how much time 
it takes for the script.It returns 3 values real,user and sys.
	real - refers to the actual elasped time
	user - refers to the amount of cpu time spent 
	outside of kernel
	sys - refers to the amount of cpu time spent 
	inside kernel specific functions

User-based: 
We ran the script on a database of 25 users and less than
100 items.We got the following results on running the code 
on 5 different instances(different user_id input).

for user_id:1(returned 6 recommendations)
real	0m4.609s
user	0m3.474s
sys	0m0.024s

for user_id:4(returned 12 recommendations)
real	0m7.083s
user	0m6.104s
sys	0m0.030s

for user_id:23(returned 32 recommendations)
real	0m15.306s
user	0m14.483s
sys	0m0.043s

for user_id:17(returned 36 recommendations)
real	0m18.979s
user	0m18.083s
sys	0m0.062s

for user_id:19(returned 8 recommendations)
real	0m5.605s
user	0m4.497s
sys	0m0.025s

SVD:
We ran this script on a database of ~1000 users and ~1600
items(20000 ratings).We checked time for 3 inputs.

for user_id:25
real	0m16.205s
user	0m14.990s
sys	0m0.036s

for user_id:254
real	0m15.041s
user	0m14.734s
sys	0m0.038s

for user_id:666
real	0m17.603s
user	0m17.218s
sys	0m0.041s
