def get_words(path = r"C:\Users\Student\Downloads\Text\Game\words.txt"):
    text = open(path, encoding='utf8')
    text_list = text.read().upper().splitlines()
    text.close()
    return text_list

def get_records(record, path = r"C:\Users\Student\Downloads\Text\Game\records.txt"):
    record_file = open(path, mode = "r+", encoding="utf8")
    cur_record = record_file.readline()
    cur_record = max(int(cur_record), int(record))
    record_file.seek(0)
    record_file.write(str(cur_record))
    return cur_record

if __name__ == "__main__":
    # print(get_words())
    # print(get_records(50))

    print(__file__) # Значение данного атрибута можно использовать для инициализации абсолютного! пути к файлу со словами по умолчанию
