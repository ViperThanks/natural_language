from collections import defaultdict
import operator


def generate_ngram(text, n=1):
    # 分词
    words = text.strip().split()

    # 生成ngram
    ngrams = []
    for i in range(len(words) - n + 1):
        ngram = ''.join(words[i:i + n])
        ngrams.append(ngram)

    return ngrams


def generate_1gram_model(text):
    # 生成1-gram模型
    freq_dict = defaultdict(int)
    total_words = 0

    # 遍历每一个单词，统计频率
    for word in text:
        freq_dict[word] += 1
        total_words += 1

    # 按照词频从大到小排序
    sorted_freq_dict = sorted(freq_dict.items(), key=operator.itemgetter(1), reverse=True)

    # 计算每个单词在文本中出现的频率
    prob_dict = {}
    for word, freq in sorted_freq_dict:
        prob_dict[word] = freq / total_words

    return prob_dict


def save_1gram_model(model, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for word, prob in model.items():
            f.write(f'{word} {prob:.6f}\n')


def main():
    with open('../作业二/output.txt', 'r', encoding='utf-8') as f:
        text = f.read()

    # 分别生成1-gram模型
    ngrams = generate_ngram(text, n=1)
    model1 = generate_1gram_model(ngrams)

    with open('target2.txt', 'r', encoding='utf-8') as f:
        text = f.read()

    ngrams = generate_ngram(text, n=1)
    model2 = generate_1gram_model(ngrams)

    # 将模型保存到文件中
    save_1gram_model(model1, '1gram_target1.txt')
    save_1gram_model(model2, '1gram_target2.txt')


if __name__ == '__main__':
    main()
