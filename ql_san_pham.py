# Chương trình con
# Quản lý sản phẩm của công ty

def ql_san_pham():
    print("Chương trình con")
    print("Quản lý sản phẩm của công ty")
    while(True):
        print('1. Thêm sản phẩm')
        print('2. Xóa sản phẩm')
        print('3. Sửa sản phẩm')
        print('0. Thoát')
        choice = input()
        if choice == '1':
            print('Đã thêm sản phẩm')
        elif choice == '2':
            print('Đã xóa sản phẩm')
        elif choice == '3':
            print('Đã sửa sản phẩm')
        elif choice == '0':
            break
            return
        else:
            print('Không có sự lựa chọn, Again!')