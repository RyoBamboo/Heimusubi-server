# -*- coding: utf-8 -*-

import psycopg2

def func_create_table(conn):

	try:
		cursor = conn.cursor()
		cursor.execute('\
			CREATE TABLE users( \
				id SERIAL, \
				user_name varchar(80), \
				email varchar(80), \
				password varchar(80), \
				status int, \
				heimu_id int, \
				created timestamp, \
				modified timestamp \
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
		cursor.execute('DROP TABLE "users"')
		conn.commit()
		print('テーブルの削除が完了しました')
	except:
		print('テーブルの削除時にエラーが発生しました')
		cursor.close()
		conn.rollback()


if __name__ == '__main__':
	# DBへの接続
	conn = psycopg2.connect(host='localhost', database='heimusubi-server', user='takenoshita', password='')

	# Usersテーブルの削除
	func_drop_table(conn)

	#Usersテーブルの作成
	func_create_table(conn)

