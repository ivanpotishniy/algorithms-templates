import random
import string


class MarsURLEncoder:
    def __init__(self):
        # Словарь для хранения пар: хеш → исходная ссылка
        self.url_map = {}
        # Набор символов для генерации хеша: буквы (верхний/нижний регистр) и цифры
        self.charset = string.ascii_letters + string.digits
        # Длина хеша — 6 символов
        self.hash_length = 6

    def _generate_hash(self):
        """Генерирует случайный хеш длиной hash_length из charset."""
        return ''.join(random.choice(self.charset) for _ in range(self.hash_length))

    def encode(self, long_url):
        """
        Кодирует длинную ссылку в короткую вида https://ma.rs/X7NYIol.

        Args:
            long_url (str): Исходная ссылка для шифрования.

        Returns:
            str: Зашифрованная ссылка вида https://ma.rs/<hash>.
        """
        # Генерируем хеш и проверяем его уникальность
        while True:
            hash_part = self._generate_hash()
            # Если хеш уже существует, генерируем новый
            if hash_part not in self.url_map:
                break

        # Формируем зашифрованную ссылку
        short_url = f"https://ma.rs/{hash_part}"
        # Сохраняем пару в словарь: хеш → исходная ссылка
        self.url_map[hash_part] = long_url

        return short_url

    def decode(self, short_url):
        """
        Декодирует короткую ссылку вида https://ma.rs/X7NYIol в исходную.

        Args:
            short_url (str): Зашифрованная ссылка.

        Returns:
            str or None: Исходная ссылка, если найдена; None, если не найдена.
        """
        # Извлекаем хеш из зашифрованной ссылки
        # Ожидаемый формат: https://ma.rs/X7NYIol
        if not short_url.startswith("https://ma.rs/"):
            return None

        # Берём часть после префикса
        hash_part = short_url[len("https://ma.rs/"):]

        # Ищем исходную ссылку по хешу
        return self.url_map.get(hash_part)


encoder = MarsURLEncoder()

url1 = "https://tsup.ru/mars/marsohod-1/01-09-2023/daily_job.html"
url2 = "https://tsup.ru/impunity/01092023/whats_new/"
url3 = "https://mars-program.ru/all/010923/plan_B.htm"

encoded1 = encoder.encode(url1)
encoded2 = encoder.encode(url2)
encoded3 = encoder.encode(url3)

print("Зашифрованные ссылки:")
print(f"{url1} → {encoded1}")
print(f"{url2} → {encoded2}")
print(f"{url3} → {encoded3}")

decoded1 = encoder.decode(encoded1)
decoded2 = encoder.decode(encoded2)
decoded3 = encoder.decode(encoded3)

print("\nРасшифрованные ссылки:")
print(f"{encoded1} → {decoded1}")
print(f"{encoded2} → {decoded2}")
print(f"{encoded3} → {decoded3}")
