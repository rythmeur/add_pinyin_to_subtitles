import codecs
import itertools
# from langdetect import detect_langs
from textblob import TextBlob
from pypinyin import pinyin, lazy_pinyin, Style


# if __name__ == "__main__":
with codecs.open(r".\The.Mandalorian.srt", "r", "gb2312") as f:

# with codecs.open(r"D:\Etude\Stanford\2018 Программирование на Pyhon\Погружение в Python\Homework\week4\29_Chinese.srt",
#                  "r", "utf_8_sig") as f:
    content = f.readlines()
    text = str()
    for line in content:
        if line is not None:
            text = text + line
            try: # detect langugage, if Chinese - add pinyin from google translate
                # probable_language = detect_langs (line)  # langdetect - poor quality of langue detection
                probable_language = TextBlob(line).detect_language()
                print(line)
                print("probable_language from TextBlob", probable_language)

                if 'zh' in probable_language:
                    pin_list = pinyin(line)
                    merged_pin_list = list(itertools.chain.from_iterable(pin_list))
                    print( pin_list)
                    print(merged_pin_list)

                    print(" ".join(pinyin(line)[0]))
                    result = ' '.join(merged_pin_list)

                    print(result)
                    if result is not None:
                        text = text + result
            except:
                pass

with codecs.open(r".\Chinese.srt", "w", 'utf_8_sig') as f:
    f.write(text)