import yadisk
import aiofiles
import os
from dotenv import load_dotenv

load_dotenv()

client = yadisk.AsyncClient(token=os.getenv("YANDEX_API_TOKEN"))
# или
# client = yadisk.AsyncClient("<application-id>", "<application-secret>", "<token>")

# Вы можете использовать либо конструкцию with, либо вручную вызвать client.close() в конце
async with client:
    # Проверяет, валиден ли токен
    print(await client.check_token())

    # Получает общую информацию о диске
    print(await client.get_disk_info())

    # Выводит содержимое "/some/path"
    print([i async for i in client.listdir("/some/path")])

    # Загружает "file_to_upload.txt" в "/destination.txt"
    await client.upload("file_to_upload.txt", "/destination.txt")

    # То же самое
    async with aiofiles.open("file_to_upload.txt", "rb") as f:
        await client.upload(f, "/destination.txt")

    # То же самое, но с обычными файлами
    with open("file_to_upload.txt", "rb") as f:
        await client.upload(f, "/destination.txt")

    # Скачивает "/some-file-to-download.txt" в "downloaded.txt"
    await client.download("/some-file-to-download.txt", "downloaded.txt")

    # То же самое
    async with aiofiles.open("downloaded.txt", "wb") as f:
        await client.download("/some-file-to-download.txt", f)

    # Безвозвратно удаляет "/file-to-remove"
    await client.remove("/file-to-remove", permanently=True)

    # Создаёт новую папку "/test-dir"
    print(await client.mkdir("/test-dir"))