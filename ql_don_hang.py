# Chương trình con
# Quản lý đơn hàng của khách hàng


def ql_don_hang():
    print("Chương trình con")
    print("Quản lý đơn hàng của khách hàng")
    print('-------------------')
    while(True):
        print('1. Thêm đơn hàng')
        print('2. Xem danh sách đơn hàng')
        print('3. Sửa đơn hàng')
        print('4. Xóa đơn hàng')
        print('5. Thoát đơn hàng')
        
        choice = input('chọn chức năng: ')
        if choice == '1':
            print('đã thêm 1')
        elif choice == '2':
            print('đã thêm 2')
        elif choice == '3':
            print('đã thêm 3')
        elif choice == '4':
            print('đã thêm 4')
        elif choice == '5':
            print('thoát')
            break
        else:
            print('chọn lại !!!')