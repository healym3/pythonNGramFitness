# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import ngram_score as ns


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    fitness = ns.ngram_score('quadgrams.txt')
    print fitness.score('ATTACKTHEEASTWALLOFTHECASTLEATDAWN')
    print fitness.score('FYYFHPYMJJFXYBFQQTKYMJHFXYQJFYIFBS')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
