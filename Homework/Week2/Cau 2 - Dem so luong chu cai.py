'''
Viết function trả về một dictionary đếm số lượng chữ xuất hiện trong một từ, với key là chữ cái
và value là số lần xuất hiện
- Input: một từ
- Output: một dictionary

'''

# Note: Khi đếm không phân biệt chữ hoa chữ thường
def count_char(s):
    result = {}

    # Duyệt từng chữ cái trong từ
    for char in s:
        char = char.lower()
        if char in result:
            result[char] += 1
        else:
            result[char] = 1

    sorted_result = {key: result[key] for key in sorted(result.keys())}
    return sorted_result

# Test
if __name__ == '__main__':
    string1 = 'Happiness'
    print(count_char(string1))

    print('-----------------')
    string2 = 'smiles'
    print(count_char(string2))