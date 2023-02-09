from .tg_parser import parser


def save(parse_data_class):
    parse_data_class.objects.all().delete()
    data = parser.start()
    for text, tag, date, photo_path in data:
        parse_data_class.objects.create(text=text, tag=tag, date=date, photo_path=photo_path)

