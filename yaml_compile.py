import yaml

# 定义要写入 YAML 文件的数据
data = {
    'version': "3.6",
    'services':{"task1":{"build":"../",
        "image":"test:0.2",
        "ports":["9999:8888"],
        "volumes":["/home/taig/niujh/workspace:/workspace"],
        "command":"python train.py"}}
}



print("start compile file")
# 将数据写入 YAML 文件
with open('docker-compose.yaml', 'w') as outfile:
    yaml.dump(data, outfile)

print("finish compile file")
