import os
import warnings
warnings.filterwarnings('ignore')
from collections import Counter
import numpy as np

def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        return files

def read(file):
    try:
        with open(file, 'r', encoding='utf-8') as f1:
            list1 = f1.read()
        with open(file, 'r', encoding='utf-8') as f1:
            list2 = f1.readlines()
        with open(file, 'r', encoding='utf-8') as f1:
            list3 = f1.readlines()
            list3 = [i.rstrip('\n') for i in list3]
            list3 = [i for i in list3 if i != '']
    except UnicodeError:
        with open(file, 'r', encoding='gbk') as f1:
            list1 = f1.read()
        with open(file, 'r', encoding='gbk') as f1:
            list2 = f1.readlines()
        with open(file, 'r', encoding='gbk') as f1:
            list3 = f1.readlines()
            list3 = [i.rstrip('\n') for i in list3]
            list3 = [i for i in list3 if i != '']
    # return list1, len(list2), len(list3)
    return list1, len(list2), len(list3), '  message' in list1

def protoc(filepath, savepath):
    try:
        os.system('protoc ' + filepath + ' --python_out=' + savepath)
    except Exception as err:
        print(filepath, str(err))

def count_syntax(content):
    if 'syntax = "proto2";' in content:
        return 2
    elif 'syntax = "proto3";' in content:
        return 3
    else:
        return 0

def wordcount(str):
    # 文章字符串前期处理
    strl_ist = str.replace('\n', '').lower().split(' ')
    count_dict = {}
    # 如果字典里有该单词则加1，否则添加入字典
    for str in strl_ist:
        if str in count_dict.keys():
            count_dict[str] = count_dict[str] + 1
        else:
            count_dict[str] = 1
    #按照词频从高到低排列
    count_list=sorted(count_dict.items(),key=lambda x:x[1],reverse=True)
    return count_list

def keywordCount(content):
    keyword_dict = {}
    keyword_list = ['double', 'float', 'int32', 'int64', 'unit32', 'unit64', 'sint32', 'sint64', 'fixed32', 'fixed64',
                    'sfixed32', 'sfixed64', 'bool', 'string', 'bytes', 'enum', 'message', 'repeated', 'import', 'extend',
                    'package', 'optional', 'required', 'singular', 'default', '//', 'oneof', 'map', 'reserved', 'allow_alias']
    for keyword in keyword_list:
        keyword_dict[keyword] = content.count(keyword)
    return keyword_dict


def scan_files(directory, prefix=None, postfix=None): # 扫描目录下所有文件 返回相对路径 https://www.jb51.net/article/52218.htm
    files_list = []

    for root, sub_dirs, files in os.walk(directory):
        for special_file in files:
            if postfix:
                if special_file.endswith(postfix):
                    files_list.append(os.path.join(root, special_file))
            elif prefix:
                if special_file.startswith(prefix):
                    files_list.append(os.path.join(root, special_file))
            else:
                files_list.append(os.path.join(root, special_file))

    return files_list

# matrix = [[0, 0, 0, 0, 12, 0, 0]]
def count_not_zero_in_matirx(matrix):
    # data = np.array([[0, 0, 0, 0, 12, 0, 0]])
    data = np.array(matrix)
    exist = (data > 0) * 1.0
    factor = np.ones(data.shape[1])
    res = np.dot(exist, factor)
    # print(int(res[0]))
    return int(res[0])

def draw():
    import matplotlib.pyplot as plt
    import numpy as np

    plt.figure(figsize=(10, 5))

    # 构建数据
    model = ['CNN', 'VGG16', 'ResNet50', 'InceptionV3', 'Xception', 'MultiNetV1', 'MultiNetV2', 'MultiNetV3',
             'MultiNetV4']
    acc = [0.6154, 0.7570, 0.9579, 0.9485, 0.9682, 0.9662, 0.9736, 0.9656, 0.9751]
    val_acc = [0.6305, 0.7957, 0.9697, 0.9774, 0.9878, 0.9852, 0.9852, 0.9866, 0.9862]
    loss = [0.6438, 0.5461, 0.1075, 0.1326, 0.0936, 0.0990, 0.0735, 0.0872, 0.0659]
    val_loss = [0.6290, 0.5026, 0.0803, 0.0750, 0.0514, 0.0521, 0.0438, 0.0419, 0.0380]
    kaggle = [0.62579, 0.50486, 0.09618, 0.08515, 0.06547, 0.06565, 0.06082, 0.05838, 0.05468]

    bar_width = 0.15
    plt.bar(x=np.arange(len(acc)) - 2 * bar_width, height=acc, label='acc', color='indianred', alpha=0.8,
            width=bar_width)
    plt.bar(x=np.arange(len(val_acc)) - bar_width, height=val_acc, label='val_acc', color='orange', alpha=0.8,
            width=bar_width)
    plt.bar(x=model, height=loss, label='loss', color='steelblue', alpha=0.8, width=bar_width)
    plt.bar(x=np.arange(len(val_loss)) + bar_width, height=val_loss, label='val_loss', color='gold', alpha=0.8,
            width=bar_width)
    plt.bar(x=np.arange(len(kaggle)) + 2 * bar_width, height=val_loss, label='kaggle', color='green', alpha=0.8,
            width=bar_width)

    # 在柱状图上显示具体数值, ha参数控制水平对齐方式, va控制垂直对齐方式
    for x, y in enumerate(acc):
        plt.text(x - 2 * bar_width, y + 0.02, '%s' % y, ha='center', va='bottom')
    for x, y in enumerate(val_acc):
        plt.text(x - bar_width, y + 0.05, '%s' % y, ha='center', va='bottom')
    for x, y in enumerate(loss):
        plt.text(x, y + 0.08, '%s' % y, ha='center', va='bottom')
    for x, y in enumerate(val_loss):
        plt.text(x + bar_width, y + 0.06, '%s' % y, ha='center', va='bottom')
    for x, y in enumerate(kaggle):
        plt.text(x + 2 * bar_width, y + 0.01, '%s' % y, ha='center', va='bottom')

    plt.ylim([0, 1.1])
    # 设置标题
    plt.title("Data comparison of each experiment")
    # 为两条坐标轴设置名称
    # plt.xlabel("年份")
    # plt.ylabel("销量")
    # 显示图例
    plt.legend()
    plt.show()


