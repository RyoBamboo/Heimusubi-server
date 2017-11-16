# coding:utf-8

import librosa
import numpy as np
import os, csv, sys
from sklearn.datasets import load_svmlight_file
from sklearn.externals import joblib
from sklearn.metrics import accuracy_score
from scipy import stats


def mfcc_calculation(voicefilename):

	x, fs = librosa.load(voicefilename, sr = 44100)
	mfccs = librosa.feature.mfcc(x, sr = fs)
	dmfccs = librosa.feature.delta(mfccs)
	result = np.zeros((mfccs.shape[0], 14))

	result[:,0] = np.mean(mfccs, axis = 1)                        # 平均
	result[:,1] = np.var(mfccs, axis = 1, dtype=np.float64)       # 分散
	result[:,2] = stats.skew(mfccs, axis=1)
	result[:,3] = stats.kurtosis(mfccs, axis=1, fisher=False)
	result[:,4] = np.median(mfccs, axis=1)
	result[:,5] = np.min(mfccs, axis=1)
	result[:,6] = np.max(mfccs, axis=1)
	result[:,7] = np.mean(dmfccs, axis=1)
	result[:,8] = np.var(dmfccs, axis=1, dtype=np.float64)
	result[:,9] = stats.skew(dmfccs, axis=1)
	result[:,10] = stats.kurtosis(dmfccs, axis=1, fisher=False)
	result[:,11] = np.median(dmfccs, axis=1)
	result[:,12] = np.min(dmfccs, axis=1)
	result[:,13] = np.max(dmfccs, axis=1)

	result = result.flatten()

	return result


# 第一引数：テストデータ(wavファイル)を第一引数に -> python voice_svm_test.py sample.wav
args = sys.argv
filepath = args[1]

#  テストデータ(音声ファイル)を読み込む
X_testdata = mfcc_calculation(filepath)
X_testdata = np.c_[X_testdata]
X_testdata = X_testdata.transpose()

# 学習した分類器を読み込む。
# svc = joblib.load('svc2.pkl.cmp')
svc = joblib.load('src/api/bin/svc2.pkl.cmp')

# huppy(1),normal(0)を推定する。
y_testdata = svc.predict(X_testdata)
y_testdata = int(y_testdata)

print(y_testdata)
# 予測結果を表示
# return y_testdata

