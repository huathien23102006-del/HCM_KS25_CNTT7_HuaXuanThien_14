class RestaurantBill:
    def __init__(self, id, customer_name, table_number, food_amount, vat_rate, service_fee, discount):
        self.id = id
        self.customer_name = customer_name
        self.table_number = table_number
        self.food_amount = food_amount
        self.vat_rate = vat_rate
        self.service_fee = service_fee
        self.discount = discount

        self.total_bill = 0
        self.bill_type = ""

        self.calculate_total_bill()
        self.classify_bill()

    def calculate_total_bill(self):
        self.total_bill = (self.food_amount * vat_rate ) / 100

    def classify_bill(self):
        if self.total_bill >= 5000000:
            self.bill_type = "VIP"
        elif self.total_bill >= 2000000:
            self.bill_type = "Lớn"
        elif self.total_bill >= 500000:
            self.bill_type = "Trung bình"
        else:
            self.bill_type = "Nhỏ"

class RestaurantBillManager:
    def __init__(self):
        self.bills = []

    def check_value_id(self, id):
        for b in self.bills:
            if b.id == id:
                return True
        return False

    def add_bill(self):
        try:
            id = input("Nhập mã hóa đơn: ")

            if not id:
                print("Mã hóa đơn không được để trống!")
                return

            if self.check_value_id(id):
                print("Mã hóa đơn không được trùng!")
                return

            customer_name = input("Nhập tên khách hàng: ")

            if not customer_name:
                print("Tên khách hàng không được để trống!")
                return
            
            table_number = input("Nhập số bàn: ")
            if not table_number:
                print("Số bàn không được để trống!")
                return

            food_amount = float(input("Nhập tiền món ăn: "))
            if food_amount < 0:
                print("Tiền món ăn phải lớn hơn hoặc bằng 0!")
                return
            
            vat_rate = float(input("Nhập vào tỷ lệ VAT: "))
            if vat_rate < 0 or vat_rate > 100:
                print("Tỷ lệ VAT phải là số từ 0 đến 100!")
                return
            
            service_fee = float(input("Nhập vào phí dịch vụ: "))
            if service_fee < 0:
                print("Phí dịch vụ phải lớn hơn hoặc bằng 0!")
                return
            
            discount = float(input("Giảm giá: "))
            if discount < 0:
                print("Giảm giá phải lớn hơn hoặc bằng 0!")
                return
            
            new_bill = RestaurantBill(
                id,
                customer_name,
                table_number,
                food_amount,
                vat_rate,
                service_fee,
                discount
            )
            self.bills.append(new_bill)
            print("Thêm hóa đơn bàn ăn thành công!")
        except:
            print("Lỗi! Dữ liệu nhập vào không hợp lệ!")

    def show_all(self):
        if not self.bills:
            print("Danh sách hóa đơn bàn ăn đang rỗng!")
            return
        print("Danh sách hóa đơn bàn ăn")
        print(f"{'Mã hóa đơn':<10} | " f"{'Tên khách hàng':<20} | " f"{'Số bàn':<15} | " f"{'Tiền món ăn':<20} | " f"{'Tỷ lệ VAT':<20} | " f"{'Phí dịch vụ':<20} | " f"{'Giảm giá':<20} | " f"{'Tổng tiền hóa đơn':<25} | " f"{'Phân loại hóa đơn':<25}")
        for bill in self.bills:
            print(f"{bill.id:<10} | " f"{bill.customer_name:<20} | " f"{bill.table_number:<15} | " f"{bill.food_amount:<20} | " f"{bill.vat_rate:<20} | " f"{bill.service_fee:<20} | " f"{bill.discount:<20} | " f"{bill.total_bill:<25} | " f"{bill.bill_type:<25}")


def main():
    retaurant = RestaurantBillManager()
    while True:
        print("""
        =============== MENU ===============
        1. Hiển thị danh sách hóa đơn bàn ăn
        2. Thêm hóa đơn mới
        3. Cập nhật hóa đơn
        4. Xóa hóa đơn
        5. Tìm kiếm hóa đơn
        6. Thoát
        ======================================""")

        choice = input("Nhập lựa chọn của bạn: ")
        match choice:
            case "1":
                retaurant.show_all()
            case "2":
                retaurant.add_bill()
            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
            case "6":
                print("Cảm ơn vì đã sử dụng chương trình! Chương trình kết thúc.")
                break
            case _:
                print("Lựa chọn của bạn không hợp lệ!")

if __name__ == "__main__":
    main()