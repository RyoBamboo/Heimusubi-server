# -*- coding: utf-8 -*-

import psycopg2
import time
from datetime import datetime

def func_create_table(conn):
	try:
		cursor = conn.cursor()
		cursor.execute('\
			CREATE TABLE addresses( \
				id SERIAL, \
				open_weather_id int, \
				address_name varchar(80), \
				weather_status int, \
				created int, \
				modified int \
		)')
		conn.commit()
		print('テーブルの作成が完了しました')
	except:
		print('テーブルの作成時にエラーが発生しました')
		cursor.close()
		conn.rollback()


def func_drop_table(conn):
	try:
		cursor = conn.cursor()
		cursor.execute('DROP TABLE "addresses"')
		conn.commit()
		print('テーブルの削除が完了しました')
	except:
		print('テーブルの削除時にエラーが発生しました')
		cursor.close()
		conn.rollback()


def func_insert_data(filename, conn):
	try:
		cursor = conn.cursor()
		for line in open(filename, 'r'):
			line = line.replace('\n', '')
			address_info = line.split(",") # address_info[0]にID, [1]に名前が入る
			id = address_info[0]
			name = address_info[1]
			status = 0
			created =  int(datetime.now().strftime('%s'))
			modified =  int(datetime.now().strftime('%s'))
			sql = "INSERT INTO addresses(open_weather_id, address_name, weather_status, created, modified) \
				VALUES (%(open_weather_id)s, %(address_name)s, %(weather_status)s, %(created)s, %(modified)s)"
			cursor.execute(sql, {'open_weather_id':id, 'address_name':name, 'weather_status':status, 'created':created, 'modified': modified})
			conn.commit()

		print('データの挿入が完了しました')
	except:
		print('データの挿入時にエラーが発生しました')
		cursor.close()
		conn.rollback()



if __name__ == '__main__':
	filename = './city_list.txt'

	# DBへの接続
	conn = psycopg2.connect(host='localhost', database='heimusubi-server', user='takenoshita', password='')

	# Usersテーブルの削除
	func_drop_table(conn)

	#Usersテーブルの作成
	func_create_table(conn)

	#データの挿入
	func_insert_data(filename, conn)

