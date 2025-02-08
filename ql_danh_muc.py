# Chương trình con
# Quản lý danh mục của sản phẩm
danh_muc = []
def ql_danh_muc():
    print("1.Thêm danh mục sản phẩm ")
    print("2.Sửa danh mục sản phẩm ")
    print("3.Xóa danh mục sản phẩm")
    print("4.Xem danh mục sản phẩm ")
    print("0.Thoát.")

def lua_chon_menu_danh_muc():
    lua_chon = input("chọn chức năng: ")
    return lua_chon

def chuc_nang_1():
    ten_danh_muc = input("Nhập tên danh mục: ")
    danh_muc.append(ten_danh_muc)
    print("Đã thêm danh mục sản phẩm thành công.")

def chu_nang_2():
    ten_danh_muc = input("Nhập tên danh mục cần sửa: ")
    if ten_danh_muc in danh_muc:
        ten_moi = input("Nhập tên mới: ")
        vi_tri = danh_muc.index(ten_danh_muc)
        danh_muc[vi_tri] = ten_moi
        print("Đã sửa danh mục sản phẩm thành công.")
    else:
        print("Danh mục sản phẩm không tồn tại.")

def chuc_nang_3():
    ten_danh_muc = input("Nhập tên danh mục cần xóa: ")
    if ten_danh_muc in danh_muc:
        danh_muc.remove(ten_danh_muc)
        print("Đã xóa danh mục sản phẩm thành công.")
    else:
        print("Danh mục sản phẩm không tồn tại.")

def chuc_nang_4():
    print("Danh mục sản phẩm: ")
    for ten_danh_muc in danh_muc:
        print(ten_danh_muc)

def chuc_nang_0():
    print("Thoát chương trình quản lý danh mục sản phẩm.")

while True:
    ql_danh_muc()
    lua_chon = lua_chon_menu_danh_muc()
    if lua_chon == '1':
        chuc_nang_1()
    elif lua_chon == '2':
        chu_nang_2()
    elif lua_chon == '3':
        chuc_nang_3()
    elif lua_chon == '4':
        chuc_nang_4()
    elif lua_chon == '0':
        chuc_nang_0()
        break

