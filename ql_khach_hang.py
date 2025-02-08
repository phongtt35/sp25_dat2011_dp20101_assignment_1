# Chương trình con
# Quản lý khách hàng của công ty

def them_khach_hang():
    print("Thêm khách hàng. ")
    
def sua_khach_hang():
    print("Sửa khách hàng. ")
    
def xoa_khach_hang():
    print("Xóa khách hàng. ")


def ql_khach_hang():
    while (True):
        print("Chương trình quản lý khách hàng")
        print("1. Thêm khách hàng")
        print("2. Sửa khách hàng")
        print("3. Xóa khách hàng")
        print("4. Thoát")
        
        chon = int(input("Chọn chức năng: "))
        
        if chon == 1:
            them_khach_hang()
        elif chon == 2:
            sua_khach_hang()
        elif chon == 3:
            xoa_khach_hang()
        elif chon == 4:
            break
        else:
            print("Chọn chức năng không hợp lệ. ")
            
ql_khach_hang()