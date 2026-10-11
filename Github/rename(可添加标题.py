import os

# --- 配置区域 ---
folder_path = r"G:\大一下\Linux操作系统_服务管理"
class_id = "网络2502"
student_name = "alex"

def run_rename():
    if not os.path.exists(folder_path):
        print(f"❌ 错误：找不到文件夹 '{folder_path}'，请检查路径是否填对！")
        return

    files = sorted(os.listdir(folder_path))
    counter = 1
    print(f"准备处理 {len(files)} 个文件...\n")

    for filename in files:
        old_path = os.path.join(folder_path, filename)

        if os.path.isdir(old_path):
            continue

        file_ext = os.path.splitext(filename)[1]

        # 交互环节：询问新标题
        prompt = f"[{counter}/{len(files)}] 当前文件: {filename}\n请输入新标题（直接回车跳过）: "
        new_title = input(prompt).strip()

        # 如果用户直接回车，跳过该文件
        if not new_title:
            print("  ⚠️ 已跳过\n")
            continue

        # 生成新文件名
        new_name = f"{class_id}_{student_name}_作业{counter}_{new_title}{file_ext}"
        new_path = os.path.join(folder_path, new_name)

        try:
            os.rename(old_path, new_path)
            print(f"✅ 成功重命名：{filename} -> {new_name}\n")
            counter += 1  # 只有成功处理后，计数器才加 1
        except Exception as e:
            print(f"❌ 失败：{filename} (原因: {e})\n")

    print(f"\n🎉 完成！共处理了 {counter - 1} 个文件。")

if __name__ == "__main__":
    run_rename()