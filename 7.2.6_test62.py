import seaborn as sns
import matplotlib.pyplot as plt
#tips = sns.load_dataset("tips")               #导入数据集
#若"tips"数据集存储在本地电脑D盘下的SeabornData文件夹中，则上行代码修改为：
tipsInfo=sns.load_dataset(name="tips",data_home="D:\SeabornData",cache=True)
sns.scatterplot(data=tipsInfo,x="total_bill",y="tip",hue="size",size="size",sizes=(5, 100))
#通过参数hue将分组依据设置为size，散点图中点的大小范围为5~100
plt.show()
