## notes sur le projet INF ML

graph d'entrainement = graph incomplet

base de test = N arrêtes manquantes (C=1) et N arrêtes non connéctées( C=0) dans le vrai graph ! 

Pb de classification de C

​	1.	Pré-prossessing = trouver des variables représentatives des liens les xi à partir des textes et du graph (cf node-embedding for graph reduction, text-embedding for text reduction)

 2. Modèle de classification 

    

  

##  To look into :

https://www.youtube.com/watch?v=5PL0TmQhItY :

Word2Vec : input : a word, hidden : an embedding of this word, output : the context of this w

[https://arxiv.org/abs/1301.3781]

*Co-occurence matrix* : count of words that appears in the same context/text + matrice décomposition

*GloVe* [https://nlp.stanford.edu/pubs/glove.pdf]

https://www.youtube.com/watch?v=QyrUentbkvw :

*Continuous Bag of Word* : context to focus word

*Skip-Gram* : focus word to context, best for rare words 

*hierarchical softmax* : tree vs *Negative Sampling*

<1 power to emphasize on rare words

*SVD* on co-occurence matrix

