import matplotlib.pyplot as plt
import os
import seaborn as sns
import pandas as pd
import numpy as np

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


def plot_boxplot(x_data, y_data, xlabel, ylabel, savefilename, folder='pic', is_x_continuous=False, bins=5):
    """
    绘制一个箱线图并保存到文件。

    参数:
    x_data: list, numpy array, or Series, 箱线图的 x 数据
    y_data: list, numpy array, or Series, 箱线图的 y 数据
    xlabel: str, 箱线图的 x 轴标签
    ylabel: str, 箱线图的 y 轴标签
    savefilename: str, 保存文件的名称
    folder: str, 保存文件的文件夹，默认是 'pic'
    is_x_continuous: bool, 如果 x 数据是连续的，则为 True，默认是 False
    bins: int, 如果 x 数据是连续的，分箱的数量，默认是 10
    """
    # 检查保存文件夹是否存在，不存在则创建
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    # 如果 x 数据是连续的，则进行分箱处理
    if is_x_continuous:
        if isinstance(x_data, (list, np.ndarray)):
            x_data = pd.Series(x_data)
        x_data = pd.cut(x_data, bins=bins)
    
    # 创建子图
    plt.figure(figsize=(10, 6))
    
    # 绘制箱线图
    sns.boxplot(x=x_data, y=y_data)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    # 保存图片
    save_path = os.path.join(folder, savefilename)
    plt.savefig(save_path)
    plt.close()

    print(f'箱线图已保存到: {save_path}')
    

def plot_line_with_error_bars(x_data, y_data, yerr, xlabel, ylabel, savefilename, folder='pic'):
    """
    绘制一个带有误差条的折线图并保存到文件。

    参数:
    x_data: list, numpy array, or Series, 折线图的 x 数据
    y_data: list, numpy array, or Series, 折线图的 y 数据
    yerr: list, numpy array, or Series, y 数据的误差
    xlabel: str, 折线图的 x 轴标签
    ylabel: str, 折线图的 y 轴标签
    savefilename: str, 保存文件的名称
    folder: str, 保存文件的文件夹，默认是 'pic'
    """
    # 检查保存文件夹是否存在，不存在则创建
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    # 创建子图
    plt.figure(figsize=(10, 6))
    
    # 绘制带有误差条的折线图
    plt.errorbar(x_data, y_data, yerr=yerr, fmt='-o')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    # 保存图片
    save_path = os.path.join(folder, savefilename)
    plt.savefig(save_path)
    plt.close()

    print(f'带有误差条的折线图已保存到: {save_path}')