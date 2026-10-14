from utlis import csv_count
if __name__=="__main__":

        # 这里写你的csv真实路径，前面加r防止转义
    result = csv_count(r"D:\csv_tool\stu.csv")

    # 打印总行数
    print(f"数据总行数：{result['total_rows']}")
    print("-" * 40)

    # 打印每列空值数量
    print("每列空值统计：")
    for col_name, count in result["null_count"].items():
        print(f"  {col_name}：{count} 个空值")

    print("-" * 40)

    # 打印每列均值
    print("每列均值统计：")
    for col_name, avg in result["mean"].items():
        if avg is not None:
            print(f"  {col_name}：{avg:.2f}")
        else:
            print(f"  {col_name}：无法计算均值（无数字）")

