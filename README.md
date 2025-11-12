## HW#32

### Module "text_sklearn_model.py" with class TextModel is implemented
* constructor takes string with sentences separated by dot
* method getAnswers(self, question: str, nAnswers: int)->list[str]

 takes string with question sentence and number of relevant answers
 
 returns list of strings-answers (maximal number of strings is the given nAnswers value) sorted by similarity (relevance) to the answer in the descending order

Result contains only sentences with non-zero similarity. If no such sentences, empty list is returned