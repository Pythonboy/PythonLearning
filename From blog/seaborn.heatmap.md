# seaborn.heatmap参数介绍

```
seaborn.heatmap(data, vmin=None, vmax=None, cmap=None, center=None, robust=False, annot=None, fmt='.2g', annotkws=None, 
linewidths=0, linecolor='white', cbar=True, cbarkws=None, cbar_ax=None, square=False, ax=None, xticklabels=True, 
yticklabels=True, mask=None, **kwargs)

```
- data：矩阵数据集，可以使numpy的数组（array），如果是pandas的dataframe，则df的index/column信息会分别对应到heatmap的columns和rows
- linewidths,热力图矩阵之间的间隔大小
- vmax,vmin, 图例中最大值和最小值的显示值，没有该参数时默认不显示

## cmap
- cmap：matplotlib的colormap名称或颜色对象；如果没有提供，默认为cubehelix map (数据集为连续数据集时) 或 RdBu_r (数据集为离散数据集时)
```
f, (ax1,ax2) = plt.subplots(figsize = (10, 8),nrows=2)
# cubehelix map颜色
cmap = sns.cubehelix_palette(start = 1.5, rot = 3, gamma=0.8, as_cmap = True)
sns.heatmap(pt, linewidths = 0.05, ax = ax1, vmax=15000, vmin=0, cmap=cmap)
ax1.set_title('cubehelix map')
ax1.set_xlabel('')
ax1.set_xticklabels([]) #设置x轴图例为空值
ax1.set_ylabel('kind')
# matplotlib colormap
sns.heatmap(pt, linewidths = 0.05, ax = ax2, vmax=15000, vmin=0, cmap='rainbow') 
# rainbow为 matplotlib 的colormap名称
ax2.set_title('matplotlib colormap')
ax2.set_xlabel('region')
ax2.set_ylabel('kind')
f.savefig('sns_heatmap_cmap.jpg', bbox_inches='tight')

```

## center
- center:将数据设置为图例中的均值数据，即图例中心的数据值；通过设置center值，可以调整生成的图像颜色的整体深浅；设置center数据时，
如果有数据溢出，则手动设置的vmax、vmin会自动改变
```
f, (ax1,ax2) = plt.subplots(figsize = (10, 8),nrows=2)
cmap = sns.cubehelix_palette(start = 1.5, rot = 3, gamma=0.8, as_cmap = True)
sns.heatmap(pt, linewidths = 0.05, ax = ax1, vmax=15000, vmin=0, cmap=cmap, center=None )
# center为None时，由于最小值为0，最大值为15000，相当于center值为vamx和vmin的均值，即7500
ax1.set_title('center=None')
ax1.set_xlabel('')
ax1.set_xticklabels([]) #设置x轴图例为空值
ax1.set_ylabel('kind')
sns.heatmap(pt, linewidths = 0.05, ax = ax2, vmax=15000, vmin=0, cmap=cmap, center=3000 ) 
# 由于均值为2000，当center设置为3000时，大部分数据会比7500大，所以center=3000时，生成的图片颜色要深
# 设置center数据时，如果有数据溢出，则手动设置的vmax或vmin会自动改变
ax2.set_title('center=3000')
ax2.set_xlabel('region')
ax2.set_ylabel('kind')
f.savefig('sns_heatmap_center.jpg', bbox_inches='tight')
```

## robust
```
f, (ax1,ax2) = plt.subplots(figsize = (10, 8),nrows=2)
cmap = sns.cubehelix_palette(start = 1.5, rot = 3, gamma=0.8, as_cmap = True)
sns.heatmap(pt, linewidths = 0.05, ax = ax1, cmap=cmap, center=None, robust=False )
# robust默认为False
ax1.set_title('robust=False')
ax1.set_xlabel('')
ax1.set_xticklabels([]) #设置x轴图例为空值
ax1.set_ylabel('kind')
sns.heatmap(pt, linewidths = 0.05, ax = ax2, cmap=cmap, center=None, robust=True ) 
# If True and vmin or vmax are absent, the colormap range is computed with robust quantiles instead of the extreme values.
ax2.set_title('robust=True')
ax2.set_xlabel('region')
ax2.set_ylabel('kind')
f.savefig('sns_heatmap_robust.jpg', bbox_inches='tight')

```

