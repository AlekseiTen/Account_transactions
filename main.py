from src.utils import read_file, formated_date, sorted_date, executed_last_five, mask_numbers_from_and_to

def main():
    open_json = read_file(r'operations.json')
    formated = formated_date(open_json)
    sorted = sorted_date(formated)
    last_five = executed_last_five(sorted)
    get_mask_numbers = mask_numbers_from_and_to(last_five)

    for item in get_mask_numbers:
        print(f"{item.get('date')} {item.get('description')}\n"
              f"{item.get('from', '')} -> {item.get('to')}\n"
              f"{item['operationAmount']['amount']} {item['operationAmount']['currency']['name']}\n")


if __name__ == '__main__':
    main()