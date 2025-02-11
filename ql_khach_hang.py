# Chương trình con
# Quản lý đơn hàng của khách hàng




def ql_khach_hang():
    print("Chương trình con")
    print("Quản lý đơn hàng của khách hàng")
    print("")
    
    ql_khach_hang = {}

    def them_khach_hang():
        ma = input('Mã khách hàng: ')
        if ma in ql_khach_hang:
            print('Mã khách hàng đã tồn tại.')
        else:
            ten = input('Tên khách hàng: ')
            ql_khach_hang[ma] = ten
            print('Đã thêm khách hàng.')

    def xem_danh_sach_khach_hang():
        if ql_khach_hang:
            print('\nDanh sách khách hàng:')
            for ma, ten in ql_khach_hang.items():
                print(f'{ma}: {ten}')
        else:
            print('Không có khách hàng.')

    def sua_thong_tin_khach_hang():
        ma = input('Mã khách hàng cần sửa: ')
        if ma in ql_khach_hang:
            ql_khach_hang[ma] = input('Tên mới: ')
            print('Cập nhật thành công.')
        else:
            print('Không tìm thấy khách hàng này.')

    def xoa_khach_hang():
        ma = input('Mã khách hàng cần xóa: ')
        if ma in ql_khach_hang:
            del ql_khach_hang[ma]
            print('Xóa thành công.')
        else:
            print('Không tìm thấy khách hàng này.')

    def main():
        while True:
            print('\n1. Thêm khách hàng')
            print('2. Xem danh sách khách hàng')
            print('3. Sửa thông tin khách hàng')
            print('4. Xóa khách hàng')
            print('5. Thoát')

            try:
                choice = int(input('Chọn: '))
                if choice == 1:
                    them_khach_hang()
                elif choice == 2:
                    xem_danh_sach_khach_hang()
                elif choice == 3:
                    sua_thong_tin_khach_hang()
                elif choice == 4:
                    xoa_khach_hang()
                elif choice == 5:
                    print('Thoát chương trình.')
                    break
                else:
                    print('Lựa chọn không hợp lệ, vui lòng nhập lại.')
            except ValueError:
                print('Vui lòng nhập một số hợp lệ.')

    main()


