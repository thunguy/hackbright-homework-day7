"""Generate sales report showing total melons each salesperson sold."""
import sys


def get_report(file):
    sales_report = {}

    fname = open(file) 

    for line in fname:
        salesperson, total, melons_sold = line.rstrip().split('|')
        k = salesperson
        v = int(melons_sold)

        sales_report[k] = sales_report.get(k, v) + v

        # if k in sales_report:
        #     sales_report[k] += int(melons_sold)
        # else:
        #     sales_report[k] = int(melons_sold)

    return sales_report

# print(get_report(sys.argv[1]))

def print_sales_report(sales_report):

    for k, v in sales_report.items():
        print(f"{k} sold {v} melons.")

print(print_sales_report(get_report(sys.argv[1])))
