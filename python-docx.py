from docx import Document


# replace không bị lỗi định dạng

def replace_string(filename):
    doc = Document(filename)
    for p in doc.paragraphs:
        if 'old text' in p.text:
            inline = p.runs
            # Loop added to work with runs (strings with same style)
            for i in range(len(inline)):
                if 'old text' in inline[i].text:
                    text = inline[i].text.replace('old text', 'new text')
                    inline[i].text = text
            print(p.text)

    doc.save('dia_chi_file')
    return 1


dia_chi_file = "E:\BÁO CÁO NGÀY 09.04.2016 ĐLĐQ.docx"
thuc_hien = replace_string(dia_chi_file)
