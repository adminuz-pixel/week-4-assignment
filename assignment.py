def classify(value):
    if value <208:
        return "Below range"
    elif 208<=value<= 212:
        return "In range"
    else:
        return "Above range"
def calculate_average(total, count):
    average_snapshot= total/count
    average_result =average_snapshot
    return average_result
def main():
    num_sheets = int(input("Enter the number of paper sheets: "))
    total_width =0
    below_count =0
    in_range_count = 0
    above_count =0
    for i in range(num_sheets):
        width= int(input("Enter the paper sheet width: "))
        classification =classify(width)
        print(classification)
        total_width +=width
        if classification=="Below range":
            below_count+= 1
        elif classification== "In range":
            in_range_count+=1
        elif classification =="Above range":
            above_count+=1
    average_width =calculate_average(total_width, num_sheets)
    print(f"Total width: {total_width} mm")
    print(f"Average width: {average_width} mm")
    print(f"Below range: {below_count}")
    print(f"In range: {in_range_count}")
    print(f"Above range: {above_count}")
main()
