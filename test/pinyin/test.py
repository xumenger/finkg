import pinyin
import pinyin.cedict

print("1. 汉语转拼音")
print(pinyin.get('你 好'))
print(pinyin.get('你好', format="strip", delimiter=" "))
print(pinyin.get('你好', format="numerical"))
print(pinyin.get_initial('你好'))


print("\n2.中文翻译为英文")
print(pinyin.cedict.translate_word('你'))
print(pinyin.cedict.translate_word('你好'))
print(list(pinyin.cedict.all_phrase_translations('你好')))
