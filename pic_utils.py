import matplotlib.pyplot as plt
import os


def plot_histogram(data, bins, title, xlabel, savefilename, folder='pic'):
    # 检查保存文件夹是否存在，不存在则创建
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    # 创建直方图
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=bins, edgecolor='black', alpha=0.7)
    
    # 设置标题和标签
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel('Frequency')
    
    # 保存图片
    save_path = os.path.join(folder, savefilename)
    plt.savefig(save_path)
    plt.close()

    print(f'直方图已保存到: {save_path}')
    

def plot_scatter(x_data, y_data, title, xlabel, ylabel, savefilename, folder='pic'):
    # 检查保存文件夹是否存在，不存在则创建
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    # 创建散点图
    plt.figure(figsize=(10, 6))
    plt.scatter(x_data, y_data, c='blue', alpha=0.7, edgecolor='black')
    
    # 设置标题和标签
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    # 保存图片
    save_path = os.path.join(folder, savefilename)
    plt.savefig(save_path)
    plt.close()

    print(f'散点图已保存到: {save_path}')

