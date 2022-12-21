class numberSystemDictionary:
    numSysDic = {
        'key1': 'Двійкова(2)',
        'key2': 'Трійкова(3)',
        'key3': 'Вісімкова(8)',
        'key4': 'Шістнадцяткова(16)',
        'key5': 'Десятковий(10)',
        'key6': 'ZM',
        'key7': 'U1',
        'key8': 'U2',
        'key9': 'BIAS=7'
    }

    numForAdd = numSysDic.copy()
    numForAdd.pop("key2")
    numForAdd.pop("key3")
    numForAdd.pop("key4")
    numForAdd.pop("key5")
