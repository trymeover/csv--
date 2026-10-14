import csv
def csv_count(filepath):
    with open(filepath, "r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        headers = next(reader)

        total_row = 0
        null_count = {}
        num_count = {}
        num_num = {}
        for col in headers:
            null_count[col] = 0
            num_count[col] = 0
            num_num[col] = 0
        for row in reader:
            total_row += 1
            for idx in range(len(headers)):
                col_name = headers[idx]
                cell = row[idx].strip()
                if cell == "":
                    null_count[col_name] += 1
                else:
                    try:
                        num = float(cell)
                        num_count[col_name] += num
                        num_num[col_name] += 1
                    except ValueError:
                        pass
        avg_dict={}
        for col in headers:
            if num_num[col] > 0:
                avg_dict[col] = num_count[col] / num_num[col]
            else:
                avg_dict[col] = None
    return {
        "total_rows": total_row,
        "null_count": null_count,
        "mean": avg_dict
    }
