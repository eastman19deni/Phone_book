from logging import Logger

from phonebook import LenNumberError

def get_new_contact(edit, modifying_contact):
    if edit:
        first_name_old = modifying_contact["Имя"]
        second_name_old = modifying_contact["Отчество"]
        last_name_old = modifying_contact["Фамилия"]
        print("Чтобы сохранить текущее значение, оставьте строку пустой.")
        print("Для определения пустого значения введите один пробел")
        first_name = input(f"Введите имя ({first_name_old}): ")
        second_name = input(f"Введите отчество ({second_name_old}): ")
        last_name = input(f"Введите фамилию ({last_name_old}): ")
        if first_name == " ":
            first_name = ""
        elif first_name == "":
            first_name = first_name_old
        if second_name == " ":
            second_name = ""
        elif second_name == "":
            second_name = second_name_old
        if last_name == " ":
            last_name = ""
        elif last_name == "":
            last_name = last_name_old
    else:
        first_name = input("Введите имя: ")
        second_name = input("Введите отчество: ")
        last_name = input("Введите фамилию: ")
    phone_number = 0
    is_valid_phone = False
    while not is_valid_phone:
        try:
            if edit:
                phone_number_old = modifying_contact["Телефон"]
                phone_number_string = input(f"Введите номер ({str(phone_number_old)}): ")
                if phone_number_string == "":
                    phone_number_string = str(phone_number_old)
                phone_number = int(phone_number_string)
            else:
                phone_number = int(input("Введите номер: "))
            if len(str(phone_number)) != 11:
                raise LenNumberError("Неверная длина номера.")
        except ValueError:
            print("Номер должен состоять только из цифр.")
        except LenNumberError as error:
            print(error)
            continue
        is_valid_phone = True
    return {"Имя": first_name, "Отчество": second_name, "Фамилия": last_name, "Телефон": phone_number}
