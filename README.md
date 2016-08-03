# PerlerBeads
拼豆图纸转换工具

## 安装
```bash
pip install git+git://github.com/Everley1993/PerlerBeads.git
```

## 使用
```bash
perler_beads -s SRC -d DST -sw SW -dw DW
  -s SRC      源图片路径
  -d DST      目标图片路径
  -sw SW      在源图片中，从SW*SW的像素块采样，作为拼豆图纸中的一颗豆
  -dw DW      在目标图片中，将每颗豆显示为SW*SW的像素块
```

## 示例
```bash
perler_beads -s images/src.png -d /images.png -sw 10 -dw 10
```

![src.png](https://github.com/Everley1993/PerlerBeads/blob/master/images/src.png?raw=true)

![dst.png](https://github.com/Everley1993/PerlerBeads/blob/master/images/dst.png?raw=true)
