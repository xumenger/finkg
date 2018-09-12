# 加载pyfasttext模块
from pyfasttext import FastText 

# 加载一个已经存在的模型
# model = FastText()
# model.load_model('./path/to/model.bin')

# 使用skip-gram模型训练
skip_gram_model = FastText()
skip_gram_model.skipgram(input='./train.txt', output='skip_gram_model', epoch=100, lr=0.7)
print(skip_gram_model['贷款'])
# print(skip_gram_model.get_numpy_vector('贷款'))
# print(skip_gram_model.get_numpy_vector('贷款', normalized=True))

var1 = skip_gram_model.get_numpy_vector('人民币')
var2 = skip_gram_model.get_numpy_vector('贷款')
var3 = skip_gram_model.get_numpy_vector('外币')
skip_gram_model.words_for_vector(var1 + var2 - var3, k=1)

# for word in skip_gram_model.words:
#    print(word, skip_gram_model[word])

print(skip_gram_model.nearest_neighbors('贷款', k=2))

# test data is stored inside a file, use this:
# skip_gram_model.predict_proba_file('./test.txt', k=2)

print("\n")

##################
# 使用cbow模型训练 #
##################
cbow_model = FastText()
cbow_model.cbow(input='./train.txt', output='cbow_model', epoch=100, lr=0.7)
print(cbow_model['贷款'])
# print(cbow_model.get_numpy_vector('贷款'))
# print(cbow_model.get_numpy_vector('贷款', normalized=True))

var1 = cbow_model.get_numpy_vector('人民币')
var2 = cbow_model.get_numpy_vector('贷款')
var3 = cbow_model.get_numpy_vector('外币')
cbow_model.words_for_vector(var1 + var2 - var3, k=1)

# for word in cbow_model.words:
#    print(word, cbow_model[word])

print(cbow_model.nearest_neighbors('贷款', k=2))

# test data is stored inside a file, use this:
# cbow_model.predict_proba_file('./test.txt', k=2)
