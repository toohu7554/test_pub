# numpy の利用
import numpy as np

x = np.array(5.2)
print(f'スカラーの値: {x}  成分のデータ型: {x.dtype}')
print(f'データ型: {type(x)}  次元: {x.ndim}')
print(f'スカラーの形状: {x.shape}  {type(x.shape)}')
print('-------------------------------------------------')

vec = [10.0, 20, 30, 40, 50, 60, 70]
print(f'リストの値: {vec}')
print(f'ベクトルのデータ型: {type(vec)}')
print('-------------------------------------------------')

x = np.array(vec)
print(f'ベクトルの値: {x}  成分のデータ型: {x.dtype}')
print(f'データ型: {type(x)}  次元: {x.ndim}')
print(f'ベクトルの形状: {x.shape}  {type(x.shape)}')
print('-------------------------------------------------')

x = np.array([[1, 2, 3, 4, 5.], [6, 7, 8, 9, 10]])
print(f'行列の値:\n{x}\n成分のデータ型: {x.dtype}')
print(f'データ型: {type(x)}  次元: {x.ndim}')
print(f'行列の形状: {x.shape}  {type(x.shape)}')
print('-------------------------------------------------')

