# Chương trình con
# Quản lý khách hàng của công ty


def menu():
    while True:
        print('1.Quản lý khách hàng.')
        print('2. Thoát')
        choice = input('Chọn chức năng: ')
        if choice == '1':
            ql_khach_hang()
        elif choice == '2':
            print('Thoát chương trình')
            break
        else:
            print('Lựa chọn không hợp lệ')

def ql_khach_hang():
    while True:
        print('\n--- Quản lý Khách Hàng ---')
        print('1. Danh sách khách hàng')
        print('2. Thêm khách hàng')
        print('3. Xóa khách hàng')
        print('4. Cập nhật thông tin khách hàng')
        print('5. Tìm kiếm khách hàng')
        print('6. Quay lại menu chính')
        
        choice = input('Chọn chức năng: ')
        if choice == "1":
            danh_sach()
        elif choice == "2":
            them_kh()
        elif choice == "3":
            xoa_kh()
        elif choice == "4":
            cap_nhat()
        elif choice == "5":
            tim()
        elif choice == "6":
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại.")
            
def danh_sach():
    print('Danh sách khách hàng')
def them_kh():
    print('Thêm khách hàng')
def xoa_kh():
    print('Xóa khách hàng')
def cap_nhat():
    print('Cập nhật thông tin khách hàng')
def tim():
    print('Tìm khách hàng')

menu()


