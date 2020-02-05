send_data = []
print('＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝')
print('指示に従い、光熱費を入力してください')
print('＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝')

print('1. 対象年月を入力してください(format: yyyymm)')
send_data.append(int(input()))

print('2. ガス料金を入力してください')
send_data.append(int(input()))

print('3. 電気料金を入力してください')
send_data.append(int(input()))

print('4. 水道料金を入力してください')
send_data.append(int(input()))

import record_costs_excel as ex
ex.w_xl(send_data)
print('スプレッドシートに書き込みが完了しました')
print('[対象年月,ガス,電気,水道]')
print(send_data)
import time
time.sleep(5)