def draw2():
    import matplotlib.pyplot as plt
    import matplotlib.font_manager as fm  # 字体管理器

    # 准备字体
    # my_font = fm.FontProperties(fname="/usr/share/fonts/wqy-microhei/wqy-microhei.ttc")

    # 准备数据
    # # no_syntax: 1086  syntax_proto2: 414  syntax_proto3: 756

    data = [1086, 414, 756]

    # 准备标签
    labels = ['no syntax tag', 'syntax = "proto2";', 'syntax = "proto3";']

    # 将排列在第4位的语言(Python)分离出来
    # explode = [0, 0, 0, 0.3, 0, 0, 0, 0, 0, 0, 0]

    # 使用自定义颜色
    colors = ['orange', 'blue', 'green']

    # 将横、纵坐标轴标准化处理,保证饼图是一个正圆,否则为椭圆
    plt.axes(aspect='equal')

    # 控制X轴和Y轴的范围(用于控制饼图的圆心、半径)
    plt.xlim(0, 8)
    plt.ylim(0, 8)

    # 不显示边框
    plt.gca().spines['right'].set_color('none')
    plt.gca().spines['top'].set_color('none')
    plt.gca().spines['left'].set_color('none')
    plt.gca().spines['bottom'].set_color('none')

    # 绘制饼图
    plt.pie(x=data,  # 绘制数据
            labels=labels,  # 添加编程语言标签
            # explode=explode,  # 突出显示Python
            colors=colors,  # 设置自定义填充色
            autopct='%.3f%%',  # 设置百分比的格式,保留3位小数
            pctdistance=0.5,  # 设置百分比标签和圆心的距离
            labeldistance=1.3,  # 设置标签和圆心的距离
            startangle=180,  # 设置饼图的初始角度
            center=(4, 5),  # 设置饼图的圆心(相当于X轴和Y轴的范围)
            radius=2.8,  # 设置饼图的半径(相当于X轴和Y轴的范围)
            counterclock=False,  # 是否为逆时针方向,False表示顺时针方向
            wedgeprops={'linewidth': 1, 'edgecolor': 'green'},  # 设置饼图内外边界的属性值
            textprops={'fontsize': 12, 'color': 'black'},  # 设置文本标签的属性值
            frame=1)  # 是否显示饼图的圆圈,1为显示

    # 不显示X轴、Y轴的刻度值
    plt.xticks(())
    plt.yticks(())

    # 添加图形标题
    plt.title('Proportion of syntax tags')
    # 显示图形
    plt.show()


