import re
import operator


def top_3_words(text):
    wordsDict = dict()
    sortedDict = dict()
    topWords = list()
    regex = re.compile(r"[a-zA-Z']*'*?[a-zA-Z']*?[^\s_!.,:?;\-/]")
    words = regex.findall(text.lower())
    for word in words:
        if word not in wordsDict and word != "'" and word != "'''":
            wordsDict[word] = 1
        elif word != "'" and word != "'''":
            wordsDict[word] += 1
    sortedDict = sorted(wordsDict.items(), key=operator.itemgetter(1), reverse=True)
    for index in range(min(3, len(sortedDict))):
        topWords.append(sortedDict[index][0])
    return topWords
