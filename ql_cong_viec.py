# Chương trình con
# Quản lý công việc của từng nhân viên
def ql_cong_viec():
    print("Chương trình con")
    print("Quản lý công việc của từng nhân viên")
    print("")
    while True:
        print("\t1. Thêm công việc cho nhân viên")
        print("\t2. Sửa công việc cho nhân viên")
        print("\t3. Xoá công việc của nhân viên")
        print("\t4. Tìm kiếm công việc của nhân viên")
        print("\t5. Xem công việc của nhân viên")
        print("\t0. Thoát")

        lua_chon = input("Nhập lựa chọn của bạn: ")
        if lua_chon == "1":
            them_cong_viec()
        elif lua_chon == "2":
            sua_cong_viec()
        elif lua_chon == "3":
            xoa_cong_viec()
        elif lua_chon == "4":
            tim_kiem_cong_viec()
        elif lua_chon == "5":
            xem_cong_viec()
        elif lua_chon == "0":
            print("Đã thoát")
            break
        else:
            print("Lựa chọn không hợp lệ!")
            print("Vui lòng thử lại")
            ql_cong_viec()

def them_cong_viec():
    print("Đã thêm công việc")
def sua_cong_viec():
    print("Đã sửa công việc")
def xoa_cong_viec():
    print("Đã xoá công việc")
def tim_kiem_cong_viec():
    print("Đã tìm kiếm thành công")
def xem_cong_viec():
    print("Đã xem công việc")
