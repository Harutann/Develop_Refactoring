import random
repeat_horizontal = random.random(0,10)
repeat_vertical = random.random(0,10)

def process_string(input_str, repeat_horizontal, repeat_vertical):
    if not (5 <= len(input_str) <= 10):
        raise ValueError("文字列は5文字以上10文字以下である必要があります。")
    
    if not input_str.isalpha():
        raise ValueError("アルファベット(a～z, A～Z)以外の文字が含まれています。")
    
    repeated_horizontal = input_str * repeat_horizontal
    
    return '\n'.join([repeated_horizontal for _ in range(repeat_vertical)])

try:
    result = process_string("Test", 3, 4)
    print(result)
except ValueError as e:
    print(f"エラー: {e}")
