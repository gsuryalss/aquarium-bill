import time


class CtAquarium:

    def __init__(self, emp_name, count_no, entries_val):
        self.store_name = "CT AQUARIUM"
        self.assoc_name = emp_name
        self.phone_no = "8608758562"
        self.curr_time = time.strftime("REG %m-%d-%Y %H:%M")
        self.counter_no = count_no
        self.entries_val = entries_val

        return

    def head_label(self):
        print(self.store_name)
        print("TEL:", self.phone_no)
        print("COME AGAIN\n")
        return

    def date_label(self):
        print(self.curr_time)
        print("Associate:", self.assoc_name, " ", "Counter:", self.counter_no)
        return

    def bill_section(self):
        # print("Quantity\tProduct\tAmount")
        # print(self.entries_val)
        for key, values in self.entries_val.items():
            # print(key, "\t", values['quantity'], "\t", values['price'], "\t", values['amount'])
            print(values['quantity'], "\t", key, "\t\t", '${:,.2f}'.format(values['amount']))
        return

    def foot_label(self):
        print("\n")
        print(self.store_name)
        return


assoc_name = input("Enter the Associate Name:\n>>")
counter_no = input("Enter the Counter No:\n>>")

prod_details = dict()
prod_list = []
print("Please enter the product details!Press \"Enter\" to continue and \"Q\" to exit the data entry")

while True:
    prod_name = input("Enter the product name:\n>>")
    prod_list.append(prod_name)

    prod_count = int(input("Enter the Quantity:\n>>"))
    prod_details.setdefault(prod_name, {}).setdefault('quantity',prod_count)

    prod_price = float(input("Enter the Amount:\n>>"))
    prod_details.setdefault(prod_name, {}).setdefault('price',prod_price)

    calc_amount = round((prod_count * prod_price), 2)

    prod_details.setdefault(prod_name, {}).setdefault('amount',calc_amount)

    quit_key = input(">>")

    if quit_key.lower() == "q":
        break


CTA = CtAquarium(assoc_name, counter_no, prod_details)

# for key, values in prod_details.items():
#     print(key)
#     print(values)

CTA.head_label()
CTA.date_label()
CTA.bill_section()
CTA.foot_label()
