We've implemented item-item collaborative filtering in our assignment as it outperforms user-user CF.
The script can be run by typing:			python assign.py

We have used movielens movie recommendation dataset which can be found on the following link:	http://www.grouplens.org/node/73

Following is the description of functions & main data structures used in our assignment:

matrix[][] : this is a dictionary of dictonaries. matrix[u] gives a dictionary of movies and ratings for user u.

pearson(x,y): this function finds the pearson correlation between 2 movie items x and y.

itemitem(x,i): this function predicts what rating user x gives to movie i. The no. of neighbors(i.e most similar items to item i) considered in the set is 20. A weighted mean calculation for the items in the neighborhood set is used as a predicting function.

populate(fname): this function is used to populate our dictionary matrix from the data file fname.

recommend(y): this is a driver function which combines the above modules and gives 10 recommendations for the user y.

Thank You.


