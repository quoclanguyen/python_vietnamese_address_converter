import json
from fuzzy_match import algorithims as fuzzer

convert_data = json.load(open("address.json", "r", encoding="utf-8-sig"))
convert_data = convert_data[-1]["data"]

def get_new_address(old_ward: str, old_district: str, old_province: str, street = ""):
    global convert_data
    for dict_ in convert_data:
        if fuzzer.trigram(str(dict_["old_ward_name"]).lower(), old_ward.lower()) < 0.5:
            continue
        if fuzzer.trigram(str(dict_["old_district_name"]).lower(), old_district.lower()) < 0.5:
            continue
        if fuzzer.trigram(str(dict_["old_province_name"]).lower(), old_province.lower()) < 0.5:
            continue
        if street != "":
            return street, dict_["new_ward_name"], dict_["new_province_name"]
        return dict_["new_ward_name"], dict_["new_province_name"]
    return -1

def get_new_address_by_str(address_str: str):
    address_str_splitted = address_str.strip().split(", ")
    length = len(address_str_splitted)
    street = ""
    if length > 3:
        for i in range(length - 3):
            street += address_str_splitted[i]
            if i < length - 4: street += ", " 
    ward, district, province = address_str_splitted[-3], address_str_splitted[-2], address_str_splitted[-1]
    return get_new_address(old_ward = ward, old_district = district, old_province = province, street = street)
    
# Các use case
print(get_new_address(old_ward = "Xã Bản Lầu", old_district = "Huyện Mường Khương", old_province = "Tỉnh Lào Cai"))
print(get_new_address_by_str("Phường Ninh Giang, Thị xã Ninh Hòa, Khánh Hòa"))
print(get_new_address_by_str("Lô 28, Khu Công nghiệp Trà Nóc 1, Phường Trà Nóc, Quận Bình Thuỷ, Thành phố Cần Thơ"))