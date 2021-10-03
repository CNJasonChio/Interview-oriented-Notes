import sys
import os
import time
import re

headline_levels = ['#', '##', '###', '####', '#####', '######']

"""统计各级标题出现的次数，从三级标题开始"""
"""定义成 8 个标题等级，为的是减少判断，简化代码"""
headlines_count = [0] * 8
MAX_LEVEL = 8

"""收集三级标题，以便生成目录"""
third_headline_in_file = []

"""判断该标题是否已完成"""
is_headline_check = {}

"""生成标题编号"""


def gen_headline_num(level):
    num = ' '
    for i in range(3, level + 1):
        num += str(headlines_count[i]) + '.'
    return num


"""处理格式为：格式：### [编号 标题](链接) 的标题"""


def handle_headline_with_num_in_hyper(headline_items):
    global headlines_count
    global MAX_LEVEL
    global third_headline_in_file

    # 该行的标题等级
    level = len(headline_items[0])
    num = gen_headline_num(level)

    headline = headline_items[0] + num + ' ['
    # 将标题中其他内容填充回去，并加上被去掉的空格
    headline += headline_items[2]
    if len(headline_items[2:]) != 1:
        for item in headline_items[3:]:
            headline += ' ' + item

    # 记录三级标题，以便生成目录
    if len(headline_items[0]) == 3:
        catalog = ' ['
        catalog += headline_items[2]
        if len(headline_items[2:]) != 1:
            for item in headline_items[3:]:
                catalog += ' ' + item
        catalog = catalog.lstrip().replace('\n', '').replace('\r', '')
        third_headline_in_file.append(catalog)

    return headline


"""处理格式为：格式：### [标题](链接) 的标题"""


def handle_headline_without_num_in_hyper(headline_items):
    global headlines_count
    global MAX_LEVEL
    global third_headline_in_file

    # 该行的标题等级
    level = len(headline_items[0])
    num = gen_headline_num(level)
    headline = headline_items[0] + num
    # 将标题中其他内容填充回去，并加上被去掉的空格
    for item in headline_items[1:]:
        headline += ' ' + item

    # 记录三级标题，以便生成目录
    if len(headline_items[0]) == 3:
        catalog = ''
        for item in headline_items[1:]:
            catalog += ' ' + item
        catalog = catalog.lstrip().replace('\n', '').replace('\r', '')
        third_headline_in_file.append(catalog)
    return headline


"""处理格式为：格式：### 编号 标题 或 ### 编号 [标题](链接) 的标题"""


def handle_headline_with_num_no_hyper(headline_items):
    global headlines_count
    global MAX_LEVEL
    global third_headline_in_file

    # 该行的标题等级
    level = len(headline_items[0])
    num = gen_headline_num(level)

    headline = headline_items[0] + num
    for item in headline_items[2:]:
        headline += ' ' + item

    # 记录三级标题，以便生成目录
    if len(headline_items[0]) == 3:
        catalog = ''
        for item in headline_items[2:]:
            catalog += ' ' + item
        catalog = catalog.lstrip().replace('\n', '').replace('\r', '')

        third_headline_in_file.append(catalog)
    return headline


"""处理格式为格式：### 标题 的标题"""


def handle_headline_only(headline_items):
    global headlines_count
    global third_headline_in_file
    global MAX_LEVEL

    # 该行的标题等级
    level = len(headline_items[0])
    num = gen_headline_num(level)
    headline = headline_items[0] + num

    # 将标题中其他内容填充回去，并加上被去掉的空格
    for item in headline_items[1:]:
        headline += ' ' + item

    # 记录三级标题，以便生成目录
    if len(headline_items[0]) == 3:
        catalog = ''
        for item in headline_items[1:]:
            catalog += ' ' + item
        catalog = catalog.lstrip().replace('\n', '').replace('\r', '')

        third_headline_in_file.append(catalog)

    return headline


"""给标题添加编号"""


def add_headline_number(headline, headline_items):
    global headlines_count
    global MAX_LEVEL
    # 该行的标题等级
    level = len(headline_items[0])
    # 该级标题出现次数+1，重置更低级标题的统计信息
    headlines_count[level] += 1
    # 定义成 8 个标题等级，为的是减少判断，简化代码
    for i in range(level + 1, MAX_LEVEL):
        headlines_count[i] = 0

    # 从三级标题开始计数
    if level <= 2:
        return headline

    # 标题中有超链接
    if headline_items[1].startswith('['):
        if re.match("\[[0-9\.]+", headline_items[1]):
            # 格式：### [编号 标题](链接)
            headline = handle_headline_with_num_in_hyper(headline_items)
        else:
            headline = handle_headline_without_num_in_hyper(headline_items)
    else:
        # 标题中没有超链接
        if re.match("^[0-9\.]+", headline_items[1]):
            # 格式：### 编号 标题 或 ### 编号 [标题](链接)
            headline = handle_headline_with_num_no_hyper(headline_items)
        else:
            # 格式：### 标题
            headline = handle_headline_only(headline_items)

    return headline


