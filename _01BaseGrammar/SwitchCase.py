# Switch case
score = "A"
match score:
    case 'A':
        print("A")
    case 'B':
        print("B")
    case 'C':
        print("C")
    case _:  # 匹配任意值
        print("alphabet")

# runtime = 0
# while runtime < 3:
#     scoreNum = int(input("请输入成绩："))
#     match scoreNum:
#         case 99 | 100:
#             print(f"你的分数是：{99}或{100}，简直完美")
#         case x if 90 <= x < 100:
#             print("优秀")
#         case x if 80 <= x < 89:
#             print("良好")
#         case x if 60 <= x < 79:
#             print("中等")
#         case x if x < 60:
#             print("不及格")
#         case _:  # 匹配任意值
#             print("请输入0~100的整数")
#     runtime += 1

# args = ['gcc', 'hello.c', 'world.c']
args = ['clean']
# args = ['gcc']
match args:
    # 如果仅出现gcc，报错:
    case ['gcc']:
        print('gcc: missing source file(s).')
    # 出现gcc，且至少指定了一个文件:
    case ['gcc', file1, *files]:
        print('gcc compile: ' + file1 + ', ' + ', '.join(files))
    # 仅出现clean:
    case ['clean']:
        print('clean')
    case _:
        print('invalid command.')
