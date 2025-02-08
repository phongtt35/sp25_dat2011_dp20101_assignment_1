# Chương trình con
# Quản lý hợp đồng của từng nhân viên

def xac_nhan():
    while True:
        y_n = input('Ban co muon tiep tuc thao tac khong (Y/N): ').upper()
        if y_n == 'Y':
            return True
        elif y_n == 'N':
            return False
        else:
            print('Lua chon khong hop le, vui long thao tac lai.')
def ql_hop_dong():
    print("Chương trình con")
    print("Quản lý hợp đồng của từng nhân viên")
    print("")
    print("1. Thêm hợp đồng")
    print("2. Xóa hợp đồng")
    print("3. Sửa hợp đồng")
    print("0. Thoát")

def them_hop_dong():
    print("Thêm hợp đồng...")

def xoa_hop_dong():
    print("Xóa hợp đồng...")

def sua_hop_dong():
    print("Sửa hợp đồng...")

def thoat():
    print('Ban da thoat')
def main():
    while True:
        ql_hop_dong()
        lua_chon = input('Mời chọn chức năng: ')

        if lua_chon == "1":
            if xac_nhan():
                them_hop_dong()
        elif lua_chon == "2":
            if xac_nhan():
                xoa_hop_dong()
        elif lua_chon == "3":
            if xac_nhan():
                sua_hop_dong
        elif lua_chon == "0":
            if xac_nhan():
                print('Ban đã thoát chương trình')
        else:
            print('Lua chon khong hợp le vui lòng nhap lại, nhap (0) để thoát: ')
main()

