import thulac

print("1. 默认模式")
t1 = thulac.thulac()
# 进行一句话分词
text = t1.cut("我在学习自然语言处理技术", text = True)
print(text)
print("\n")

print("2. 只进行分词，不进行词性标注")
t2 = thulac.thulac(seg_only = True)
#对input.txt文件内容进行分词，输出到output.txt
t2.cut_f("input.txt", "output.txt")
