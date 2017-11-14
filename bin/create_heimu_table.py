# -*- coding: utf-8 -*-

import psycopg2
import time
from datetime import datetime

def func_create_table(conn):
	try:
		cursor = conn.cursor()
		cursor.execute('\
			CREATE TABLE heimus( \
				id SERIAL, \
				heimu_name varchar(80), \
				related_heimu_ids varchar(80), \
				belong_user_ids varchar(80), \
				address_id int, \
				is_sleep int, \
				serial_number int, \
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


if __name__ == '__main__':

	# DBへの接続
	conn = psycopg2.connect(host='localhost', database='heimusubi-server', user='takenoshita', password='')

	# Heimusテーブルの削除
	func_drop_table(conn)

	# Heimusテーブルの作成
	func_create_table(conn)


