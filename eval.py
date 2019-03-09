total_chars = 0
correct_chars = 0
dis_matched_chars = 0


def match_char(real_str, recognized_str):
    global total_chars
    global correct_chars
    global dis_matched_chars
    error_flag = 0
    for real_char, reco_char in zip(real_str, recognized_str):
        total_chars += 1
        if real_char == reco_char:
            correct_chars += 1
        else:
            print(real_char, "--->", reco_char)
            dis_matched_chars += 1
            error_flag = 1

    if error_flag == 1:
        print(real_str, "-->", recognized_str)
        print("--------")


def match_words():
    real_txt = open("actual_output_lines.txt")
    recognized_txt = open("ocr_output_lines.txt")
    for real_line, reco_line in zip(real_txt, recognized_txt):
        for i in range(len(real_line.split())):
            match_char(real_line.split()[i], reco_line.split()[i])


if __name__ == '__main__':
    match_words()
    print("============STATSTICS====================")
    print("toatl chars --->", total_chars )
    print("correct chars --->",correct_chars)
    print("dismatched char---> ", dis_matched_chars)
    print("Accurecy-->",(correct_chars/total_chars)*100)
