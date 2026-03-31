from utils import cyan_print, sep_print

sep_print()

def remove_duplicates(items: list[str]) -> list[str]:
    to_dict = dict.fromkeys(items)
    return list(to_dict)

list_with_duplicates = ["luiz", "a", "b", "a", "c", "a", "d", "luiz"]
unique_list_items = remove_duplicates(list_with_duplicates)
sep_print()
cyan_print(unique_list_items)
sep_print()

def is_image_file(filename: str) -> bool:
    extensions = (".jpg", ".jpeg", ".png", ".gif", ".bmp")

    name_lowercase = filename.lower()
    return name_lowercase.endswith(extensions)

filename1 = "File.exe"
cyan_print(f"{is_image_file(filename1)=} | {filename1=}")

filename2 = "Image.JPEG"
cyan_print(f"{is_image_file(filename2)=} | {filename2=}")

filename3 = "photo.png"
cyan_print(f"{is_image_file(filename3)=} | {filename3=}")

filename4 = "meme.gif"
cyan_print(f"{is_image_file(filename4)=} | {filename4=}")
