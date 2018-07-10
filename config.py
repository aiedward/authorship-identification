# -*- coding: utf-8 -*-
# Author: XuMing <xuming624@qq.com>
# Brief: 
# data
import os

train_seg_path = "data/training_new_seg.txt"  # segment of train file
test_seg_path = "data/testing_seg.txt"  # segment of test file

sentence_symbol_path = 'data/sentence_symbol.txt'
stop_words_path = 'data/stop_words.txt'

# one of "tfidf_char, tfidf_word, language, tfidf_char_language", ignore when model_type="cnn"
feature_type = 'tfidf_char'
# one of "logistic_regression, random_forest, bayes, decision_tree, svm, knn, xgboost, xgboost_lr, mlp, ensemble, stack, cnn"
model_type = "ensemble"
output_dir = "output"

pr_figure_path = output_dir + "/R_P.png"  # precision recall figure
model_save_path = output_dir + "/model_" + feature_type + "_" + model_type + ".pkl"  # save model path
vectorizer_path = output_dir + "/vectorizer_" + feature_type + ".pkl"

# xgboost_lr model
xgblr_xgb_model_path = output_dir + "/xgblr_xgb.pkl"
xgblr_lr_model_path = output_dir + "/xgblr_lr.pkl"
feature_encoder_path = output_dir + "/xgblr_encoder.pkl"

pred_save_path = output_dir + "/validation_seg_result.txt"  # infer data result
col_sep = '\t'  # separate label and content of train data
pred_thresholds = 0.5
num_classes = 4  # num of data label classes

# --- train_w2v_model ---
# path of train sentence, if this file does not exist,
# it will be built from train_seg_path data by train_w2v_model.py train
# word2vec bin path
sentence_w2v_bin_path = output_dir + "/sentence_w2v.bin"
# word_dict saved path
sentence_w2v_path = output_dir + "/sentence_w2v.pkl"

# --- train ---
word_vocab_path = output_dir + "/word_vocab.txt"
pos_vocab_path = output_dir + "/pos_vocab.txt"
label_vocab_path = output_dir + "/label_vocab.txt"
word_vocab_start = 2
pos_vocab_start = 1

# embedding
w2v_path = output_dir + "/w2v.pkl"
p2v_path = output_dir + "/p2v.pkl"  # pos vector path
w2v_dim = 256
pos_dim = 64

# param
max_len = 300  # max len words of sentence
min_count = 5  # word will not be added to dictionary if it's frequency is less than min_count
batch_size = 128
nb_epoch = 5
keep_prob = 0.5
word_keep_prob = 0.9
pos_keep_prob = 0.9

# directory to save the trained model
# create a new directory if the dir does not exist
model_save_temp_dir = "output/save_model"
best_result_path = output_dir + "/best_result.csv"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)
if not os.path.exists(model_save_temp_dir):
    os.mkdir(model_save_temp_dir)
