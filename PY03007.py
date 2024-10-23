import re


def process_text(text):
    # Tách các câu bằng dấu ngắt câu
    sentences = re.split(r'[.!?]', text)
    processed_sentences = []

    for sentence in sentences:
        # Bỏ khoảng trắng ở đầu và cuối câu
        sentence = sentence.strip()

        # Kiểm tra nếu câu có ít nhất 1 ký tự chữ cái hoặc chữ số
        if re.search(r'[a-zA-Z0-9]', sentence):
            # Đưa tất cả ký tự về thường và viết hoa ký tự đầu tiên
            sentence = sentence.lower()
            sentence = sentence.capitalize()
            processed_sentences.append(sentence)

    return processed_sentences


def main():
    input_text = ''
    # Đọc từng dòng cho đến khi không còn dòng nào
    try:
        while True:
            line = input()
            input_text += line + ' '  # Thêm khoảng trắng giữa các dòng
    except EOFError:
        pass  # Kết thúc khi không còn dòng nào

    processed_sentences = process_text(input_text.strip())

    for sentence in processed_sentences:
        print(sentence)


if __name__ == "__main__":
    main()
