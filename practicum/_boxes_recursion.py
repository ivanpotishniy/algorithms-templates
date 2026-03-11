class Box:

    def __init__(self, size, inner_items=None):
        self.size = size
        self.inner_items = inner_items

    def __repr__(self):
        return self.size


def disassemble_boxes(box):
    """Функция разборки коробок."""
    print(f'Взяли коробку размера {box.size}, внутри: {box.inner_items}.')
    for item in box.inner_items:
        if item.inner_items is None:
            print(f'В коробке размера {item.size} больше ничего нет.')
            # continue - перейти к следующему шагу цикла, не выполняя код ниже.
            continue
        disassemble_boxes(item)


if __name__ == '__main__':
    small_boxes = [Box(size='S') for _ in range(4)]
    middle_box_full = Box(size='M', inner_items=small_boxes)
    middle_box_empty = Box(size='M')
    large_box = Box(size='L', inner_items=[middle_box_empty, middle_box_full])
    disassemble_boxes(large_box)
