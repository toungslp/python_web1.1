print("ຄິດໄລ່ຍອດຂາຍສຳລັບໃດ?")

today = str(input("ກະລຸນນາບອກມື້:"))

print("ມື້ທີ່ທ່ານຕອບແມ່ນ: ",today)

income = int(input("ລາຍຮັບທັງໝົດທີ່ໄດ້ໃນມື້ນີ້: "))

playment = int(input("ລາຍຈ່າຍທັງໝົດທີ່ລົງທືນໄປ: "))

print("ລາຍຮັບທັງໝົດຂອງວັນ ", today ,"ທັງໝົດແມ່ນ:", income)


print("ລາຍຈ່າຍທັງໝົດຈອງວັນ: ", today, "ທັງໝົດແມ່ນ: ",playment)

#total = income - playment

print("ຍອດເງີນທັງໝົດທີ່ສະຫຼຸບໄດ້ໃນວັນ :" , today, "ແມ່ນ: ", income - playment ," $")
