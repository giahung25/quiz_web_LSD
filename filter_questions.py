import json
import os

# Set working directory to the data folder
os.chdir(r'd:\tai_lieu_hk2_nam_2\on_thi\References\lich_su_dang_cong_san_viet_nam\data')

files_to_read = ['bai_trac_nghiem_lsd(1).json', 'bai_trac_nghiem_lsd.json']
out_file = 'bai_trac_nghiem_lsd_dai_hoi_hoi_nghi.json'

all_filtered = []

for filename in files_to_read:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for q in data.get('questions', []):
                text = q.get('question', '').lower()
                if 'hội nghị' in text or 'đại hội' in text:
                    all_filtered.append(q)
    except Exception as e:
        print(f"Error reading {filename}: {e}")

out_data = {
    "section": "BÀI TRẮC NGHIỆM - ĐẠI HỘI & HỘI NGHỊ",
    "questions": all_filtered
}

with open(out_file, 'w', encoding='utf-8') as f:
    json.dump(out_data, f, ensure_ascii=False, indent=2)

print(f"Extracted {len(all_filtered)} questions.")
