# Chương trình con
# Quản lý công việc của từng nhân viên

# Quản lý công việc của từng nhân viên
def ql_cong_viec():
    while True:
        print("\n--- Quản lý công việc của từng nhân viên \n---")
        print("1. Thêm công việc")
        print("2. Sửa công việc")
        print("3. Xóa công việc")
        print("4. Xem danh sách công việc")
        print("0. Thoát")
        
        try:
            choice = int(input("Chọn chức năng (1-5): "))
        except ValueError:
            print("Vui lòng nhập một số từ 1 đến 5.")
            continue

        if choice == 1:
            them_cong_viec()
        elif choice == 2:
            sua_cong_viec()
        elif choice == 3:
            xoa_cong_viec()
        elif choice == 4:
            xem_danh_sach_cong_viec()
        elif choice == 5:
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

# Chương trình con
def them_cong_viec():
    ten_nv = input("Nhập tên nhân viên: ")
    cong_viec = input("Nhập công việc cần thêm: ")
    print(f"Đã thêm công việc '{cong_viec}' cho nhân viên {ten_nv}.")


def sua_cong_viec():
    ten_nv = input("Nhập tên nhân viên cần sửa công việc: ")
    cong_viec_moi = input("Nhập công việc mới: ")
    print(f"Đã cập nhật công việc cho nhân viên {ten_nv}: {cong_viec_moi}.")


def xoa_cong_viec():
    ten_nv = input("Nhập tên nhân viên cần xóa công việc: ")
    print(f"Đã xóa công việc của nhân viên {ten_nv}.")


def xem_danh_sach_cong_viec():
    print("Hiển thị danh sách công việc (chức năng chưa hoàn thiện).")