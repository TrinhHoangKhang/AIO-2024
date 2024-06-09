from collections import deque
'''
Cho một list các số nguyên num_list và một sliding window có kích thước size k di
chuyển từ trái sang phải. Mỗi lần dịch chuyển 1 vị trí sang phải có thể nhìn thấy
đươc k số trong num_list và tìm số lớn nhất trong k số này sau mỗi lần trượt k phải
lớn hơn hoặc bằng 1
- Input: num_list, k
- Output: List chứa các phần tử lớn nhất của mỗi cửa sổ

'''


'''
Cách 1: Brute force
Kiểm tra từng cửa sổ
Với từng cửa sổ, ta dò tuyến tính để tìm số lớn nhất
'''
def solve1(num_list, k):
    # Kiểm tra list có đủ dài không
    if len(num_list) < k:
        print ('List có độ dài nhỏ hơn k!')
        return 
    
    result = []

    # Duyệt từng cửa sổ
    for i in range(0, len(numList) - k + 1):
        sub_list = numList[i:i+k]

        # Tìm số lớn nhất trong cửa sổ hiện tại
        max_num = -999999999
        for j in sub_list:
            if j > max_num:
                max_num = j

        result.append(max_num)

    return result


'''
Cách 2: Sử dụng deque
Phần tử đầu tiên của deque sẽ là số lớn nhất trong cửa sổ hiện tại
Mỗi khi dịch chuyển cửa sổ, ta sẽ thêm phần tử mới vào cuối deque
- Nếu phần tử mới thêm vào lớn hơn phần tử đầu deque, thì cứ pop phần tử đầu ra
- Hoặc nếu độ dài deque lớn hơn k, pop phần tử đầu ra
'''
def solve2(num_list, k):
    # Kiểm tra list có đủ dài không
    if len(num_list) < k:
        print ('List có độ dài nhỏ hơn k!')
        return
    
    result = []
    deq = deque()
    deq.append(numList[0]) # Thêm sẵn 2 phần tử đầu tiên
    deq.append(numList[1])

    for i in range(2, len(num_list)): # Duyệt từ phần tử thứ 3 đến cuối
        deq.append(numList[i])

        while (deq[0] < deq[-1]) or len(deq) > k:
            deq.popleft()

        result.append(deq[0])
    
    return result

# Test
if __name__ == "__main__":
    numList = [3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1]
    k = 3

    print('Brute force: ', solve1(numList, k))
    print('Deque:       ', solve2(numList, k))
        