if __name__ == "__main__":
    # data = np.array([[0, 0, 0, 0, 12, 0, 0]])
    # exist = (data > 0) * 1.0
    # factor = np.ones(data.shape[1])
    # res = np.dot(exist, factor)
    # print(int(res[0]))
    # exit(0)
    # import csv
    # with open('proto.csv', 'r') as f:
    #     reader = csv.reader(f)
    #     set = len(set([str(row[0])[:str(row[0]).find('/raw')] for row in reader]))
    #
    #     print(set)
    #     for row in reader:
    #         print(str(row[0])[:str(row[0]).find('/raw')])
    #
    # exit(0)
    # x = {'a': 1, 'b': 2, 'c': 3}
    # y = {'a': 4, 'b': 5, 'c': -1}
    # l = ['a', 'b', 'c']
    # z = {}
    # for i in l:
    #     z[i] = max(x[i], y[i])
    # print(z)
    # exit(0)
    # draw2()
    # exit(0)
    base_dir = './proto2'
    if os.path.exists(base_dir + '/.DS_Store'):
        os.remove(base_dir + '/.DS_Store')

    protolist = file_name(base_dir)

    count_nest = 0

    count_syntax_proto2, count_syntax_proto3, count_no_syntax = 0, 0, 0
    count_sum_lines, count_effective_lines = 0, 0
    count_sum_lines_list, count_effective_lines_list = [], [] # 总的行数列表，有效行数列表

    count_keyword_dict = {}
    count_keyword_list = ['double', 'float', 'int32', 'int64', 'unit32', 'unit64', 'sint32', 'sint64', 'fixed32',
                          'fixed64', 'sfixed32', 'sfixed64', 'bool', 'string', 'bytes', 'enum', 'message', 'repeated',
                          'import', 'extend', 'package', 'optional', 'required', 'singular', 'default', '//', 'oneof',
                          'map', 'reserved', 'allow_alias']
    for keyword in count_keyword_list:
        count_keyword_dict[keyword] = []

    for num, file in enumerate(protolist):
        content, count_lines_1, count_lines_2, nest = read(base_dir + '/' + file)
        # if 'message' not in content:
        #     os.remove(base_dir + '/' + file)

        # if 'oneof' in content:
        #     print(file)

        # 统计文件中嵌套信息
        count_nest += nest

        # 统计文件中含有的syntax信息
        syntax = count_syntax(content)
        if syntax == 2:
            count_syntax_proto2 += 1
        elif syntax == 3:
            count_syntax_proto3 += 1
        elif syntax == 0:
            count_no_syntax += 1

        # 统计总的行数，有效行数
        # count_sum_lines += count_lines_1
        # count_effective_lines += count_lines_2
        count_sum_lines_list.append(count_lines_1)
        count_effective_lines_list.append(count_lines_2)
        count_sum_lines = sum(count_sum_lines_list)
        count_effective_lines = sum(count_effective_lines_list)

        # 统计关键词
        # count_keyword_dict_sum = dict(Counter(count_keyword_dict_sum) + Counter(keywordCount(content)))
        for keyword in count_keyword_list:
            count_keyword_dict[keyword].append(keywordCount(content)[keyword])

        # 统计能直接编译的文件数
        # filepath = base_dir + '/' + file
        # savepath = './protoc'
        # protoc(filepath, savepath)

    print('no_syntax:', count_no_syntax, '\nsyntax_proto2:', count_syntax_proto2, '\nsyntax_proto3:', count_syntax_proto3)
    # no_syntax: 1073  syntax_proto2: 411  syntax_proto3: 744
    # print(len(scan_files('./protoc')))  # 1256
    count_files = count_no_syntax + count_syntax_proto2 + count_syntax_proto3
    print('count_sum_lines:', count_sum_lines, '\ncount_effective_lines:', count_effective_lines)
    # count_sum_lines: 545499  count_effective_lines: 475780
    print('avg_sum_lines:', count_sum_lines / count_files, '\navg_effective_lines:', count_effective_lines / count_files)
    # avg_sum_lines: 244.83797127468583   avg_effective_lines: 213.54578096947935
    print("count_nest:", count_nest, '\ncount_nest_rate:', count_nest / count_files)
    # count_nest: 353  count_nest_rate: 0.15843806104129263

    count_keyword_dict_sum, count_keyword_dict_mean, count_keyword_dict_min, count_keyword_dict_max, \
    count_keyword_dict_var, count_keyword_dict_files, count_keyword_dict_rate = {}, {}, {}, {}, {}, {}, {}
    for keyword in count_keyword_list:
        count_keyword_dict_sum[keyword] = np.sum(count_keyword_dict[keyword])
        count_keyword_dict_mean[keyword] = np.mean(count_keyword_dict[keyword])
        count_keyword_dict_min[keyword] = np.min(count_keyword_dict[keyword])
        count_keyword_dict_max[keyword] = np.max(count_keyword_dict[keyword])
        count_keyword_dict_var[keyword] = np.var(count_keyword_dict[keyword])
        count_keyword_dict_files[keyword] = count_not_zero_in_matirx([count_keyword_dict[keyword]])
        count_keyword_dict_rate[keyword] = count_keyword_dict_files[keyword] / count_files

    print('count_keyword_dict_sum:', count_keyword_dict_sum)
    print('count_keyword_dict_mean:', count_keyword_dict_mean)
    print('count_keyword_dict_min:', count_keyword_dict_min)
    print('count_keyword_dict_max:', count_keyword_dict_max)
    print('count_keyword_dict_var:', count_keyword_dict_var)
    print('count_keyword_dict_files:', count_keyword_dict_files)
    print('count_keyword_dict_rate:', count_keyword_dict_rate)


    count_keyword_dict_summary = {}
    for keyword in count_keyword_list:
        count_keyword_dict_summary[keyword] = []
        count_keyword_dict_summary[keyword].append(count_keyword_dict_sum[keyword])
        count_keyword_dict_summary[keyword].append(count_keyword_dict_mean[keyword])
        count_keyword_dict_summary[keyword].append(count_keyword_dict_min[keyword])
        count_keyword_dict_summary[keyword].append(count_keyword_dict_max[keyword])
        count_keyword_dict_summary[keyword].append(count_keyword_dict_var[keyword])
        count_keyword_dict_summary[keyword].append(count_keyword_dict_files[keyword])
        count_keyword_dict_summary[keyword].append(count_keyword_dict_rate[keyword])

    print(count_keyword_dict_summary)



