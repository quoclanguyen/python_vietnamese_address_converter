# Python Vietnamese Address Converter

A Python utility for converting old Vietnamese addresses to their updated equivalents based on a reference dataset.

## Features

- Convert an **old-style** ward/district/province to its **new-style** version.
- Support for optional street name preservation.
- Fuzzy matching using trigram similarity and acronym matching for better tolerance of typos or variations.
- Accepts both structured address components and full address strings.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/quoclanguyen/python_vietnamese_address_converter.git
cd python_vietnamese_address_converter
```

Ensure you have the `address.json` file in the repository root (already included in the repo).

---

## Usage

### 1. Convert using structured components

```python
from main import get_new_address

result = get_new_address(
    old_ward="Xã Bản Lầu",
    old_district="Huyện Mường Khương",
    old_province="Tỉnh Lào Cai"
)

print(result)
# Output: ('Xã Bản Lầu (mới)', 'Tỉnh Lào Cai (mới)') or -1 if not found
```

---

### 2. Convert using a single address string

```python
from main import get_new_address_by_str

result = get_new_address_by_str(
    "Phường Ninh Giang, Thị xã Ninh Hòa, Khánh Hòa"
)

print(result)
# Output: ('Phường Ninh Giang (mới)', 'Tỉnh Khánh Hòa (mới)') or -1 if not found
```

---


## Dataset

The `address.json` file contains the mapping between **old** and **new** addresses.  
Each entry has fields like:

```json
{
  "old_ward_name": "...",
  "old_district_name": "...",
  "old_province_name": "...",
  "new_ward_name": "...",
  "new_province_name": "..."
}
```

---

## License

MIT License © 2025 Quốc Lân Nguyễn
