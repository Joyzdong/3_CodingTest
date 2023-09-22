def solution(phone_book):
    phone_dict = dict.fromkeys(phone_book)
    for phone in phone_book:
        for i in range(1, len(phone)):
            if phone[:i] in phone_dict:
                return False
    return True

