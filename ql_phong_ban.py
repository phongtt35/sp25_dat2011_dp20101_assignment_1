# Chương trình con
# Quản lý phòng ban của nhân viên

def ql_phong_ban():
    print("Chương trình con")
    print("Quản lý phòng ban của nhân viên")
    print("")

    phong_ban = {}
    
    while True:
        print('\n1. Thêm phòng ban')
        print('2. Xem danh sách phòng ban')
        print('3. Sửa thông tin phòng ban')
        print('4. Xóa phòng ban')
        print('5. Thoát')
        
        chon = input('Chọn: ')
        
        if chon == '1':
            ma = input('Mã phòng ban: ')
            ten = input('Tên phòng ban: ')
            phong_ban[ma] = ten
            print('Đã thêm phòng ban.')
        elif chon == '2':
            if phong_ban:
                print('\nDanh sách phòng ban:')
                for ma, ten in phong_ban.items():
                    print(f'{ma}: {ten}')
            else:
                print('Không có phòng ban.')
        elif chon == '3':
            ma = input('Mã phòng ban cần sửa: ')
            if ma in phong_ban:
                phong_ban[ma] = input('Tên mới: ')
                print('Cập nhật thành công.')
            else:
                print('Không tìm thấy phòng ban này.')
        elif chon == '4':
            ma = input('Mã phòng ban cần xóa: ')
            if ma in phong_ban:
                del phong_ban[ma]
                print('Xóa thành công.')
            else:
                print('Không tìm thấy phòng ban này.')
        elif chon == '5':
            print('Thoát chương trình.')
            break
        else:
            print('Lựa chọn không hợp lệ, vui lòng nhập lại.')