# Chương trình con
# Quản lý khách hàng của công ty

def them_don_hang_khach_hang():
    print("Thêm đơn hàng khách hàng. ")
    
def sua_don_hang_khach_hang():
    print("Sửa đơn hàng khách hàng. ")
    
def xoa_don_hang_khach_hang():
    print("Xóa đơn hàng khách hàng. ")


def ql_khach_hang():
    while True:
        print("\nChương trình quản lý đơn hàng khách hàng")
        print("1. Thêm đơn hàng khách hàng")
        print("2. Sửa đơn hàng khách hàng")
        print("3. Xóa đơn hàng khách hàng")
        print("4. Thoát")
        
        chon = int(input("Chọn chức năng: "))
        
        if chon == 1:
            them_don_hang_khach_hang()
        elif chon == 2:
            sua_don_hang_khach_hang()
        elif chon == 3:
            xoa_don_hang_khach_hang()
        elif chon == 4:
            break
        else:
            print("Chọn chức năng không hợp lệ. ")
            
ql_khach_hang()