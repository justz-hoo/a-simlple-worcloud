import numpy as np
from wordcloud import WordCloud, ImageColorGenerator#, STOPWORDS
import matplotlib.pyplot as plt
from PIL import Image
import jieba # cutting Chinese sentences into words


def count_frequencies(word_list):
    freq = dict()
    for w in word_list:
        if w not in freq.keys():
            freq[w] = 1
        else:
            freq[w] += 1
    return freq


def plt_imshow(x, ax=None, show=True):
    if ax is None:
        fig, ax = plt.subplots()
    ax.imshow(x)
    ax.axis("off")
    if show: plt.show()
    return ax

if __name__ == '__main__':
    # setting paths
    fname_text = 'daodao.txt'
    fname_stop = 'cn_stopwords.txt'
    fname_mask = 'pic.PNG'
    fname_font = 'C:/Windows/Fonts/simkai.ttf'
    Out_text_path = 'outfile.txt'

    text_input = open(fname_text, 'r', encoding='utf8')
    text_output = open(Out_text_path,'w' ,encoding='utf8')
    STOPWORDS_CH = open(fname_stop, encoding='utf8').read().split()

    for i in range(500):
        text_output.write("导导")
    for i in range(500):
        text_output.write("生日快乐")
    for line in text_input.readlines():
        if line == "\n" or line[0] == '2' or line[0] == '[':
            continue
        else:
            text_output.write(line)

    # 向jieba库中添加
    jieba.add_word("导导")
    text = open(Out_text_path, encoding='utf8').read()

    # processing texts: cutting words, removing stop-words and single-charactors
    word_list = [
            w for w in jieba.cut(text)
            if w not in set(STOPWORDS_CH) and len(w) > 1
            ]

    freq = count_frequencies(word_list)

    im_mask = np.array(Image.open(fname_mask))
    im_colors = ImageColorGenerator(im_mask)
    wcd = WordCloud(background_color='white',
                    mode='RGBA',
                    mask=im_mask,
                    font_path=fname_font,
    )
    wcd.generate_from_frequencies(freq)
    wcd.recolor(color_func=im_colors)

    ax = plt_imshow(wcd, )
    ax.figure.savefig(f'single_wcd.png', bbox_inches='tight', dpi=150)

    # fig, axs = plt.subplots(1, 2)
    # plt_imshow(im_mask, axs[0], show=False)
    # plt_imshow(wcd, axs[1])
    # fig.savefig(f'conbined_wcd.png', bbox_inches='tight', dpi=150)
