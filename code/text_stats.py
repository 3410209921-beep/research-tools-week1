# 文本词频统计示例程序
import os
import re
import sys
from collections import Counter


def load_text(file_path):
    """读取 UTF-8 文本文件并返回内容字符串。"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


def extract_words(text):
    """
    从文本中提取英文单词（统一转为小写）。
    使用正则表达式只保留字母，去除标点和数字。
    """
    return re.findall(r'[a-z]+', text.lower())


def count_words(file_path):
    """统计文件中的单词总数。"""
    words = extract_words(load_text(file_path))
    return len(words)


def word_frequency(file_path, top_n=5):
    """
    统计文件中每个单词的出现频率，返回出现次数最多的前 top_n 个单词。
    返回格式: [(word, count), ...]
    """
    words = extract_words(load_text(file_path))
    return Counter(words).most_common(top_n)


def self_test():
    """
    自测函数：使用一段内置文本验证 count_words 和 word_frequency 的正确性。
    无需外部文件即可运行。
    """
    test_text = "apple banana apple cherry banana apple date cherry fig grape banana"
    words = extract_words(test_text)

    # 验证单词总数
    expected_total = 11
    actual_total = len(words)
    assert actual_total == expected_total, \
        f'单词总数不通过: 期望 {expected_total}, 实际 {actual_total}'

    # 验证词频统计
    freq = Counter(words).most_common(5)
    expected_freq = [('apple', 3), ('banana', 3), ('cherry', 2), ('date', 1), ('fig', 1)]
    assert freq == expected_freq, \
        f'词频统计不通过: 期望 {expected_freq}, 实际 {freq}'

    print('[自测通过]')
    print(f'  单词总数: {actual_total}')
    print(f'  Top 5 高频词:')
    for rank, (word, cnt) in enumerate(freq, start=1):
        print(f'    {rank}. {word}: {cnt} 次')
    return True


if __name__ == '__main__':
    # 如果带 --test 参数则运行自测
    if len(sys.argv) > 1 and sys.argv[1] == '--test':
        self_test()
        sys.exit(0)

    # 使用 __file__ 定位脚本所在目录，从而兼容从任意目录运行
    script_dir = os.path.dirname(os.path.abspath(__file__))
    sample_path = os.path.join(script_dir, '..', 'sample.txt')

    print(f'单词总数: {count_words(sample_path)}')
    print()
    print('出现次数最多的前 5 个单词:')
    for rank, (word, cnt) in enumerate(word_frequency(sample_path, 5), start=1):
        print(f'  {rank}. {word}: {cnt} 次')
