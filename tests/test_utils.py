from src.utils import read_file
from src.utils import formated_date
from src.utils import sorted_date
from src.utils import executed_last_five
from src.utils import mask_card
from src.utils import mask_bill
from src.utils import mask_numbers_from_and_to


def test_read_file():
    expected = [
        {
            "id": 667307132,
            "state": "EXECUTED",
            "date": "2019-07-13T18:51:29.313309",
            "operationAmount": {
                "amount": "97853.86",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "Maestro 1308795367077170",
            "to": "Счет 96527012349577388612"
        }
    ]
    assert read_file('test_operation.json') == expected


def test_formated_date():
    assert formated_date([{"date": "2013-08-26T10:50:58.294041"},
                          {"date": "2019-08-26T10:50:58.294041"},
                          {"date": "2011-08-26T10:50:58.294041"},
                          {"date": "2020-08-26T10:50:58.294041"},
                          {"date": "2022-08-26T10:50:58.294041"}]) == [{"date": "26.08.2013"},
                                                                       {"date": "26.08.2019"},
                                                                       {"date": "26.08.2011"},
                                                                       {"date": "26.08.2020"},
                                                                       {"date": "26.08.2022"}]


def test_sorted_date():
    assert sorted_date([{"date": "26.08.2013"},
                        {"date": "26.08.2019"},
                        {"date": "26.08.2011"}, ]) == [{"date": "26.08.2019"},
                                                       {"date": "26.08.2013"},
                                                       {"date": "26.08.2011"}]


def test_executed_last_five():
    assert executed_last_five([{"state": "EXECUTED"},
                               {"state": "CANCELED"},
                               {"state": "CANCELED"}, ]) == [{"state": "EXECUTED"}]


def test_mask_card():
    assert mask_card("Visa Classic 4610247282706784") == "Visa Classic 4610 24** **** 6784"


def test_mask_bill():
    assert mask_bill("Счет 51958934737718181351") == "Счет **1351"


def test_mask_numbers_from_and_to():
    data = [
        {
            "from": "Maestro 1308795367077170",
            "to": "Счет 96527012349577388612"
        },
        {
            "from": "Maestro 1308795367077170",
            "to": "Maestro 1308795367077170"
        },
        {
            "from": "Счет 96527012349577388612",
            "to": "Счет 96527012349577388612"
        },
        {
            "to": "Счет 96527012349577388612"
        }

    ]

    expected = [
        {
            "from": "Maestro 1308 79** **** 7170",
            "to": "Счет **8612"
        },
        {
            "from": "Maestro 1308 79** **** 7170",
            "to": "Maestro 1308 79** **** 7170"
        },
        {
            "from": "Счет **8612",
            "to": "Счет **8612"
        },
        {
            "to": "Счет **8612"
        }

    ]
    assert mask_numbers_from_and_to(data) == expected
