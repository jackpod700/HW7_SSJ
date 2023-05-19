import numpy as np

def q2():
    Docs=np.array([[1,1,0,1,0,1],
                  [1,1,1,0,1,0],
                  [1,1,0,1,0,0]])
    Query=np.array([1,1,0,0,1,0])
    dot_products = np.dot(Docs, Query)

    doc_magnitudes = np.linalg.norm(Docs, axis=1)
    query_magnitude = np.linalg.norm(Query)

    cosine_similarities = dot_products / (doc_magnitudes * query_magnitude)

    print("doc1={0:0.2f}".format(cosine_similarities[0]))
    print("doc2={0:0.2f}".format(cosine_similarities[1]))
    print("doc3={0:0.2f}".format(cosine_similarities[2]))


if __name__=="__main__":
    q2()