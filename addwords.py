#!/usr/bin/python3

import sys
import os

if 5 != len(sys.argv):
    print("")
    print("Add word to Canna server")
    print("")
    print("|品詞コード |品詞名                            |例           |")
    print("+------------------------------------------------------------+")
    print("|#T35       |名詞( 一般的な名詞)               |山、本       |")
    print("|#T30       |サ変名詞                          |努力、検査   |")
    print("|#KK        |団体・会社名                      |　           |")
    print("|#JN        |人名                              |　           |")
    print("|#CN        |地名                              |　           |")
    print("|#K5        |動詞( か行5 段活用)               |描く         |")
    print("|#G5        |動詞( が行5 段活用)               |注ぐ         |")
    print("|#S5        |動詞( さ行5 段活用)               |倒す         |")
    print("|#T5        |動詞( た行5 段活用)               |絶つ         |")
    print("|#N5        |動詞( な行5 段活用)               |死ぬ         |")
    print("|#B5        |動詞( ば行5 段活用)               |転ぶ         |")
    print("|#M5        |動詞( ま行5 段活用)               |住む         |")
    print("|#R5        |動詞( ら行5 段活用)               |威張る       |")
    print("|#W5        |動詞( わ( あ) 行5 段活用)         |言う         |")
    print("|#KS        |動詞( 上下一段活用)               |降りる       |")
    print("|#KX        |動詞( カ変活用)                   |来る         |")
    print("|#ZX        |動詞( ザ変活用)                   |感ずる       |")
    print("|#SX        |動詞( サ変活用)                   |関する       |")
    print("|#K5r       |動詞( か行5 段で連用形が名詞)     |動く         |")
    print("|#C5r       |動詞( か行5 段で連用形が名詞特殊) |　           |")
    print("|#G5r       |動詞( が行5 段で連用形が名詞)     |急ぐ         |")
    print("|#S5r       |動詞( さ行5 段で連用形が名詞)     |写す         |")
    print("|#T5r       |動詞( た行5 段で連用形が名詞)     |勝つ         |")
    print("|#B5r       |動詞( ば行5 段で連用形が名詞)     |遊ぶ         |")
    print("|#M5r       |動詞( ま行5 段で連用形が名詞)     |歩む         |")
    print("|#R5r       |動詞( ら行5 段で連用形が名詞)     |見張る       |")
    print("|#W5r       |動詞( わ( あ) 行5 段で連用形が名  |扱う         |")
    print("|#KSr       |動詞( 上下1 段，語幹が名詞)       |生きる       |")
    print("|#KY        |形容詞                            |美しい、早い |")
    print("|#KYT       |形容詞                            |古い         |")
    print("|#T00       |形容動詞( サ変名詞としても使う)   |心配だ       |")
    print("|#T05       |形容動詞                          |幸運だ       |")
    print("|#F04       |副詞                              |　           |")
    print("|#F06       |副詞                              |             |")
    print("|#F12       |副詞                              |　           |")
    print("|#F14       |副詞                              |飽くまで     |")
    print("|#KJ        |単漢字                            |　           |")
    print("|#NN        |数詞                              |何           |")
    print("|#RT        |連体詞                            |　           |")
    print("|#CJ        |接続詞・感動詞                    |及び         |")
    print("")
    print(" USAGE:")
    print("")
    print("  $ {} よみ 品詞コード 漢字 dict".format(sys.argv[0]))
    print("")
    print(" EXAMPLE:")
    print("")
    print("  $ {} ぶながだけ \\#T35 武奈ヶ岳 user".format(sys.argv[0]))
    print("")
    exit()

read = sys.argv[1]
part = sys.argv[2]
kanj = sys.argv[3]
dict = sys.argv[4]


# Do addwords
cmd = "echo '{} {} {}' | iconv -t euc-jp | addwords {}".format(
    read, part, kanj, dict)

print(cmd)
stdout = os.popen(cmd).read()
print(stdout)
