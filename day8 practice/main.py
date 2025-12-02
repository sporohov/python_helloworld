from data_provider import get_order_data
from processing import filter_and_calculate_lines
from processing import calculate_order_totals
from reporting import print_order_report

if __name__ == "__main__":
    
    order_data = get_order_data()
    
    filters_order_data = filter_and_calculate_lines(order_data)

    totals = calculate_order_totals(filters_order_data)

    print_order_report(filters_order_data, totals)
    


