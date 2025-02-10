# Chương trình Quản lý doanh nghiệp VIP PRO

import ql_cham_cong, ql_nhan_vien, ql_cong_viec, ql_hop_dong, ql_khach_hang, ql_don_hang, ql_san_pham, ql_phieu_giam_gia, ql_phong_ban, ql_danh_muc

def menu():
    print("=====================================")
    print("Chương trình Quản lý doanh nghiệp VIP PRO")
    print("\t1. Quản lý chấm công của nhân viên")
    print("\t2. Quản lý nhân viên của công ty")
    print("\t3. Quản lý việc của từng nhân viên")
    print("\t4. Quản lý hợp đồng của từng nhân viên")
    print("\t5. Quản lý khách hàng của công ty")
    print("\t6. Quản lý đơn hàng của khách hàng")
    print("\t7. Quản lý sản phẩm của công ty")
    print("\t8. Quản lý phiếu giảm giá của công ty")
    print("\t9. Quản lý phòng ban của công ty")
    print("\t10. Quản lý danh mục của sản phẩm")
    print("\t99. Thoát chương trình")

tu_dien_chuc_nang = {
    '1': ql_cham_cong.ql_cham_cong,
    '2': ql_nhan_vien.ql_nhan_vien,
    '3': ql_cong_viec.ql_cong_viec,
    '4': ql_hop_dong.ql_hop_dong,
    '5': ql_khach_hang.ql_khach_hang,
    '6': ql_don_hang.ql_don_hang,
    '7': ql_san_pham.ql_san_pham,
    '8': ql_phieu_giam_gia.ql_phieu_giam_gia,
    '9': ql_phong_ban.ql_phong_ban,
    '10': ql_danh_muc.ql_danh_muc,
    '99': exit
}

def main():
    while True:
        menu()
        chon = input("Chọn chức năng: ")
        if chon in tu_dien_chuc_nang:
            tu_dien_chuc_nang[chon]()
        else:
            print("Chức năng không tồn tại")
        print('\n')

main()