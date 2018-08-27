import jieba

test_str = "李小福是创新办主任也是云计算方面的专家 "

print("【使用自定义词典前】")
seg_list = jieba.cut(test_str, cut_all=False)
print("/ ".join(seg_list))

print("\n【使用自定义词典后】")
jieba.load_userdict("./dict.txt")
seg_list = jieba.cut(test_str, cut_all=False)
print("/ ".join(seg_list))
