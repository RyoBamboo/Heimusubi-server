# -*- coding: utf-8 -*-

import psycopg2

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


def func_insert_data(filename):
	for line in open(filename, 'r'):
		print(line)


	# try:
	# except:
	# 	print('データの挿入時にエラーが発生しました')



if __name__ == '__main__':
	filename = 'city_list.txt'

	# DBへの接続
	conn = psycopg2.connect(host='localhost', database='heimusubi-server', user='takenoshita', password='')

	# Usersテーブルの削除
	func_drop_table(conn)

	#Usersテーブルの作成
	func_create_table(conn)

	#データの挿入
	func_insert_data(filename)

