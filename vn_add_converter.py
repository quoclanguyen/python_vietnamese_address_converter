import json
from algorithms import *

convert_data = json.load(open("address.json", "r", encoding="utf-8-sig"))
convert_data = convert_data[-1]["data"]

def get_new_address(old_ward: str, old_district: str, old_province: str, street = ""):
    """
    Find new address using old address information.
    Returns new address: street, ward, province. If new address cannot be found, return -1.

    Arguments:
        old_ward: old ward string to match with data.
        old_district: old district string to match with data.
        old_province: old province string to match with data.
        street: optional street info.

    Example:
        ```
        get_new_address(old_ward = "Xã Bản Lầu", old_district = "Huyện Mường Khương", old_province = "Tỉnh Lào Cai")
        ```
        
    """
    global convert_data
    for dict_ in convert_data:
        if trigram(str(dict_["old_ward_name"]).lower(), old_ward.lower()) < 0.5:
            continue
        if trigram(str(dict_["old_district_name"]).lower(), old_district.lower()) < 0.5:
            continue
        data_old_province = str(dict_["old_province_name"]).lower()
        if trigram(data_old_province, old_province.lower()) < 0.5:
            if trigram(acronymize(data_old_province), old_province.lower(), 2) < 0.5:
                continue
        if street != "":
            return street, dict_["new_ward_name"], dict_["new_province_name"]
        return dict_["new_ward_name"], dict_["new_province_name"]
    return -1

def get_new_address_by_str(address_str: str):
    """
    Find new address using old address string.
    Returns new address: street, ward, province. If new address cannot be found, return -1.

    Arguments:
        address_str: address line, must be string.
    
    Examples:
        ```
        get_new_address_by_str("Phường Ninh Giang, Thị xã Ninh Hòa, Khánh Hòa")
        get_new_address_by_str("Lô 28, Khu Công nghiệp Trà Nóc 1, Phường Trà Nóc, Quận Bình Thuỷ, Thành phố Cần Thơ")
        ```
    """
    address_str_splitted = address_str.strip().split(", ")
    length = len(address_str_splitted)
    street = ""
    if length > 3:
        for i in range(length - 3):
            street += address_str_splitted[i]
            if i < length - 4: street += ", " 
    ward, district, province = address_str_splitted[-3], address_str_splitted[-2], address_str_splitted[-1]
    return get_new_address(old_ward = ward, old_district = district, old_province = province, street = street)