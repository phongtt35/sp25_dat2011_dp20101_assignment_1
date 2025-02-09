# Chương trình con
# Quản lý nhân viên của công ty...
def menu():
    while True:
        print('1.Quản lý nhân viên.')
        print('2. Thoát')
        choice = input('Chọn chức năng: ')
        if choice == '1':
            ql_nhan_vien()
        elif choice == '2':
            print('Thoát chương trình')
            break
        else:
            print('Lựa chọn  không hợp lệ')

def ql_nhan_vien():
    while True:
        print('\n--- Quản lý Nhân Viên ---')
        print('1. Danh sách nhân viên')
        print('2. Thêm nhân viên')
        print('3. Xóa nhân viên')
        print('4. Cập nhật thông tin nhân viên')
        print('5. Tìm kiếm nhân viên')
        print('6. Quay lại menu chính')
        
        choice = input('Chọn chức năng: ')
        if choice == "1":
            danh_sach()
        elif choice == "2":
            them_nv()
        elif choice == "3":
            xoa_nv()
        elif choice == "4":
            cap_nhat()
        elif choice == "5":
            tim()
        elif choice == "6":
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại.")
            
def danh_sach():
    print('Danh sách nhân viên')
def them_nv():
    print('Thêm nhân viên')
def xoa_nv():
    print('Xóa nhân viên')
def cap_nhat():
    print('Cập nhật thông tin nhân viên')
def tim():
    print('Tìm nhân viên')
