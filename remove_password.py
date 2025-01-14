from PyPDF2 import PdfReader, PdfWriter

def remove_pdf_password(input_path, output_path, password):
    # 创建 PDF reader 对象
    reader = PdfReader(input_path)
    
    # 如果 PDF 有加密，则使用密码解密
    if reader.is_encrypted:
        reader.decrypt(password)
    
    # 创建 PDF writer 对象
    writer = PdfWriter()
    
    # 将所有页面添加到新的 PDF 中
    for page in reader.pages:
        writer.add_page(page)
    
    # 保存无密码的 PDF
    with open(output_path, 'wb') as output_file:
        writer.write(output_file)

# 使用示例
input_pdf = "资料（密码：hsw111111）\AutoGen实现多智能体对话机器人.pdf"
output_pdf = "decrypted.pdf"
pdf_password = "hsw111111"

try:
    remove_pdf_password(input_pdf, output_pdf, pdf_password)
    print("PDF 密码已成功移除！")
except Exception as e:
    print(f"发生错误: {str(e)}") 