from PIL import Image
import os

# Шаг 1: Исходное изображение
original_image = Image.open("image_test.jpg").convert("RGB")
print(f"Исходное изображение: режим {original_image.mode}")

# Шаг 2: Разделяем на каналы
red, green, blue = original_image.split()

# Шаг 3: Сохраняем каналы как отдельные файлы
red.save("red_channel.jpg")
green.save("green_channel.jpg")
blue.save("blue_channel.jpg")
print("Каналы сохранены как отдельные файлы")

# Шаг 4: Удаляем исходное изображение (если нужно)
# os.remove("image_test.jpg")  # Раскомментируйте, если нужно удалить

# Шаг 5: Позже собираем обратно из сохраненных каналов
red_reloaded = Image.open("red_channel.jpg").convert("L")
green_reloaded = Image.open("green_channel.jpg").convert("L")
blue_reloaded = Image.open("blue_channel.jpg").convert("L")

final_image = Image.merge("RGB", (red_reloaded, green_reloaded, blue_reloaded))
final_image.save("final_reconstructed.jpg")
print("Изображение собрано из сохраненных каналов!")

# Шаг 6: Сравнение размеров (опционально)
print(f"\nСравнение размеров:")
print(f"Красный канал: {red_reloaded.size}")
print(f"Зеленый канал: {green_reloaded.size}")
print(f"Синий канал: {blue_reloaded.size}")