import numpy
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

class TextModel:
    def __init__(self, text: str):
        arr = text.split(".")
        self.__clean_arr = [res for s in arr if (res := s.strip())]
        self.__vectorizer = TfidfVectorizer()
        self.__embeddings = self.__vectorizer.fit_transform(self.__clean_arr).toarray()
        
    def getAnswers(self, question: str, n: int):
        transformed_question = self.__vectorizer.transform([question]).toarray()
        res_vector = cosine_similarity(transformed_question, self.__embeddings)
        non_zero_indices = numpy.nonzero(res_vector[0])[0]
        best = numpy.argsort(res_vector)[0][::-1][:n]
        return [self.__clean_arr[i] for i in best if i in non_zero_indices]
      

if __name__ == "__main__":

    model = TextModel("An iterator is an object that contains a countable number of values.\
    An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.\
    Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().\
    Lists, tuples, dictionaries, and sets are all iterable objects. \
    They are iterable containers which you can get an iterator from.\
    All these objects have a iter() method which is used to get an iterator.\
    Even strings are iterable objects, and can return an iterator.\
    We can also use a for loop to iterate through an iterable object.")
    
    print(model.getAnswers("What is an iterator?", 3))