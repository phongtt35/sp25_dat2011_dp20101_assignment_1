# Chương trình con
# Quản lý danh mục của sản phẩm

def ql_danh_muc():
    while True:
        print("1.Quản lý danh mục")
        print("0.Thoát")
        chon = input("Chọn chức năng: ")
        if chon == '1':
            ql_danh_muc()
        elif chon == '0':
            print("Thoát chương trình quản lý danh mục")
            break
        else:
            print("Không có chức năng đó.")

def ql_danh_muc():
    while True:
        print("\n === Quản lý danh mục ===")
        print("1. Xem danh sách danh mục")
        print("2. Thêm danh mục")
        print("3. Sửa danh mục")
        print("4. Xóa danh mục")
        print("5. Tìm kiếm danh mục")
        print("0. Thoát")

        chon = input("Chọn chức năng: ")
        if chon == '1':
            xem_danh_sach_danh_muc()
        elif chon == '2':
            them_danh_muc()
        elif chon == '3':
            sua_danh_muc()
        elif chon == '4':
            xoa_danh_muc()
        elif chon == '5':
            tim_kiem_danh_muc()
        elif chon == '0':
            print("Thoát chương trình quản lý danh mục")
            break
        else:
            print("Không có chức năng đó.")


def xem_danh_sach_danh_muc():
    print("=== Danh sách danh mục ===")
def them_danh_muc():
    print("=== Thêm danh mục ===")
def sua_danh_muc():
    print("=== Sửa danh mục ===")
def xoa_danh_muc():
    print("=== Xóa danh mục ===")
def tim_kiem_danh_muc():
    print("=== Tìm kiếm danh mục ===")
