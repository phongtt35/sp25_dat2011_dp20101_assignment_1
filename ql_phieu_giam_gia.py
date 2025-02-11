# Chương trình con
# Quản lý công việc của từng nhân viên

def them_ma():
    print("Đã thêm mã")

def sua_ma():
    print("Đã sửa mã")

def xoa_ma():
    print("Đã xoá mã")  

def xem_ma():
    print("Đã xem mã")

def ql_phieu_giam_gia():
    print("Chương trình con")
    print("Quản lý công việc của từng nhân viên")
    print("")
    while True:
        print("\t1. Thêm mã giảm giá")
        print("\t2. Sửa mã giảm giá")
        print("\t3. Xoá mã giảm giá")
        print("\t4. Xem mã giảm giá")
        print("\t0. Thoát")

        lua_chon = input("Nhập lựa chọn của bạn: ")
        if lua_chon == "1":
            them_ma()
        elif lua_chon == "2":
            sua_ma()
        elif lua_chon == "3":
            xoa_ma()
        elif lua_chon == "4":
            xem_ma()
        elif lua_chon == "0":
            print("Đã thoát")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại!")
            print('\n')

if __name__ == "__main__": 
    ql_phieu_giam_gia()
