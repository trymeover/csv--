import argparse

from utlis import csv_count

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="csv数据分析小工具")
    parser.add_argument("--flie", required=True, help="csv文件路径")
    args = parser.parse_args()
    # 这里写你的csv真实路径，前面加r防止转义
    result = csv_count(args.file)

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

    print("-" * 40)

    # ✅ 新增：打印每行空值数量
    print("每行空值统计：")
    for i, cnt in enumerate(result["row_null_counts"], start=1):
        print(f"  第 {i} 行：{cnt} 个空值")
