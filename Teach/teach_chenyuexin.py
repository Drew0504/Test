import random


std_dict = [0, "石头", "剪刀", "布"]
std_list = [1,2,3]
for i in range(10):
    print("现在游戏开始，请输入(1)石头、（2）剪刀，(3)布：")
    try:
        input_key = int(input())
        if input_key not in std_list:
            print ("无效的输入，请对号入座，输入一个对应的数字：")
            print("开始下一局：\n\n")
            continue

        sys_key = random.randint(1,3)
        print("本局系统出的是%s，" % std_dict[sys_key])
        if sys_key == 1:
            # 1是石头
            if input_key == 1:
                print("您出的是%s，\n 没有分出胜负，请继续。" % std_dict[1])
            if input_key == 2:
                print("您出的是%s，\n 很遗憾。您输了。" % std_dict[2])
            if input_key == 3:
                print("您出的是%s，\n恭喜您！您赢了。" % std_dict[3])

        if sys_key == 2:
            # 剪刀
            if input_key == 2:
                print("您出的是%s，\n 没有分出胜负，请继续。" % std_dict[2])
            if input_key == 3:
                print("您出的是%s，\n 很遗憾。您输了。" % std_dict[3])
            if input_key == 1:
                print("您出的是%s，\n恭喜您！您赢了。" % std_dict[1])

        if sys_key == 3:
            # 布
            if input_key == 3:
                print("您出的是%s，\n 没有分出胜负，请继续。" % std_dict[3])
            if input_key == 2:
                print("您出的是%s，\n 很遗憾。您输了。" % std_dict[2])
            if input_key == 1:
                print("您出的是%s，\n恭喜您！您赢了。" % std_dict[1])
        print("开始下一局：\n\n")

    except ValueError as E:
        print("无效的输入，请对号入座，输入一个对应的数字：")
