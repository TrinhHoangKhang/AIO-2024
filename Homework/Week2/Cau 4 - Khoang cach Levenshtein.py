'''
Tìm số bước để biến đổi từ xâu s1 thành xâu s2
Mỗi bước được thực hiện 1 trong 3 thao tác: thêm, xóa, sửa
- Input: xâu s1, xâu s2
-> In ra số bước và các bước biến đổi
- Output: None

'''

def find_Levenshtein_distance(s1, s2):
    # Tạo một bảng có số hàng là len(s2) + 1, số cột là len(s1) + 1

    # Tạo thêm một bảng traceback để dò ngược lại đường sau khi chúng ta tính xong
    # Traceback[i][j] sẽ chứa 1 trong 2 giá trị: 'sub', 'add', 'del'. Chỉ ra trước
    # đó chúng ta đã thực hiện thao tác gì để đến được ô hiên tại
    table = []
    traceback = []

    # Khởi tạo 2 bảng
    for i in range(len(s2) + 1):
        row = []
        traceback_row = []
        for j in range(len(s1) + 1):
            row.append(0)
            traceback_row.append('')

        table.append(row)
        traceback.append(traceback_row)
    
    # Dòng đầu tiên của bảng sẽ là: 0, 1, 2, 3, 4, ...
    # Cột đầu tiên của bảng sẽ là: 0, 1, 2, 3, 4, ...
    for i in range(1, len(s1) + 1):
        table[0][i] = i
        traceback[0][i] = 'del'
    for i in range(1, len(s2) + 1):
        table[i][0] = i 
        traceback[i][0] = 'add'

    # ========================================================================
    # Duyệt các ô và tính giá trị cho ô đó, đồng thời cập nhật traceback
    for i in range(1, len(s2) + 1):
        for j in range(1, len(s1) + 1):
            # Nếu sửa
            sub_cost = table[i - 1][j - 1]
            if s1[j - 1] != s2[i - 1]:
                sub_cost += 1

            # Nếu thêm
            add_cost = table[i - 1][j] + 1

            # Nếu xóa
            del_cost = table[i][j - 1] + 1

            table[i][j] = min(sub_cost, add_cost, del_cost)

            # Cập nhật traceback
            if table[i][j] == sub_cost:
                traceback[i][j] = 'sub'
            elif table[i][j] == add_cost:
                traceback[i][j] = 'add'
            else:
                traceback[i][j] = 'del'

    # ========================================================================
    # Dùng traceback để truy ngước lại đường đi và in ra kết quả
    route = []
    i = len(s2) # Bắt đầu tại vị trí góc dưới bên phải
    j = len(s1)
    current_position = traceback[i][j]
    while current_position != '':
        if current_position == 'sub':
            if s1[j - 1] != s2[i - 1]:
                route.append(f'sub: {s1[j - 1]} -> {s2[i - 1]}')
            i -= 1
            j -= 1
        
        if current_position == 'add':
            route.append(f'add: {s2[i - 2]}')
            i -= 1
    
        if current_position == 'del':
            route.append(f'del: {s1[j - 2]}')
            j -= 1
        
        current_position = traceback[i][j]

    # Đảo ngược route do ta nạp ngược từ dưới lên
    route = route[::-1]

    # In kết quả
    print(f'Cần tổng cộng {table[-1][-1]} bước')
    for i in route:
        print(i)

# Test
if __name__ == '__main__':
    print('Test 1')
    print("From 'cat' to 'cot'")
    find_Levenshtein_distance('cat', 'cot')

    print('\nTest 2')
    print("From 'kitten' to 'sitting'")
    find_Levenshtein_distance('kitten', 'sitting')

    print('\nTest 3')
    print("From 'yu' to 'you'")
    find_Levenshtein_distance('yu', 'you')