## mask
```
f, (ax1,ax2) = plt.subplots(figsize = (10, 8),nrows=2)
cmap = sns.cubehelix_palette(start = 1.5, rot = 3, gamma=0.8, as_cmap = True)
p1 = sns.heatmap(pt, linewidths = 0.05,ax=ax1, vmax=15000, vmin=0, cmap=cmap, center=None, robust=False, mask=None )
# robust默认为False
ax1.set_title('mask=None')
ax1.set_xlabel('')
ax1.set_xticklabels([]) #设置x轴图例为空值
ax1.set_ylabel('kind')
p2 = sns.heatmap(pt, linewidths = 0.05, ax=ax2, vmax=15000, vmin=0, cmap=cmap, center=None, robust=False, annot=False,mask=pt<10000 ) 
# mask: boolean array or DataFrame
ax2.set_title('mask: boolean DataFrame')
ax2.set_xlabel('region')
ax2.set_ylabel('kind')
f.savefig('sns_heatmap_mask.jpg', bbox_inches='tight')

```

## xticklabels, yticklabels
- xticklabels: 如果是True，则绘制dataframe的列名。如果是False，则不绘制列名。如果是列表，则绘制列表中的内容作为xticklabels。如果是整数n，则绘制列名，但每个n绘制一个label。 默认为True。
- yticklabels: 如果是True，则绘制dataframe的行名。如果是False，则不绘制行名。如果是列表，则绘制列表中的内容作为yticklabels。 如果是整数n，则绘制列名，但每个n绘制一个label。 默认为True。默认为True。
```
f, (ax1,ax2) = plt.subplots(figsize = (10, 8),nrows=2)
cmap = sns.cubehelix_palette(start = 1.5, rot = 3, gamma=0.8, as_cmap = True)
p1 = sns.heatmap(pt, linewidths = 0.05,ax=ax1, vmax=15000, vmin=0, cmap=cmap, center=None, robust=False, mask=None, xticklabels=False )
# robust默认为False
ax1.set_title('xticklabels=None')
ax1.set_xlabel('')
# ax1.set_xticklabels([]) #设置x轴图例为空值
ax1.set_ylabel('kind')
p2 = sns.heatmap(pt, linewidths = 0.05, ax=ax2, vmax=15000, vmin=0, cmap=cmap, center=None, robust=False, annot=False,mask=None,xticklabels=3, yticklabels=list(range(20)) ) 
# mask: boolean array or DataFrame
ax2.set_title('xticklabels=3, yticklabels is a list')
ax2.set_xlabel('region')
ax2.set_ylabel('kind')
f.savefig('sns_heatmap_xyticklabels.jpg', bbox_inches='tight')
```

## fmt
- fmt，格式设置
```
np.random.seed(0)
x = np.random.randn(10, 10)
f, (ax1, ax2) = plt.subplots(figsize=(8,8),nrows=2)
sns.heatmap(x, annot=True, ax=ax1)
sns.heatmap(x, annot=True, fmt='.1f', ax=ax2)
f.savefig('sns_heatmap_fmt.jpg')

```

## annot
- annotate的缩写，annot默认为False，当annot为True时，在heatmap中每个方格写入数据
- annot_kws，当annot为True时，可设置各个参数，包括大小，颜色，加粗，斜体字等
```
np.random.seed(0)
x = np.random.randn(10, 10)
f, (ax1, ax2) = plt.subplots(figsize=(8,8),nrows=2)
sns.heatmap(x, annot=True, ax=ax1)
sns.heatmap(x, annot=True, ax=ax2, annot_kws={'size':9,'weight':'bold', 'color':'blue'})
# Keyword arguments for ax.text when annot is True.
# http://stackoverflow.com/questions/35024475/seaborn-heatmap-key-words
f.savefig('sns_heatmap_annot.jpg')

```
