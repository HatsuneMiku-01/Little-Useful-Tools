print("你好，欢迎使用GPA计算器。本GPA标准基于北大“GPA4.0”版本")
print("操作指南：请根据提示输入您课程的成绩以及相应的分值，输入完毕后按Q健结束")

# 表示输入第几门课的成绩与分值
i = 1
chengji = 0
fensu = 0
total_chengji = 0
total_fensu = 0
total_score = 0
chengji = float(input(f"请输入您第{i}门课的成绩（按Q结束）："))
# 用循环来输入各科成绩与分值
while chengji != "Q":
    fensu = float(input(f"请输入您第{i}门课程的分值：（按Q结束)"))
    total_score += float(chengji)*fensu
    total_fensu += fensu
    weight_average_score = total_score/total_fensu
    i += 1
    chengji = input(f"请输入您第{i}门课程的成绩：（按Q结束)")

print("您的加权平均成绩为：" + str(weight_average_score))
# 根据加权平均分数，判断您的GPA情况
if weight_average_score == 0:
    print("您的绩点为0")
else:
    if weight_average_score < 60:
        print("您的GPA为0")
    elif 60 <= weight_average_score <= 63:
        print("您的GPA为1.0")
    elif 64 <= weight_average_score <= 67:
        print("您的GPA为1.5")
    elif 68 <= weight_average_score <= 71:
        print("您的GPA为2.0")
    elif 72 <= weight_average_score <= 74:
        print("您的GPA为2.3")
    elif 75 <= weight_average_score <= 77:
        print("您的GPA为2.7")
    elif 78 <= weight_average_score <= 81:
        print("您的GPA为3.0")
    elif 82 <= weight_average_score <= 84:
        print("您的GPA为3.3")
    elif 85 <= weight_average_score <= 89:
        print("您的GPA为3.7")
    elif 90 <= weight_average_score <= 100:
        print("您的GPA为4.0")