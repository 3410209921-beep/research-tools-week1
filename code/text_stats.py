# 文本词频统计示例程序
def count_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    words = text.split()
    return len(words)

if __name__ == "__main__":
    print("单词总数:", count_words("../sample.txt"))
