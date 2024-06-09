'''
Viết function đọc các câu trong một file txt, đếm số lượng các từ xuất hiện và trả về một dictionary
với key là từ và value là số lần từ đó xuất hiện.
- Input: đường dẫn đến file txt
- Output: dictionary

'''

file_path = 'E:\AIO 2024\AIO-2024\AIO-2024\Homework\Week2\P1_data.txt'
def count_words(file_path):
    result = {}

    # Mở file
    open_file = open(file_path, 'r')
    lines = open_file.readlines()
    open_file.close()

    # Duyệt từng dòng
    for line in lines:
        words = line.split() # Tách từ trong dòng

        # Duyệt từng từ
        for word in words:
            word = word.lower()
            if word in result:
                result[word] += 1
            else:
                result[word] = 1

    sorted_result = {key: result[key] for key in sorted(result.keys())}
    return sorted_result

# Test
if __name__ == '__main__':
    print(count_words(file_path))