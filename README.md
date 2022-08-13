# JK_valuation
## 安装方法

命令行输入`pip install -i https://test.pypi.org/simple/ jk-valuation`

## 函数
`extract_valuation(folder_path, subjects)`

## 使用方法

`from jk_valuation import extract_valuations`
`extract_valuations(文件路径:str, 科目:['科目','科目2',...])`

*生成的output.xlsx存放于input文件夹路径*

## 使用案例

`from jk_valuation import extract_valuations`
`extract_valuations('/Users/andy/Desktop/work/ubiquant/valuation/input', ['1002'])`
