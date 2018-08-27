import jieba.posseg as pseg

text = "线程是程序执行时的最小单位，它是进程的一个执行流，是CPU调度和分派的基本单位。"

words = pseg.cut(text)
for w in words:
    print(w.word + " " + w.flag)
