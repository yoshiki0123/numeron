import random

# Gameの設定
answer_length = 3 # 答えの桁数
game_count = 10 # Gameの試行回数

# 三桁の異なる数字を生成
def generate_answer():
    numbers = list(range(10)) # 0〜9の数字リストを作成
    random.shuffle(numbers) # 数字リストをシャッフル 
    answer = numbers[0:answer_length]
    return list(map(str, answer)) # 数字を文字列として返す

# 入力の数字を取得
def get_user_input():
    while True:
        user_input = input(f"{answer_length}桁の数値を入力してください: ")

        # 半角数字かどうかを確認し、3桁かどうかをチェック
        if user_input.isdigit() and len(user_input) == answer_length and all(ord(char) < 128 for char in user_input):
            # すべての桁が異なるかどうかを確認
            if len(set(user_input)) == answer_length:
                return list(user_input)
            else:
                print("無効な入力です。すべての桁が異なる数字を入力してください。")
        else:
            print(f"無効な入力です。{answer_length}桁の半角数字を入力してください")

# 入力された数字の判定
def user_input_judgment(user_input, answer):
    Great_num = 0
    Good_num = 0
    for i in range(len(answer)):
        # Greatの判定
        if user_input[i] == answer[i]:
            Great_num += 1
        # Goodの判定
        elif user_input[i] in answer:
            Good_num += 1
    return Great_num, Good_num



# main文
def main():
    print("Gameを開始します!")
    answer = generate_answer() 

    for current_game_count in range(1,game_count+1):
        print(f"{current_game_count}回目のチャレンジ!")
        user_input = get_user_input() 
        Great_num, Good_num = user_input_judgment(user_input, answer) # Great&Goodをカウント
        if Great_num == answer_length:
            print("成解です!!")
            return 
        else:
            print(f"Eat:{Great_num}\nBite:{Good_num}")
        
    print(f"残念でした。答えは{''.join(answer)}です。")
    

if __name__ == '__main__':
    main()