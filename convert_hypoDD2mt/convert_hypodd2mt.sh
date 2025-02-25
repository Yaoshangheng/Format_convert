#!/bin/bash

input_file="hypoDD.reloc"
output_file="earthquakes.txt"

if [[ ! -f "$input_file" ]]; then
  echo "输入文件 $input_file 不存在!"
  exit 1
fi

> "$output_file"

while IFS= read -r line; do
  # 提取字段并格式化数值为两位数
  longitude=$(echo "$line" | awk '{print $3}')
  latitude=$(echo "$line" | awk '{print $2}')
  depth=$(echo "$line" | awk '{print $4}')
  
  year=$(echo "$line" | awk '{print $11}')
  month=$(echo "$line" | awk '{printf "%02d", $12}')      # 月格式化
  day=$(echo "$line" | awk '{printf "%02d", $13}')        # 日格式化
  hour=$(echo "$line" | awk '{printf "%02d", $14}')       # 时格式化
  minute=$(echo "$line" | awk '{printf "%02d", $15}')     # 分格式化
  second=$(echo "$line" | awk '{printf "%02d", $16}')     # 秒格式化
  
  magnitude=$(echo "$line" | awk '{print $17}')

  # 组合日期时间字符串
  datetime="${year}-${month}-${day}T${hour}:${minute}:${second}"

  # 写入文件
  echo "$datetime $longitude $latitude $depth $magnitude" >> "$output_file"
done < "$input_file"

echo "处理完成，结果已保存到 $output_file"