def solution(phone_book):
    for i in phone_book:
        # 좋은 활용법 찾아서 비교하여 보기 좋아서 놔둠
        # phone_book_s = {}
        # for j in phone_book:
        #     if i != j: phone_book_s[j[0:len(i)]] = None
        phone_book_s = {j[0:len(i)] for j in phone_book if i != j}
        if i in phone_book_s: return False
    return True

phone_book = ["119", "97674223", "1195524421"]
r = solution(phone_book)
print(r)
phone_book = ["125","127","1235","567","88"]
r = solution(phone_book)
print(r)
