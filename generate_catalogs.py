# coding=utf-8
import os


# 生成目录
def generate_catalogs(path, readme_path, before_text, after_text):
    file_name_list = []
    file_list = os.listdir(path)
    for file_name in file_list:
        # GBK 解码，防止中文乱码问题
        file_name_gbk = file_name
        file_path = os.path.join(path, file_name)
        if os.path.isfile(file_path) and str(file_path).endswith('.md'):
            file_name_list.append(file_name_gbk)
        else:
            print(file_name_gbk + ' is dir or non-md file, ignored.')
    write_to_readme(file_name_list, readme_path, before_text, after_text)


# 写入Readme
def write_to_readme(file_name_list, readme_path, before_text, after_text):
    with open(readme_path, 'w+') as f:
        f.write(before_text.encode('gbk').decode('gbk'))
        for file_name in file_name_list:
            link = '- [%s](./docs/%s)\n' % (file_name[:-3], file_name)
            f.write(link.encode('gbk').decode('gbk'))
        f.write(after_text.encode('gbk').decode('gbk'))
    f.close()

if __name__ == '__main__':
    path = './docs'
    readme_path = './README.md'
    before_text = """
# Edwin Xu Notes

## Contents
"""
    after_text = """
## Personal Info
- name: Edwin Xu
- [GitHub](https://github.com/Edwin-Xu)
- Email: edwinxu83@gmail.com, 1603837506@qq.com
- [Pages](https://edwin-xu.github.io/)
    """
    generate_catalogs(path, readme_path, before_text, after_text)
