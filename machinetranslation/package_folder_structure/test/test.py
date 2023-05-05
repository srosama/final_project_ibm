from package_folder_structure import translator
test_en_fr = translator.Trans_English_To_French("My name is osama and yours?".capitalize())
test_fr_en = translator.Trans_French_To_English("Mon nom est osama et le tien?")
print(f" This is FR: {test_en_fr.convert_EN_FR()}")
print(f" This is EN: {test_fr_en.convert_FR_EN()}")
