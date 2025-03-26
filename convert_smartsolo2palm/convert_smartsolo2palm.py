#  
# 
# 
# Yuan Yao@YNU 2025-03-26 

import os
import shutil
from tqdm import tqdm
from datetime import datetime

# 设置源目录和目标目录
source_dir = r'H:\2024MangShi'
target_dir = r'G:\2024MangShi_palm'

# 将年、月、日转换为儒略日
def get_julian_day(year, month, day):
    date = datetime(year, month, day)
    # 计算儒略日
    start_of_year = datetime(year, 1, 1)
    delta = date - start_of_year
    julian_day = delta.days + 1  # 儒略日是从1月1日开始的，所以加1
    return julian_day

# 遍历源目录中的所有文件
def rename_and_copy_files(source_dir, target_dir):
    # 获取所有.sac文件
    files = [f for f in os.listdir(source_dir) if f.endswith('.sac')]

    # 处理每个文件
    for file_name in tqdm(files, desc="Copying files", unit="file"):
        # 解析原文件名
        parts = file_name.split('.')
        station_name = parts[0]  # 台站名称
        year = int(parts[2])  # 年
        month = int(parts[3])  # 月
        day = int(parts[4])  # 日
        channel = parts[9]  # 通道名称（第10部分）

        # 将年、月、日转换为儒略日
        julian_day = get_julian_day(year, month, day)

        # 儒略日补充为3位（例如0001，0010等）
        julian_day_str = f"{julian_day:03d}"

        # 通道名称加上"SH"（如E -> SHE）
        channel_with_sh = f"SH{channel}"

        # 新文件名的格式：KMS.station_name.year.julian_day.channelSH.SAC
        new_file_name = f"KMS.{station_name}.{year}.{julian_day_str}.{channel_with_sh}.SAC"

        # 创建目标路径：年 -> 年月日 -> 文件
        year_dir = os.path.join(target_dir, str(year))
        date_dir = os.path.join(year_dir, f"{year}{parts[3]}{parts[4]}")  # 年月日目录

        # 如果目标年目录不存在，创建它
        if not os.path.exists(year_dir):
            os.makedirs(year_dir)

        # 如果目标年月日目录不存在，创建它
        if not os.path.exists(date_dir):
            os.makedirs(date_dir)

        # 获取源文件的完整路径和目标文件的完整路径
        source_file = os.path.join(source_dir, file_name)
        target_file = os.path.join(date_dir, new_file_name)

        # 复制文件
        shutil.copy2(source_file, target_file)

# 调用函数
rename_and_copy_files(source_dir, target_dir)