def handle_toc_lines(line):
    global is_headline_check
    global headline_levels

    # 跳过空行
    if line.strip() == '':
        return

    result = re.match("(?P<check>\-\s\[[\sx]\]\s)(?P<num>[0-9]+\.)\s(?P<content>.*)", line)
    if result is not None:
        content = result.group('content')
        check = result.group('check')
        if check == '- [ ] ':
            is_headline_check[content] = False
        else:
            is_headline_check[content] = True


"""过滤原来的目录"""


def remove_original_catalog(lines_in_file):
    content_start = 1
    is_catalog_headline_showed = False

    for i in range(len(lines_in_file)):
        headline_items = lines_in_file[i].lstrip().split(' ')
        # 检查是否为二级标题且不是正文的二级标题
        if (headline_items[0] in headline_levels) and (
                len(headline_items[0]) == 2 and is_catalog_headline_showed is False):
            is_catalog_headline_showed = True
        elif (headline_items[0] in headline_levels) and (
                len(headline_items[0]) == 2 and is_catalog_headline_showed is True):
            content_start = i
            break
        # 在目录和正文两个二级标题中间，应该是目录的正文
        else:
            handle_toc_lines(lines_in_file[i])

    file_headline = lines_in_file[0]
    lines_in_file = lines_in_file[content_start:]
    lines_in_file.insert(0, file_headline)

    return lines_in_file


"""给传入内容添加编号"""


def handle_lines_in_file(lines_in_file):
    for i in range(len(lines_in_file)):
        # 逐行处理文件内容，去掉每行最左侧多余的空格后，分割出标题等级
        headline_items = lines_in_file[i].lstrip().split(' ')
        # 检查是否为标题行
        if headline_items[0] in headline_levels:
            lines_in_file[i] = add_headline_number(lines_in_file[i], headline_items)

    # 过滤掉原来的目录
    lines_in_file = remove_original_catalog(lines_in_file)

    return lines_in_file


"""生成文件"""


def gen_file_with_num_and_catalog(filename, lines_in_file_handled):
    global is_headline_check
    global third_headline_in_file

    # 根据原文件名生成标题添加了序号的文件的文件名
    new_file_with_headline_num = os.getcwd() + '\\' + filename[::-1].split('.', 1)[1][::-1] + '.md'

    with open(new_file_with_headline_num, 'w+', encoding='utf-8') as file:
        # 写文件标题
        file.write(lines_in_file_handled[0])

        headline = "## 目录 or TODO" + '\n'
        file.write(headline)

        # 写目录
        for i in range(len(third_headline_in_file)):
            content = third_headline_in_file[i]
            if (content in is_headline_check) and (is_headline_check[content] is True):
                toc_item = '- [x] ' + str(i + 1) + '.' + content + '\n'
            else:
                toc_item = '- [ ] ' + str(i + 1) + '.' + content + '\n'
            file.write(toc_item)

        # 写正文
        for i in range(1, len(lines_in_file_handled)):
            file.write(lines_in_file_handled[i])
        print('文件已生成')


def clean_data():
    global headlines_count
    global third_headline_in_file
    global is_headline_check

    headlines_count = [0] * 8
    third_headline_in_file = []
    is_headline_check = {}


"""为标题添加序列号，为文件添加目录"""


def add_headline_num_and_catalog(file, filename):
    lines_in_file = []
    lines_in_file_handled = []

    # 将文件内容读入 lines_in_file
    lines_in_file = file.readlines()
    file.close()

    # 提取所有的标题行
    lines_in_file_handled = handle_lines_in_file(lines_in_file)

    # 将处理过的的内容填充到文件中
    gen_file_with_num_and_catalog(filename, lines_in_file_handled)

    # 记录的相关信息的结构
    clean_data()


"""处理指定 md 文件"""


def start_process(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            add_headline_num_and_catalog(f, file_name)
    else:
        msg = "未找到文件"
        print(msg)


if __name__ == "__main__":
    file_name = ''

    # 传入了要处理的文件名
    if len(sys.argv) >= 2:
        file_name = sys.argv[1]
        start_process(file_name)

    # 未传入文件名,则扫描本地目录下的 md 文件
    path = os.getcwd()
    file_and_dir = os.listdir(path)
    md_files = []
    for item in file_and_dir:
        if item.split('.')[-1].lower() in ['md', 'mdown', 'markdown'] and os.path.isfile(item):
            md_files.append(item)

    if len(md_files) == 0:
        print('该目录下无Markdown文件，即将退出...')
        time.sleep(2)
        os._exit(0)

    print('当前目录下的Markdown文件：')
    num = 1

    for file in md_files:
        print('序号：' + str(num) + ' 文件名：' + file)
        num += 1

    num = input('请输入文件序号, 输入 0 表示处理所有文件\n')

    if int(num) == 0:
        # 逐个处理 md 文件
        for file in md_files:
            start_process(file)
    else:
        file_name = md_files[int(num) - 1]
        start_process(file_name)
