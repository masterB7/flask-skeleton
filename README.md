# Flask restful 风格项目骨架
# 开发指南

## step 0 初始化项目
项目根目录下
安装依赖
```shell
 pip install -r requirements.txt
```
运行
```shell
 python ./src/api.py
```
or 

使用 docker 
```shell
docker build -t pythonserver:v1.0 .
docker run  -p 8080:8080  -d  pythonserver:v1.0 
```
验证
```shell
 curl http://localhost:8080/ping
```
## step 1 逻辑编写
src 目录下新建 xxx.py 项目
具体 handler 的定义可以参照 todo.py 
一个 class 代表一套 restful 操作资源，里面的 get put delete 即 http方法
定义好后在  api.py 中进行 `import 文件名` 的操作
然后就可以在 add router 部分即可进行路由的注册
`api.add_resource` 第一个参数即 class ，第二参数是路由 

## step 2
导出依赖
```shell
pipreqs ./ --encoding=utf8 --force
```